# [Linux] C Shell (csh) cp Uso: Copy files and directories

## Overview
The `cp` command in C Shell (csh) is used to copy files and directories from one location to another. It allows users to duplicate files or entire directories while maintaining the original files intact.

## Usage
The basic syntax for the `cp` command is as follows:

```csh
cp [options] [source] [destination]
```

## Common Options
- `-i`: Prompts before overwriting an existing file.
- `-r`: Recursively copies directories and their contents.
- `-u`: Copies only when the source file is newer than the destination file or when the destination file is missing.
- `-v`: Verbosely lists files being copied.

## Common Examples
Here are some practical examples of using the `cp` command:

1. **Copy a single file:**
   ```csh
   cp file1.txt file2.txt
   ```
   This command copies `file1.txt` to `file2.txt`.

2. **Copy a directory recursively:**
   ```csh
   cp -r dir1 dir2
   ```
   This command copies the entire directory `dir1` and its contents to `dir2`.

3. **Copy a file with prompt before overwrite:**
   ```csh
   cp -i file1.txt file2.txt
   ```
   This command will ask for confirmation before overwriting `file2.txt` if it already exists.

4. **Copy only newer files:**
   ```csh
   cp -u file1.txt file2.txt
   ```
   This command copies `file1.txt` to `file2.txt` only if `file1.txt` is newer or if `file2.txt` does not exist.

5. **Verbose copy:**
   ```csh
   cp -v file1.txt file2.txt
   ```
   This command will display a message indicating that `file1.txt` is being copied to `file2.txt`.

## Tips
- Always use the `-i` option if you're unsure about overwriting files to avoid accidental data loss.
- When copying directories, remember to use the `-r` option to ensure all contents are copied.
- Use the `-v` option for a clearer understanding of what files are being copied, especially when dealing with multiple files or directories.