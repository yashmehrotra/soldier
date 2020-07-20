Usage
=====

**Philosophy**: The reason for creating soldier is to provide a user-friendly and pythonic API on top the subprocess module in order to manage system processes in python.

After successfully installing soldier, you will now be able to communicate with system processes without making your eyes bleed.

**Get output of pwd command**

.. code-block:: python

    >> import soldier
    >> current_path = soldier.run('pwd')
    >> print(current_path.output)
    /home/pythonista
    # Status Code
    >> print(current_path.exit_code)
    0

**Run a process in background, and later terminate it**

.. code-block:: python

    >> firefox_proc = soldier.run('firefox', background=True)
    # Get pid of firefox process
    >> print(firefox_proc.pid)
    18673
    # Kill firefox
    >> firefox_proc.kill()
    >> firefox_proc.is_alive()
    >> False

**Run a root command**

.. code-block:: python

    >> soldier.run('service nginx start', sudo='my_password')

**Run a command with timeout**

.. code-block:: python

    >> soldier.run('./infinite_loop_script.py', timeout=10, kill_on_timeout=True)

    # Handle timeouts
    >> try
           soldier.run('./my_script.py', timeout=5, kill_on_timeout=False)
       except soldier.ProcessTimeoutError:
           print("Your script timed out")
    Your script timed out
