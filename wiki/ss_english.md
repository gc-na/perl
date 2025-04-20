# [Linux] C Shell (csh) ss用法: 查看套接字统计信息

## Overview
The `ss` command is used to investigate sockets on a Linux system. It provides detailed information about network connections, including TCP, UDP, and UNIX sockets, making it a powerful tool for network diagnostics and monitoring.

## Usage
The basic syntax of the `ss` command is as follows:

```bash
ss [options] [arguments]
```

## Common Options
- `-t`: Display TCP sockets.
- `-u`: Display UDP sockets.
- `-l`: Show listening sockets.
- `-p`: Show the process using the socket.
- `-n`: Show numerical addresses instead of resolving hostnames.
- `-a`: Display all sockets (listening and non-listening).

## Common Examples
Here are several practical examples of using the `ss` command:

1. **Display all TCP sockets:**
   ```bash
   ss -t
   ```

2. **Show all listening sockets:**
   ```bash
   ss -l
   ```

3. **Display all UDP sockets:**
   ```bash
   ss -u
   ```

4. **Show all sockets with process information:**
   ```bash
   ss -p
   ```

5. **Display all sockets with numerical addresses:**
   ```bash
   ss -n
   ```

6. **Show both listening and non-listening sockets:**
   ```bash
   ss -a
   ```

## Tips
- Use the `-n` option to speed up the output by avoiding DNS resolution, especially on systems with many connections.
- Combine options for more specific queries, such as `ss -tunlp` to show TCP and UDP sockets with process information.
- Regularly check socket statistics to monitor for unusual activity or potential security issues.