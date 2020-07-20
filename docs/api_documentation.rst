API Documentation
=================

.. function:: soldier.run(command, background=False, std_id='', sudo=None, timeout=0, kill_on_timeout=False, shell=False)

    The main run command which executes the system process

    :param background: Set this true if you want to run the command asynchronously
    :type background: bool
    :param std_in: The standard input to be given to the process
    :type std_in: string
    :param sudo: If you want to execute the command as root, this argument should be your password
    :type sudo: string
    :param cwd: Working directory of the command being executed
    :type cwd: string
    :param env: Environment variables that would be available when the command is being executed
    :type env: dict(str, str)
    :param stream: When set to true, the output of your command will be streamed. (It does not work with piped commands)
    :type stream: bool
    :param timeout: The timeout for the process in seconds
    :type timeout: int
    :param kill_on_timeout: If set to true, your process will killed when the time is up, and if it is False, it will throw a ``soldier.ProcessTimeoutError``
    :type kill_on_timeout: bool
    :param shell: Set this to true if you want to execute the process in the /bin/sh environment
    :type shell: bool
    :returns: A :class:`soldier.Soldier` object
    :rtype: :class:`soldier.Soldier`

.. warning::

    Passing ``shell=True`` can be a security hazard if combined with untrusted input.


.. class:: soldier.Soldier

    The class object which is returned with the :func:`soldier.run()` method.

    **Methods**

    .. function:: kill()

        This function is used to kill the current process

        :rtype: ``None``


    .. function:: is_alive()

        This function checks whether process is active or not

        :returns: A ``bool`` specifying whether the process is running or not
        :rtype: ``bool``


    **Properties**

    - pid - Returns the pid of the process
    - status_code - Returns the status code of the process
    - output - Returns the stdout (standard output) of the process
    - error - Returns the stderr (standard error) of the process
    - start_ts - Returns the start time (:class:`datetime.datetime` object) of the process
    - end_ts - Returns the end time (:class:`datetime.datetime` object) of the process
    - duration - Returns the total duration(:class:`datetime.timedelta` object) of the process
 
