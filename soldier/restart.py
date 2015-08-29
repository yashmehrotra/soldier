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
    pass


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
        self._start_ts = None
        self._end_ts = None

    def run(self):
        """
        Run handler
        """

        # Things to do-
        # Start the timer
        # Remember about PID
        # Remember about background
        # You have to handle errors gracefully

