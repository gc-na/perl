# [Linux] C Shell (csh) jobs 用法等价: Manage Background and Stopped Jobs

## Overview
The `jobs` command in C Shell (csh) is used to display the status of jobs that are running in the background or have been stopped. It provides information about each job, including its job number, status, and command line.

## Usage
The basic syntax of the `jobs` command is as follows:

```csh
jobs [options] [arguments]
```

## Common Options
- `-l`: Displays the process IDs (PIDs) along with the job status.
- `-n`: Shows only jobs that have changed status since the last time the command was run.
- `-p`: Displays only the process IDs of the jobs.

## Common Examples

1. **Display all jobs:**
   ```csh
   jobs
   ```

2. **Display jobs with process IDs:**
   ```csh
   jobs -l
   ```

3. **Show only jobs that have changed status:**
   ```csh
   jobs -n
   ```

4. **Display only process IDs of jobs:**
   ```csh
   jobs -p
   ```

5. **Check the status of jobs after running a background command:**
   ```csh
   sleep 60 &
   jobs
   ```

## Tips
- Use `jobs` frequently to monitor your background tasks and ensure they are running as expected.
- Combine `jobs` with other commands like `fg` or `bg` to manage jobs more effectively.
- Remember that jobs will be listed only if they were started in the current shell session.