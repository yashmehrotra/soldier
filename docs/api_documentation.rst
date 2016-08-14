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
    :param timeout:
    :type timeout: int
    :param kill_on_timeout:
    :type kill_on_timeout: bool
    :param shell: Set this to true if you
    :type shell: bool
    :rtype: A *soldier.Soldier* object



.. class:: soldier.Soldier

    The class object which is returned with the *soldier.run()* method.
    :param std_in: The standard input to be given to the process
    :type std_in: string
 
