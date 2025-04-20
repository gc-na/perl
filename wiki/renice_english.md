# [Linux] C Shell (csh) renice用法: Adjust process priority

## Overview
The `renice` command in C Shell (csh) is used to change the priority of running processes. By adjusting a process's priority, you can influence how much CPU time it receives compared to other processes. A lower nice value means higher priority, while a higher nice value means lower priority.

## Usage
The basic syntax for the `renice` command is as follows:

```csh
renice [options] [arguments]
```

## Common Options
- `-n`: Specify the new nice value. This is required to change the priority.
- `-p`: Change the priority of a process by its process ID (PID).
- `-g`: Change the priority of all processes in a specified group.
- `-u`: Change the priority of all processes owned by a specified user.

## Common Examples
Here are some practical examples of how to use the `renice` command:

1. **Change the priority of a specific process by PID:**

   ```csh
   renice -n 10 -p 1234
   ```

   This command sets the nice value of the process with PID 1234 to 10.

2. **Change the priority of all processes owned by a specific user:**

   ```csh
   renice -n -5 -u username
   ```

   This command lowers the nice value of all processes owned by "username" to -5, giving them higher priority.

3. **Change the priority of a process group:**

   ```csh
   renice -n 15 -g 5678
   ```

   This command sets the nice value of all processes in the group with GID 5678 to 15.

4. **Check the current nice value of a process:**

   ```csh
   ps -o pid,nice,cmd -p 1234
   ```

   While not part of `renice`, this command helps you check the current nice value of the process with PID 1234 before making changes.

## Tips
- Always check the current nice value of a process before changing it to avoid unintended consequences.
- Use negative nice values cautiously, as they can significantly affect system performance by prioritizing certain processes over others.
- Remember that only the superuser (root) can set a negative nice value; regular users can only increase the nice value (lower priority).