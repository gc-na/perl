# [Linux] C Shell (csh) users equivalente: Display user information

## Overview
The `users` command in C Shell (csh) is used to display the usernames of users currently logged into the system. It provides a simple way to see who is active on the machine.

## Usage
The basic syntax of the `users` command is as follows:

```
users [options] [arguments]
```

## Common Options
- `-n`: Suppresses the output of the usernames, typically used in scripts where user information is not needed.
- `-r`: Displays the number of users currently logged in instead of their usernames.

## Common Examples

1. **Display currently logged-in users:**

   ```csh
   users
   ```

   This command will output a list of usernames currently logged into the system.

2. **Count the number of logged-in users:**

   ```csh
   users -r
   ```

   This will show the total count of users currently logged in.

3. **Suppress output of usernames:**

   ```csh
   users -n
   ```

   This command will execute without displaying any usernames, useful for scripting.

## Tips
- Use the `users` command in combination with other commands like `who` or `w` for more detailed information about logged-in users.
- If you are writing scripts, consider using the `-n` option to avoid cluttering output with usernames when they are not needed.
- Regularly check logged-in users to monitor system activity, especially on shared environments.