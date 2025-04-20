# [Linux] C Shell (csh) killall用法: Terminate processes by name

## Overview
The `killall` command in C Shell (csh) is used to terminate all processes that match a specified name. This command is particularly useful for managing multiple instances of a program without needing to find and kill each process individually.

## Usage
The basic syntax of the `killall` command is as follows:

```csh
killall [options] [arguments]
```

## Common Options
- `-u <user>`: Only kill processes owned by the specified user.
- `-s <signal>`: Specify the signal to send to the processes (e.g., `-s TERM` to send the terminate signal).
- `-q`: Suppress error messages for processes that do not exist.
- `-I`: Ignore case when matching process names.

## Common Examples
Here are some practical examples of using the `killall` command:

1. **Terminate all instances of a program:**
   ```csh
   killall firefox
   ```
   This command will kill all running instances of Firefox.

2. **Send a specific signal to a process:**
   ```csh
   killall -s TERM myapp
   ```
   This sends the terminate signal to all instances of `myapp`.

3. **Kill processes owned by a specific user:**
   ```csh
   killall -u username
   ```
   This will terminate all processes owned by `username`.

4. **Suppress error messages:**
   ```csh
   killall -q myapp
   ```
   This will attempt to kill `myapp` without displaying errors if it is not running.

5. **Ignore case when killing processes:**
   ```csh
   killall -I myapp
   ```
   This will kill all processes matching `myapp`, regardless of case.

## Tips
- Always double-check the process name you are targeting to avoid accidentally terminating the wrong processes.
- Use the `-q` option if you want to avoid cluttering your terminal with error messages when a process is not found.
- Consider using `ps` or `pgrep` to list processes before using `killall` to ensure you are terminating the correct ones.