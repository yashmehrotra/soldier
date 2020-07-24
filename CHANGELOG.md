## v0.2.4
- Bugfix: Call `Popen.communicate` when `stream=True` to set `exit_code` explicitly in case process is still in running state

## v0.2.3
- Bugfix: `exit_code` was not being set when using `stream=True`. This was fixed by calling `Popen.poll()`

## v0.2.2
- `exit_code` is now a property, `status_code` is still supported but will be deprecated
- `suppress_std_err` keyworded argument is added to prevent from always printing stderr

## v0.2.1
- Custom enviroment variables can be passed to commands

## v0.2.0
- Support for cwd when executing commands
- Supoort for streaming of output to stdout

## v0.1.0
Initial Relase
