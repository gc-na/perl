# [Unix] C Shell (csh) at: Schedule Commands for Later Execution

## Overview
The `at` command in C Shell (csh) is used to schedule commands to be executed at a specified time in the future. This is particularly useful for automating tasks that need to run once at a specific time, rather than on a recurring basis.

## Usage
The basic syntax of the `at` command is as follows:

```csh
at [options] [time]
```

## Common Options
- `-f <file>`: Read commands from the specified file instead of standard input.
- `-m`: Send mail to the user when the job is completed, even if there was no output.
- `-q <queue>`: Specify the queue to which the job should be added (e.g., a, b, c).
- `-l`: List the jobs scheduled for the user.

## Common Examples
Here are some practical examples of using the `at` command:

1. **Schedule a command for a specific time:**
   To run a command at 3 PM today:
   ```csh
   echo "echo 'Hello, World!'" | at 15:00
   ```

2. **Schedule a command for tomorrow at noon:**
   ```csh
   echo "backup.sh" | at noon tomorrow
   ```

3. **Read commands from a file:**
   If you have a script named `my_script.sh` that you want to run at 5 PM:
   ```csh
   at -f my_script.sh 17:00
   ```

4. **List scheduled jobs:**
   To see all jobs you have scheduled:
   ```csh
   at -l
   ```

5. **Send mail upon job completion:**
   Schedule a job and ensure you receive an email when it's done:
   ```csh
   echo "cleanup.sh" | at -m 22:00
   ```

## Tips
- Always check the scheduled jobs with `at -l` to avoid confusion about what is set to run.
- Use the `-m` option if you want to be notified of job completion, especially for long-running tasks.
- To remove a scheduled job, you can use the `atrm` command followed by the job number listed by `at -l`.