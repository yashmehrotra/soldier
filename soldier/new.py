# import should be done in alphabetic order
# Cause PEP-8 \m/
from datetime import time
from subprocess import (
        CalledProcessError,
        PIPE,
        Popen,
        STDOUT,
        call,
        check_output,
    )
import sys
import shlex

class Soldier(object):
    """
    Add docstring here bwahaaha
    """
    
    def __init__(self,command,**kwargs):
        """
        The Constructor
        """
        
        #self._command = Soldier._parse_command(command)
        self._command = command
        self._pid = None
        self._status_code = None
        self._pstart_ts = None
        self._pend_ts = None
        self._output = kwargs.get('output')

    
    @staticmethod
    def _parse_command(command):
        """
        Parse and return shlexed stuff
        """

        command = shlex.split(command)
        return command


    @staticmethod
    def output(command, **kwargs):
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
            #return Soldier(command,output=output)
            return output
        except CalledProcessError:
            return "Error"


    @classmethod
    def call(Soldier, command):
        """
        Call a process
        """

        shlex_command = Soldier._parse_command(command)

        called_process = call(shlex_command)

        return Soldier(command)
    

    @property
    def command(self):
        """
        Return command
        """
        return self._command
    

    @property
    def out(self):
        """
        Return output
        """
        return self._output

def t_output(command):
    """API
    MAYBE"""

    s = Soldier('fuck',output='suck')
    s._status_code = 0

    return s

