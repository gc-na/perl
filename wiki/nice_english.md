# [Linux] C Shell (csh) nice用法: 控制进程优先级

## Overview
The `nice` command in C Shell (csh) is used to run a command with a modified scheduling priority. It allows users to influence the priority of processes, making it possible to give more or less CPU time to specific tasks. By default, processes run with a priority of 0, but `nice` can adjust this value.

## Usage
The basic syntax of the `nice` command is as follows:

```csh
nice [options] [command [arguments]]
```

## Common Options
- `-n` or `--adjustment`: Specifies the priority adjustment value. The default is 10. Negative values can be used to increase priority.
- `-h` or `--help`: Displays help information about the command.
- `-v` or `--version`: Shows the version information of the `nice` command.

## Common Examples
Here are some practical examples of using the `nice` command:

1. **Run a command with default nice value (10)**:
   ```csh
   nice myscript.sh
   ```

2. **Run a command with a specific nice value (e.g., 15)**:
   ```csh
   nice -n 15 myscript.sh
   ```

3. **Run a command with increased priority (e.g., -5)**:
   ```csh
   nice -n -5 myscript.sh
   ```

4. **Check the nice value of a running process** (using `ps`):
   ```csh
   ps -o pid,nice,cmd
   ```

## Tips
- Use `nice` to run background tasks without hogging CPU resources, allowing other processes to run smoothly.
- Be cautious when using negative nice values, as they can affect system performance by prioritizing certain processes over others.
- Always check the current nice value of a process if you are unsure about its priority, using the `ps` command.