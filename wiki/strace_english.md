# [Linux] C Shell (csh) strace用法: Trace system calls and signals

## Overview
The `strace` command is a powerful diagnostic tool used to monitor the interactions between a program and the Linux kernel. It allows users to trace system calls and signals received by a process, making it invaluable for debugging and performance analysis.

## Usage
The basic syntax of the `strace` command is as follows:

```bash
strace [options] [arguments]
```

## Common Options
- `-c`: Count time, calls, and errors for each system call and report summary statistics.
- `-f`: Follow forks, tracing child processes as they are created.
- `-p <pid>`: Attach to the process with the specified process ID (PID) and trace its system calls.
- `-o <file>`: Write the trace output to the specified file instead of standard error.
- `-e <expr>`: Filter the system calls to trace based on the provided expression.

## Common Examples
Here are some practical examples of using `strace`:

1. **Trace a command execution:**
   ```bash
   strace ls
   ```
   This command will trace all system calls made by the `ls` command.

2. **Trace a running process:**
   ```bash
   strace -p 1234
   ```
   Replace `1234` with the actual PID of the process you want to trace.

3. **Count system calls:**
   ```bash
   strace -c ls
   ```
   This will execute `ls` and provide a summary of the system calls made, including counts and time spent.

4. **Output to a file:**
   ```bash
   strace -o output.txt ls
   ```
   This will save the trace output of the `ls` command to `output.txt`.

5. **Filter specific system calls:**
   ```bash
   strace -e trace=open,close ls
   ```
   This will only trace the `open` and `close` system calls made by the `ls` command.

## Tips
- Use `strace` with `-f` when dealing with programs that create child processes to ensure you capture all relevant system calls.
- Redirect output to a file with `-o` for easier analysis, especially for long-running processes.
- Combine `strace` with other tools like `grep` to filter specific output, making it easier to find relevant information in the trace logs.