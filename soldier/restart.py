# A New Beginning
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
        self._background = kwargs.get('background', False)
        self._process = None
        self._pid = None
        self._output = None
        self._std_err = None
        self._start_ts = None
        self._end_ts = None
        self._in_shell = False
        self._is_active = False

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
        # Start the timer
        # Remember about PID
        # Remember about background
        # You have to handle errors gracefully
        print 'Run called'
        self._start_ts = datetime.now()
        for comm in self._parsed_command:

            self._process = Popen(comm,
                                  shell=self._in_shell,
                                  stdin=PIPE,
                                  stdout=PIPE,
                                  stderr=PIPE)
            self._pid = self._process.pid
            self._is_active = True

            if not self._background:
                self._set_communication_params()

        if not self._background:
            self._finish()

    def _set_communication_params(self):
        """
        Sets output prop and status code
        """

        self._output, self._err = self._process.communicate(self._output)
        if self._err:
            # Do something
            print 'Err ' + self._err
            pass

        self._status_code = self._process.returncode

    def _finish(self):
        """
        End a command
        """

        self._end_ts = datetime.now()
        self._is_active = False

    def kill(self):
        # Kill the fucking process
        # self._process.kill()
        kill_family(self._pid)
        self._set_communication_params()

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
    def start_ts(self):
        return self._start_ts

    @property
    def end_ts(self):
        return self._end_ts

    @property
    def is_active(self):
        return self._is_active
