# A New Beginning

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
        self._pid = None
        self._output = None
        self._std_err = None
        self._start_ts = None
        self._end_ts = None

        # Call run
        self.run()

    def __repr__(self):
        return "<Soldier [{0}]>".format(self._command)

    def run(self):
        """
        Run handler
        """

        # Things to do-
        # Start the timer
        # Remember about PID
        # Remember about background
        # You have to handle errors gracefully
        print 'Run called'
        p = Popen(self._parsed_command, shell=True, stdout=PIPE, stderr=PIPE)
        self._pid = p.pid
        if not self._background:
            output, err = p.communicate()
            self._output = output
            self._status_code = p.returncode
        return 'h'

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
        return 'Killed'

    @property
    def start_ts(self):
        return self._start_ts

    @property
    def end_ts(self):
        return self._end_ts
