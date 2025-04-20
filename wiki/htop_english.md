# [Linux] C Shell (csh) htop用法: 交互式进程查看器

## Overview
The `htop` command is an interactive process viewer for Unix systems. It provides a real-time, visual representation of system processes, allowing users to monitor system performance and manage processes more effectively than with traditional tools like `top`.

## Usage
The basic syntax for the `htop` command is as follows:

```bash
htop [options] [arguments]
```

## Common Options
- `-h`, `--help`: Display help information about `htop`.
- `-s`, `--sort`: Specify the sorting order of processes (e.g., by CPU usage, memory usage).
- `-p`, `--pid`: Show only the processes with the specified process IDs.
- `-u`, `--user`: Display processes for a specific user.

## Common Examples
- To start `htop` and view all processes:
  ```bash
  htop
  ```

- To sort processes by memory usage:
  ```bash
  htop -s MEM
  ```

- To display processes for a specific user:
  ```bash
  htop -u username
  ```

- To view only specific processes by their IDs:
  ```bash
  htop -p 1234,5678
  ```

## Tips
- Use the function keys (F1 to F10) for quick access to various features, such as searching for processes or killing processes.
- You can customize the display by pressing `F2` to access the setup menu.
- To quit `htop`, simply press `F10` or `q`.