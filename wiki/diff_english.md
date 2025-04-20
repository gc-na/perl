# [Linux] C Shell (csh) diff用法: Compare files line by line

## Overview
The `diff` command is used to compare two files line by line. It identifies differences between the files and displays them in a format that highlights what has been added, removed, or changed.

## Usage
The basic syntax of the `diff` command is as follows:

```csh
diff [options] [file1] [file2]
```

## Common Options
- `-u`: Outputs differences in a unified format, which is easier to read.
- `-c`: Produces a context diff, showing a few lines of context around the changes.
- `-i`: Ignores case differences in the files.
- `-w`: Ignores all white space when comparing lines.
- `-r`: Recursively compares any subdirectories found.

## Common Examples
Here are some practical examples of using the `diff` command:

1. **Basic comparison of two files:**
   ```csh
   diff file1.txt file2.txt
   ```

2. **Unified format comparison:**
   ```csh
   diff -u file1.txt file2.txt
   ```

3. **Context diff with surrounding lines:**
   ```csh
   diff -c file1.txt file2.txt
   ```

4. **Ignoring case differences:**
   ```csh
   diff -i file1.txt file2.txt
   ```

5. **Recursive comparison of two directories:**
   ```csh
   diff -r dir1/ dir2/
   ```

## Tips
- Always use the `-u` option for a more readable output, especially when sharing differences with others.
- When working with large files, consider using `less` to paginate the output: 
  ```csh
  diff file1.txt file2.txt | less
  ```
- If you frequently compare the same files, consider creating a shell script to automate the process.