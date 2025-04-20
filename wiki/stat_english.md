# [Linux] C Shell (csh) stat用法: Retrieve file or filesystem status

## Overview
The `stat` command in C Shell (csh) is used to display detailed information about files or file systems. It provides insights into file attributes such as size, permissions, modification times, and more.

## Usage
The basic syntax of the `stat` command is as follows:

```csh
stat [options] [arguments]
```

## Common Options
- `-c, --format=FORMAT`: Specify the output format using a format string.
- `-f, --file-system`: Display information about the file system instead of the file.
- `-L, --dereference`: Follow symbolic links to display information about the target file.
- `--help`: Display help information about the command.
- `--version`: Show the version information of the `stat` command.

## Common Examples
Here are some practical examples of using the `stat` command:

1. **Display file status:**
   ```csh
   stat filename.txt
   ```

2. **Display file system status:**
   ```csh
   stat -f /
   ```

3. **Format output to show only file size and modification time:**
   ```csh
   stat -c '%s %y' filename.txt
   ```

4. **Follow symbolic links:**
   ```csh
   stat -L symlink
   ```

5. **Show version information:**
   ```csh
   stat --version
   ```

## Tips
- Use the `-c` option to customize the output format for better readability.
- When working with symbolic links, remember to use the `-L` option to get information about the target file.
- Combine `stat` with other commands like `grep` to filter specific information from the output.