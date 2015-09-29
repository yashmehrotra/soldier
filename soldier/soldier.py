from datetime import datetime
import os
import psutil
import shlex
import signal

from subprocess import (
    CalledProcessError,
    PIPE,
    Popen,
    STDOUT,
    call,
)

import sys
import warnings

from .exceptions import ProcessDoesNotExistError


def kill_family(pid):
    """
    Kills the children and the parents
    """
    os.kill(pid, signal.SIGTERM)
    """
    process = psutil.Process(pid)
    for child in process.children():
        child.kill()
    process.kill()
    """

def run(command, **kwargs):
    """
    API
    """
    return Soldier(command, **kwargs)


def call(command, **kwargs):
    pass


class Soldier(object):
    """
    The main object
    """

    def __init__(self, command, **kwargs):
        """
        The constructor
        """

        self._command = command
        self._status_code = None
        self._background = bool(kwargs.get('background', False))
        self._process = None
        self._pid = None
        self._output = None
        self._std_err = None
        self._start_ts = None
        self._end_ts = None
        self._in_shell = False
        self._is_active = False
        self._std_in = kwargs.get('stdin', False)
        self._err = None

        self._parse()
        # Call run
        self._run()

    def __repr__(self):
        return "<Soldier [{0}]>".format(self._command)

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

        # Things to do-
        # You have to handle errors gracefully
        self._start_ts = datetime.now()
        wait = True if self._background else False
        for comm in self._parsed_command:

            self._process = Popen(comm,
                                  shell=self._in_shell,
                                  stdin=PIPE,
                                  stdout=PIPE,
                                  stderr=PIPE)
            self._pid = self._process.pid
            self._is_active = True

            self._set_communication_params(wait=wait)

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
        self._is_active = False

    def kill(self):
        """
        Kill the current process
        """

        if self._is_active:
            kill_family(self._pid)
            self._set_communication_params()
            self._finish()
        else:
            raise ProcessDoesNotExistError(
                    'The process you are trying to kill does not exist')

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

    @property
    def is_active(self):
        return self._is_active

    @property
    def duration(self):
        try:
            duration = self.end_ts - self.start_ts
        except TypeError:
            duration = None

        return duration

# TODO - Timeout
# TODO - Best way to kill a process
