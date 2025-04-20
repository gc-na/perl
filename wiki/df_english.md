# [Linux] C Shell (csh) df Uso equivalente: Display disk space usage

## Overview
The `df` command in C Shell (csh) is used to display the amount of disk space used and available on file systems. It provides a summary of the total space, used space, available space, and the mount points of each file system.

## Usage
The basic syntax of the `df` command is as follows:

```csh
df [options] [arguments]
```

## Common Options
- `-h`: Displays the disk space in a human-readable format (e.g., KB, MB, GB).
- `-T`: Shows the file system type along with the disk space information.
- `-i`: Displays inode information instead of block usage.
- `-a`: Includes dummy file systems in the output.
- `-t <type>`: Shows only file systems of the specified type.

## Common Examples
Here are some practical examples of using the `df` command:

1. **Basic Usage**: Display disk space for all mounted file systems.
   ```csh
   df
   ```

2. **Human-Readable Format**: Display disk space in a more understandable format.
   ```csh
   df -h
   ```

3. **Include File System Type**: Show file system types along with disk usage.
   ```csh
   df -T
   ```

4. **Inode Information**: Display inode usage instead of block usage.
   ```csh
   df -i
   ```

5. **Filter by File System Type**: Show only ext4 file systems.
   ```csh
   df -t ext4
   ```

## Tips
- Use the `-h` option for easier readability, especially when dealing with large disk sizes.
- Regularly check disk usage to avoid running out of space, which can affect system performance.
- Combine options for more detailed output, such as `df -hT` to see both human-readable sizes and file system types.