# [Linux] C Shell (csh) lsblk Uso equivalente: Listar dispositivos de bloques

## Overview
The `lsblk` command is used to list information about block devices in a Linux system. It provides a tree-like view of all available storage devices, including their partitions and mount points, which is essential for managing disks and filesystems.

## Usage
The basic syntax of the `lsblk` command is as follows:

```bash
lsblk [options] [arguments]
```

## Common Options
- `-a`, `--all`: Show all devices, including empty ones.
- `-f`, `--fs`: Display filesystem information such as type and label.
- `-l`, `--list`: Use a list format instead of the tree format.
- `-o`, `--output`: Specify which columns to display (e.g., NAME, SIZE, TYPE).
- `-p`, `--paths`: Show device paths instead of device names.

## Common Examples
Here are some practical examples of using the `lsblk` command:

1. **Basic usage**: List all block devices.
   ```bash
   lsblk
   ```

2. **Show all devices, including empty ones**:
   ```bash
   lsblk -a
   ```

3. **Display filesystem information**:
   ```bash
   lsblk -f
   ```

4. **List devices in a flat format**:
   ```bash
   lsblk -l
   ```

5. **Specify output columns**:
   ```bash
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

## Tips
- Use the `-f` option to quickly check the filesystem type and label, which can help in identifying devices.
- Combine `lsblk` with other commands like `grep` to filter specific devices or mount points.
- Regularly check your block devices to monitor disk usage and ensure that partitions are mounted correctly.