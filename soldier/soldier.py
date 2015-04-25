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

"""
try:
    retcode = call("mycmd" + " myarg", shell=True)
    if retcode < 0:
        print >>sys.stderr, "Child was terminated by signal", -retcode
    else:
        print >>sys.stderr, "Child returned", retcode
except OSError as e:
    print >>sys.stderr, "Execution failed:", e
"""

class Soldier(object):
    def __init__(self, command):
        
        self.command = command
        self.subcomm = shlex.split(command)
        
        # Properties
        self._pid = None
        self._pstart_ts = None
        self._pend_ts = None
        self._status_code = None
        # When you just need to run a background command (open something or copy something etc.)
        if False:
            self.process =  Popen(self.subcomm, shell=True)
        # For everything else
        elif False:
            try:
                self.process = Popen(self.subcomm,
                                     stdin=PIPE,
                                     stdout=PIPE,
                                     stderr=PIPE,
                                     shell=True,
                                )

                (self.out,self.error) = self.process.communicate()

            except Exception as e:
                print "Invalid Command!! Try Again!",e
                sys.exit(1)


    def output(self, split=False, delimiter=None):
        #output = self.out
        # according to docs
        try:
            output = check_output(
                        self.subcomm,
                        stderr=STDOUT,
                        #shell=True
                    )
        
            # The user just wants the ouptput
            if not split:
                return output

            # Output spilt through a delimiter
            elif split and delimiter:
                output = output.split(delimiter)
                output = filter(None,output)
                return output

            # Output split through the default delimiter '\n'
            elif split and not delimiter:
                output = output.split('\n') # The Default
                output = filter(None,output)
                return output
            else:
                print 'Impossible to reach here, if u just gave the delimiter without split u have reached here, I think only delimiter should be given'
        
        except CalledProcessError:
            return self.error


    def call(self):
        # it should return a whole lot of stuff
        process = Popen(self.subcomm, shell=True)
        self._pid = process.pid
        return process


    @staticmethod
    def processes(pid=None):
        # Return a readable list or tuple, if pid give do something more
        pass


    @property
    def pid(self):
        '''
        Return pid
        '''
        return self._pid


    @property
    def status_code(self):
        '''
        Return status code
        '''

        return self._status_code

    

    

if __name__== "__main__":
    command = str(raw_input())
    sub = Soldier(command)
    print sub.output()


# TO - DO
# 1. Handle Error
# 2. Incorporate for modules
# 3. Change Name
# 4. Put it on pip
# 5. travis.yml
# 6. implement in cyberoam rescue
# 7. cyberoam rescue as a shell command, where it automatically asks to input user, pass etc.'
# 8. grep not working, or any another pipe command .... soldier('history|grep ssh')
# 9. head,cat also not working

# TO - READ
# 1. http://pymotw.com/2/subprocess/
# 2. https://docs.python.org/2/library/subprocess.html
