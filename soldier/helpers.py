import os
import signal


def kill_family(pid):
    """
    Kills the children and the parents
    """
    os.kill(pid, signal.SIGTERM)


def pid_exists(pid):
    """
    Check whether pid exists in the current process table
    """

    if pid == 0:
        return True
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True
