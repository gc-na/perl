# [Linux] C Shell (csh) w: Display logged-in users and their activity

## Overview
The `w` command in C Shell (csh) is used to display information about users currently logged into the system, along with their activities. It provides details such as the username, terminal, login time, idle time, and the command being executed.

## Usage
The basic syntax of the `w` command is as follows:

```
w [options] [arguments]
```

## Common Options
- `-h`: Suppresses the header line in the output.
- `-s`: Displays the output in a short format, omitting the idle time and JCPU.
- `-f`: Shows the full login name and the host name of the users.

## Common Examples
Here are some practical examples of using the `w` command:

1. **Basic Usage**
   ```csh
   w
   ```
   This command displays a list of all users currently logged in, along with their activity.

2. **Suppressing the Header**
   ```csh
   w -h
   ```
   This command shows the same information as the basic usage but without the header line.

3. **Short Format Output**
   ```csh
   w -s
   ```
   This command provides a concise view of logged-in users without idle time and JCPU information.

4. **Full User Information**
   ```csh
   w -f
   ```
   This command displays the full login names and host names of the users, providing more context about who is logged in.

## Tips
- Use `w` regularly to monitor user activity on a multi-user system.
- Combine `w` with other commands like `grep` to filter results for specific users.
- Familiarize yourself with the output format to quickly interpret user activity and system load.