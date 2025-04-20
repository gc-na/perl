# [Linux] C Shell (csh) tee用法: Duplicate output to files

## Overview
The `tee` command in C Shell (csh) is used to read from standard input and write to both standard output and one or more files simultaneously. This is particularly useful when you want to view the output of a command while also saving it for later use.

## Usage
The basic syntax of the `tee` command is as follows:

```csh
tee [options] [arguments]
```

## Common Options
- `-a`: Append the output to the specified files instead of overwriting them.
- `-i`: Ignore the interrupt signals.

## Common Examples

1. **Basic Usage**: Display output and save it to a file.
   ```csh
   echo "Hello, World!" | tee output.txt
   ```

2. **Appending Output**: Append output to an existing file.
   ```csh
   echo "Another line" | tee -a output.txt
   ```

3. **Multiple Files**: Write output to multiple files.
   ```csh
   echo "Logging data" | tee file1.txt file2.txt
   ```

4. **Using with Other Commands**: Capture the output of a command while displaying it.
   ```csh
   ls -l | tee directory_listing.txt
   ```

## Tips
- Use the `-a` option when you want to keep previous data in a file and add new data to it.
- Combine `tee` with other commands in a pipeline to monitor and save output simultaneously.
- Remember that `tee` will overwrite files by default, so use the `-a` option if you want to append data.