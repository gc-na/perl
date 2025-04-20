# [Linux] C Shell (csh) cmp Usage: Compare two files byte by byte

## Overview
The `cmp` command in C Shell (csh) is used to compare two files byte by byte. It identifies the first byte where the files differ and can also report whether the files are identical or not.

## Usage
The basic syntax of the `cmp` command is as follows:

```
cmp [options] [file1] [file2]
```

## Common Options
- `-l`: Outputs the byte numbers and values of differing bytes in octal.
- `-s`: Suppresses all output; only the exit status is returned.
- `-i`: Ignores the first `n` bytes of each file.
- `-n`: Compares only the first `n` bytes of the files.

## Common Examples
Here are some practical examples of using the `cmp` command:

1. **Basic comparison of two files:**
   ```csh
   cmp file1.txt file2.txt
   ```

2. **Suppress output and only check if files are different:**
   ```csh
   cmp -s file1.txt file2.txt
   ```

3. **Compare the first 10 bytes of two files:**
   ```csh
   cmp -n 10 file1.txt file2.txt
   ```

4. **List differing bytes in octal format:**
   ```csh
   cmp -l file1.txt file2.txt
   ```

5. **Ignore the first 5 bytes of each file during comparison:**
   ```csh
   cmp -i 5 file1.txt file2.txt
   ```

## Tips
- Use the `-s` option when you only need to know if the files differ without cluttering the output.
- The exit status of `cmp` can be useful in scripts: `0` means files are identical, `1` means they differ, and `2` indicates an error.
- When comparing large files, consider using `-n` to limit the number of bytes compared for quicker results.