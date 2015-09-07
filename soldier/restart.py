# A New Beginning
from datetime import datetime
import psutil
from subprocess import (
    CalledProcessError,
    PIPE,
    Popen,
    STDOUT,
    call,
    check_output
)

import sys
import shlex


def kill_family(pid):
    """
    Kills the children and the parents
    """

    process = psutil.Process(pid)
    for child in process.children():
        child.kill()
    process.kill()


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
        self._parsed_command = shlex.split(command)
        self._status_code = None
        self._background = kwargs.get('background', False)
        self._process = None
        self._pid = None
        self._output = None
        self._std_err = None
        self._start_ts = None
        self._end_ts = None
        self._in_shell = True

        # Call run
        self._run()

    def __repr__(self):
        return "<Soldier [{0}]>".format(self._command)

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
        p = Popen(self._parsed_command, shell=True, stdout=PIPE, stderr=PIPE)
        self._pid = p.pid
        self._process = p
        if not self._background:
            self._set_output_and_status_code()

    def _set_output_and_status_code(self):
        """
        Sets output prop and status code
        """

        output, err = self._process.communicate()
        if err:
            # Do something
            pass

        self._output = output
        self._status_code = self._process.returncode
        self._end_ts = datetime.now()

    @property
    def pid(self):
        return self._pid

    @property
    def status_code(self):
        return self._status_code

    @property
    def output(self):
        return self._output

    def kill(self):
        # Kill the fucking process
        # self._process.kill()
        kill_family(self._pid)
        self._set_output_and_status_code()
        return 'Killed'

    @property
    def start_ts(self):
        return self._start_ts

    @property
    def end_ts(self):
        return self._end_ts
