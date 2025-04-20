# [Linux] C Shell (csh) parted用法: Manage disk partitions

## Overview
The `parted` command is a powerful tool used for managing disk partitions in Linux. It allows users to create, delete, resize, and manipulate disk partitions, making it essential for system administration and disk management tasks.

## Usage
The basic syntax of the `parted` command is as follows:

```shell
parted [options] [arguments]
```

## Common Options
- `-l`, `--list`: List all available partitions on all devices.
- `-s`, `--script`: Run in script mode, suppressing all interactive prompts.
- `mkpart`: Create a new partition.
- `rm`: Remove a partition.
- `resizepart`: Resize an existing partition.
- `print`: Display the partition table of the specified device.

## Common Examples
Here are some practical examples of using the `parted` command:

1. **List all partitions on a device:**
   ```shell
   parted -l
   ```

2. **Create a new partition:**
   ```shell
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Remove a partition:**
   ```shell
   parted /dev/sda rm 1
   ```

4. **Resize an existing partition:**
   ```shell
   parted /dev/sda resizepart 1 200MiB
   ```

5. **Display the partition table of a specific device:**
   ```shell
   parted /dev/sda print
   ```

## Tips
- Always back up important data before modifying partitions.
- Use the `--script` option when running commands in scripts to avoid interactive prompts.
- Be cautious when resizing partitions, as it can lead to data loss if not done correctly.