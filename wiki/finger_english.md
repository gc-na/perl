# [Unix] C Shell (csh) finger Usage: Display user information

## Overview
The `finger` command is used to display information about users on a system. It provides details such as login name, real name, terminal, idle time, and more. This command is particularly useful for system administrators and users who want to see who is logged in and gather information about them.

## Usage
The basic syntax of the `finger` command is as follows:

```csh
finger [options] [arguments]
```

## Common Options
- `-l`: Displays a longer format of user information, including the user's home directory and shell.
- `-m`: Matches the user name case-insensitively.
- `-s`: Displays a short format, showing only the login name and the user's real name.
- `-p`: Suppresses the display of the user's plan file and project information.

## Common Examples
Here are some practical examples of how to use the `finger` command:

1. **Display information about all users:**
   ```csh
   finger
   ```

2. **Display detailed information about a specific user:**
   ```csh
   finger username
   ```

3. **Show a short format of user information:**
   ```csh
   finger -s
   ```

4. **Display information about a user without showing their plan file:**
   ```csh
   finger -p username
   ```

5. **Case-insensitive search for a user:**
   ```csh
   finger -m USERNAME
   ```

## Tips
- Use `finger` to quickly check who is logged into the system and their status.
- Combine options for more specific queries, such as `finger -ls username` for detailed information in a short format.
- Remember that the availability of the `finger` command may depend on your system configuration and user permissions.