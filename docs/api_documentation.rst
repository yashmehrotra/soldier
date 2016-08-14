API Documentation
=================

.. function:: soldier.run(command, **kwargs)

    The main run command which executes the system process

    :param background: Set this true if you want to run the command asynchronously (default: False)
    :type background: bool
    :param std_in: The standard input to be given to the process
    :type std_in: string
    :param sudo: If you want to execute the command as root, this argument should be your password
    :type sudo: string
    :param timeout: The timeout for the process in seconds
    :type timeout: int
    :param kill_on_timeout:
    :type kill_on_timeout: bool
    :param shell: Set this to true if you
    :type shell: bool
    :rtype: A *soldier.Soldier* object



.. class:: soldier.Soldier

    The class object which is returned with the *soldier.run()* method.

    **Methods**

    .. function:: kill()

        This function is used to kill the current process

        :rtype: *None*


    .. function:: is_alive()

        This function checks whether process is active or not

        :rtype: *boolean*


    **Properties**

    - pid - Returns the pid of the process
    - status_code - Returns the status code of the process
    - output - Returns the stdout (standard output) of the process
    - error - Returns the stderr (standard error) of the process
    - start_ts - Returns the start time (:class:`datetime.datetime` object) of the process
    - end_ts - Returns the end time (:class:`datetime.datetime` object) of the process
    - duration - Returns the total duration(:class:`datetime.timedelta` object) of the process
 
