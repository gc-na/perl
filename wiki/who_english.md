# [Linux] C Shell (csh) who uso: Display logged-in users

## Overview
The `who` command in C Shell (csh) is used to display a list of users who are currently logged into the system. It provides information such as the username, terminal, login time, and more, which can be useful for system monitoring and management.

## Usage
The basic syntax of the `who` command is as follows:

```
who [options] [arguments]
```

## Common Options
- `-a`: Displays all available information, including users' idle times and the current run level.
- `-b`: Shows the last system boot time.
- `-q`: Displays only the usernames and the number of users logged in.
- `-H`: Includes a header in the output, showing the column names.

## Common Examples
Here are some practical examples of using the `who` command:

1. **Basic usage**: Display all logged-in users.
   ```csh
   who
   ```

2. **Show detailed information**: Display all available information about logged-in users.
   ```csh
   who -a
   ```

3. **Last boot time**: Show the last time the system was booted.
   ```csh
   who -b
   ```

4. **Count of logged-in users**: Display only the usernames and the count of users logged in.
   ```csh
   who -q
   ```

5. **Include headers**: Display logged-in users with column headers.
   ```csh
   who -H
   ```

## Tips
- Use `who -a` for a comprehensive view of user sessions, especially when troubleshooting user-related issues.
- Combine `who` with other commands like `grep` to filter results for specific users.
- Regularly check logged-in users to monitor system activity and ensure security.