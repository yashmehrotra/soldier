# import should be done in alphabetic order
# Cause PEP-8 \m/
from datetime import time
from subprocess import (
        CalledProcessError,
        PIPE,
        Popen,
        STDOUT,
        check_output,
    )
import sys
import shlex

class Soldier(object):
    """
    Add docstring here bwahaaha
    """
    
    def __init__(self,command):
        """
        The Constructor
        """
        
        self._command = command
        self._pid = None
        self._status_code = None
        self._pstart_ts = None
        self._pend_ts = None

    
    @staticmethod
    def _parse_command(command):
        """
        Parse and return shlexed stuff
        """

        command = shlex.split(command)
        return command


    @classmethod
    def output(Soldier,command,**kwargs):
        """
        Possible kwargs:
        - split
        - delimiter
        - think of more
        """

        command = Soldier._parse_command(command)

        try:
            output = check_output(
                        command,
                        stderr=STDOUT,
                        #shell=True Commented out as it has to be researched
                    )
            #self._command = command
            return Soldier(command)
        except CalledProcessError:
            return "Error"

    @property
    def command(self):
        """
        Return command
        """
        return self._command
