# [Linux] C Shell (csh) fdisk用法: Manage disk partitions

## Overview
The `fdisk` command is a powerful utility used to manage disk partitions on a system. It allows users to create, delete, resize, and modify partitions on hard drives and other storage devices.

## Usage
The basic syntax of the `fdisk` command is as follows:

```bash
fdisk [options] [arguments]
```

## Common Options
- `-l`: Lists all available disk partitions.
- `-u`: Uses sectors instead of cylinders for displaying partition sizes.
- `-n`: Creates a new partition.
- `-d`: Deletes a partition.
- `-p`: Prints the partition table.

## Common Examples
1. **List all partitions on a disk:**
   ```bash
   fdisk -l
   ```

2. **Create a new partition:**
   ```bash
   fdisk /dev/sda
   ```
   After running this command, follow the interactive prompts to create a new partition.

3. **Delete a partition:**
   ```bash
   fdisk /dev/sda
   ```
   Similar to creating a partition, you'll need to follow the prompts to delete a specific partition.

4. **Print the partition table:**
   ```bash
   fdisk -p /dev/sda
   ```

## Tips
- Always back up your data before modifying partitions to prevent data loss.
- Use the `-u` option if you prefer to work with sectors for more precise partitioning.
- Be cautious when deleting partitions; ensure you are targeting the correct one to avoid accidental data loss.