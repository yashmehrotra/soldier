import sys
from datetime import datetime
import shlex
import signal

from subprocess import (
    PIPE,
    Popen,
)

import warnings

from .helpers import (
    kill_family,
    pid_exists
)

from .exceptions import (
    InvalidCommandError,
    ProcessDoesNotExistError,
    ProcessTimeoutError
)


def run(command, **kwargs):
    """
    API
    """
    return Soldier(command, **kwargs)


class Soldier(object):
    """
    The main class object
    """

    def __init__(self, command, **kwargs):
        """
        The constructor
        """

        self._command = command
        self._exit_code = None
        self._background = kwargs.get('background', False)
        self._process = None
        self._pid = None
        self._output = None
        self._std_err = None
        self._start_ts = None
        self._end_ts = None
        self._in_shell = kwargs.get('shell', False)
        self._is_alive = False
        self._cwd = kwargs.get('cwd', None)
        self._env = kwargs.get('env', None)
        self._stream = kwargs.get('stream', False)
        self._std_in = kwargs.get('std_in', False)
        self._output = kwargs.get('std_in', None)  # Hack, think of better way
        self._sudo = bool(kwargs.get('sudo'))
        self._password = kwargs.get('sudo', '') + '\n'
        self._err = None
        self._timeout = kwargs.get('timeout', 0)
        self._kill_on_timeout = kwargs.get('kill_on_timeout', False)
        self._suppress_std_err = kwargs.get('suppress_std_err', False)

        self._parse()
        self._validate()

        # The main process handler
        self._run()

    def __repr__(self):
        return "<Soldier [{0}]>".format(self._command)

    def _validate(self):
        """
        Validate key worded arguments
        """

        if type(self._background) is not bool:
            raise ValueError(
                'background argument must be boolean')

        if type(self._timeout) is not int:
            raise ValueError(
                'timeout argument must be integer')

        if type(self._kill_on_timeout) is not bool:
            raise ValueError(
                'kill_on_timeout must be boolean')

        if type(self._in_shell) is not bool:
            raise ValueError(
                'shell argument must be boolean')

    def _parse(self):
        """
        Parse the command
        """

        command = self._command
        command = command.split('|')
        self._parsed_command = map(shlex.split, command)

    def _run(self):
        """
        Run handler
        """

        self._start_ts = datetime.now()
        wait = True if self._background else False
        self._is_alive = True

        if self._timeout:
            signal.signal(signal.SIGALRM, self._handle_timeout)
            signal.alarm(self._timeout)

        for comm in self._parsed_command:

            if self._sudo:
                comm = ['sudo', '-S'] + comm
            try:
                self._process = Popen(comm,
                                      shell=self._in_shell,
                                      cwd=self._cwd,
                                      env=self._env,
                                      stdin=PIPE,
                                      stdout=PIPE,
                                      stderr=PIPE,
                                      universal_newlines=True)
            except OSError:
                raise InvalidCommandError(
                    'please check the command you are trying to execute')

            self._pid = self._process.pid

            self._set_communication_params(wait=wait)

        if self._timeout:
            signal.alarm(0)

        if not self._background:
            self._finish()

    def _set_communication_params(self, wait=False):
        """
        Sets output prop and status code
        if wait true, backgr process
        """
        if wait:
            return

        # TODO: std_in does not work with sudo
        #       Figure out a way to accommodate it
        if self._sudo:
            self._output = self._password
            self._sudo = False

        if self._stream:
            output = ''
            for line in iter(self._process.stdout.readline, ''):
                sys.stdout.write(line)
                output += line
            self._output = output
            self._err = self._process.stderr.read()
        else:
            self._output, self._err = self._process.communicate(self._output)

        # This even comes as an output for stderr
        if self._err and not self._suppress_std_err:
            print(self._err)

        self._process.poll()
        self._exit_code = self._process.returncode

    def _finish(self):
        """
        End a command
        """

        self._end_ts = datetime.now()
        self._is_alive = False

    def kill(self, with_honor=True):
        """
        Kill the current process
        """

        if self._is_alive:
            kill_family(self._pid)
            self._finish()

            if with_honor:
                self._set_communication_params()
        else:
            raise ProcessDoesNotExistError(
                'The process you are trying to kill does not exist')

    def _handle_timeout(self, signum, frame):
        """
        Handle timeout for a process
        """
        if self._kill_on_timeout:
            self.kill(with_honor=False)

        raise ProcessTimeoutError(
            'The process could not be completed in the specified timeframe')

    @property
    def pid(self):
        return self._pid

    @property
    def status_code(self):
        return self._exit_code

    @property
    def exit_code(self):
        return self._exit_code

    @property
    def output(self):
        return self._output

    @property
    def error(self):
        return self._err

    @property
    def start_ts(self):
        return self._start_ts

    @property
    def end_ts(self):
        return self._end_ts

    def is_alive(self):
        if self._background:
            return pid_exists(self._pid)

        return self._is_alive

    @property
    def timeout(self):
        return self._timeout

    @property
    def kill_on_timeout(self):
        return self._kill_on_timeout

    @property
    def duration(self):
        try:
            duration = self.end_ts - self.start_ts
        except TypeError:
            duration = None

        return duration
