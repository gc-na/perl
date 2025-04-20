# [Linux] C Shell (csh) dmesg 使用法: Display kernel messages

## Overview
The `dmesg` command is used to print or control the kernel ring buffer, which contains messages related to the system's hardware and kernel events. It is particularly useful for diagnosing hardware issues or monitoring system boot messages.

## Usage
The basic syntax of the `dmesg` command is as follows:

```bash
dmesg [options] [arguments]
```

## Common Options
- `-C`: Clear the ring buffer.
- `-c`: Clear the ring buffer after printing its contents.
- `-n level`: Set the level of messages to be printed. Levels range from 0 (emergencies) to 7 (debugging).
- `-s size`: Set the size of the buffer to be printed in bytes.
- `-T`: Print human-readable timestamps.

## Common Examples
Here are some practical examples of using the `dmesg` command:

1. **View the entire kernel message buffer:**
   ```bash
   dmesg
   ```

2. **Clear the kernel message buffer:**
   ```bash
   dmesg -C
   ```

3. **View kernel messages with human-readable timestamps:**
   ```bash
   dmesg -T
   ```

4. **Print messages of a specific severity level (e.g., only warnings and errors):**
   ```bash
   dmesg -n 3
   ```

5. **View the last 100 bytes of the kernel message buffer:**
   ```bash
   dmesg -s 100
   ```

## Tips
- Use `dmesg | less` to scroll through the output if it is too long to fit on one screen.
- Combine `dmesg` with `grep` to filter messages for specific keywords, such as:
  ```bash
  dmesg | grep error
  ```
- Regularly check `dmesg` after booting to diagnose any hardware issues that may have occurred during startup.