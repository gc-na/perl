# [Linux] C Shell (csh) journalctl用法: View system logs

## Overview
The `journalctl` command is used to query and display messages from the journal, which is a component of the systemd system and service manager. It allows users to view logs from various sources, including the kernel, system services, and user applications.

## Usage
The basic syntax of the `journalctl` command is as follows:

```bash
journalctl [options] [arguments]
```

## Common Options
- `-b`: Show logs from the current boot.
- `-f`: Follow the log output in real-time.
- `--since`: Show logs since a specified time.
- `--until`: Show logs until a specified time.
- `-u <unit>`: Show logs for a specific systemd unit (service).
- `-p <priority>`: Show logs with a specific priority level (e.g., `err`, `warning`, `info`).

## Common Examples
Here are some practical examples of using `journalctl`:

1. **View all logs:**
   ```bash
   journalctl
   ```

2. **View logs from the current boot:**
   ```bash
   journalctl -b
   ```

3. **Follow logs in real-time:**
   ```bash
   journalctl -f
   ```

4. **View logs since a specific date:**
   ```bash
   journalctl --since "2023-10-01"
   ```

5. **View logs for a specific service:**
   ```bash
   journalctl -u ssh.service
   ```

6. **View error logs:**
   ```bash
   journalctl -p err
   ```

## Tips
- Use the `-f` option to monitor logs in real-time, which is particularly useful for troubleshooting.
- Combine `--since` and `--until` options to narrow down logs to a specific time frame.
- Use `grep` in conjunction with `journalctl` to filter logs for specific keywords:
  ```bash
  journalctl | grep "error"
  ```