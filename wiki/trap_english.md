# [Linux] C Shell (csh) trap用法: 处理信号和清理

## Overview
The `trap` command in C Shell (csh) is used to specify commands that will be executed when the shell receives certain signals. This is particularly useful for cleaning up temporary files or performing specific actions before a script exits or is interrupted.

## Usage
The basic syntax of the `trap` command is as follows:

```csh
trap [commands] [signals]
```

## Common Options
- `commands`: The commands to execute when the specified signals are received.
- `signals`: The signals that will trigger the execution of the commands. Common signals include:
  - `INT`: Interrupt signal (usually from Ctrl+C).
  - `TERM`: Termination signal.
  - `QUIT`: Quit signal (usually from Ctrl+\).

## Common Examples

### Example 1: Cleanup on Interrupt
This example shows how to clean up temporary files when the script is interrupted.

```csh
#!/bin/csh
trap 'rm -f /tmp/mytempfile' INT
echo "Running script. Press Ctrl+C to interrupt."
sleep 60
```

### Example 2: Custom Exit Message
In this example, a custom message is displayed when the script is terminated.

```csh
#!/bin/csh
trap 'echo "Script terminated. Goodbye!"' TERM
echo "Running script. Send a TERM signal to see the message."
sleep 60
```

### Example 3: Multiple Signals
You can specify multiple signals to trigger the same command.

```csh
#!/bin/csh
trap 'echo "Received signal, exiting!"' INT TERM
echo "Running script. Press Ctrl+C or send TERM signal."
sleep 60
```

## Tips
- Always ensure that the commands specified in `trap` are simple and quick to execute to avoid delays in signal handling.
- Use `trap` at the beginning of your scripts to set up signal handling before any long-running processes.
- Remember to test your scripts to ensure that the `trap` commands behave as expected under different signal conditions.