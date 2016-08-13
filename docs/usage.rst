How to use
==========

Philosophy: The reason for creating soldier was mainly to provide a user-friendly and pythonic API to the subprocess module.

After successfully installing soldier, you will now be able to communicate with system processes without making your eyes bleed.

.. code-block:: python

    >> import soldier

    # Get output of pwd command
    >> current_path = soldier.run('pwd')
    >> print(current_path.output)
    /home/pythonista
    # Status Code
    >> print(current_path.status_code)
    0

    # Run a process in background
    >> firefox_proc = soldier.run('firefox', background=True)
    # Get pid of firefox process
    >> print(firefox_proc.pid)
    18673
    # Kill firefox
    >> firefox_proc.kill()
    >> firefox_proc.is_alive()
    >> False

    # Run a root command
    >> soldier.run('service nginx start', sudo='my_password')

    # Run a command with timeout
    >> soldier.run('./infinite_loop_script.py', timeout=10, kill_on_timeout=True)

    # Handle timeouts
    >> try
           soldier.run('./my_script.py', timeout=5, kill_on_timeout=False)
       except soldier.TimeoutError:
           print("Your script timed out")
    Your script timed out
