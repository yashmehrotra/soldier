from datetime import datetime
import os
import shlex
import signal

from subprocess import (
    PIPE,
    Popen,
)

import warnings

from .exceptions import (
    ProcessDoesNotExistError,
    TimeoutError
)


def kill_family(pid):
    """
    Kills the children and the parents
    """
    os.kill(pid, signal.SIGTERM)


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
        self._status_code = None
        self._background = kwargs.get('background', False)
        self._process = None
        self._pid = None
        self._output = None
        self._std_err = None
        self._start_ts = None
        self._end_ts = None
        self._in_shell = False
        self._is_alive = False
        self._std_in = kwargs.get('stdin', False)
        self._err = None
        self._timeout = kwargs.get('timeout')
        self._kill_on_timeout = kwargs.get('kill_on_timeout')

        self._parse()
        self._validate()

        # The main process handler
        self._run()

    def __repr__(self):
        return "<Soldier [{0}]>".format(self._command)

    def _validate(self):
        """
        Validate kwargs
        """

        if self._background:
            if self._background is not True:
                raise ValueError(
                    'background argument must be boolean')

        if self._timeout:
            try:
                self._timeout = int(self._timeout)
            except ValueError:
                raise ValueError(
                    'timeout argument must be integer')

        if self._kill_on_timeout:
            if self._kill_on_timeout is not True:
                raise ValueError(
                    'kill_on_timeout must be boolean')

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

            self._process = Popen(comm,
                                  shell=self._in_shell,
                                  stdin=PIPE,
                                  stdout=PIPE,
                                  stderr=PIPE)
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

        self._output = self._std_in if self._std_in else None

        self._output, self._err = self._process.communicate(self._output)
        if self._err:
            warnings.warn(self._err, RuntimeWarning)
            pass

        self._status_code = self._process.returncode

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

            if with_honor:
                self._set_communication_params()
                self._finish()
        else:
            raise ProcessDoesNotExistError(
                'The process you are trying to kill does not exist')

    def _handle_timeout(self, signum, frame):
        """
        Handle timeout for a process
        """
        if self._kill_on_timeout:
            self.kill(with_honor=False)

        raise TimeoutError(
            'The process could not be completed in the specified timeframe')

    @property
    def pid(self):
        return self._pid

    @property
    def status_code(self):
        return self._status_code

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
