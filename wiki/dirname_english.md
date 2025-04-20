# [Unix] C Shell (csh) dirname Usage: Extract directory path from file name

## Overview
The `dirname` command is used to extract the directory path from a given file name. It takes a full file path as input and returns the path leading up to the file, effectively removing the file name itself.

## Usage
The basic syntax of the `dirname` command is as follows:

```csh
dirname [options] [arguments]
```

## Common Options
- `-z`: Suppresses the output if the input is an empty string.
- `--help`: Displays help information about the command.
- `--version`: Shows the version of the `dirname` command.

## Common Examples
Here are some practical examples of using the `dirname` command:

1. Extracting the directory from a full file path:
   ```csh
   dirname /home/user/documents/file.txt
   ```
   Output:
   ```
   /home/user/documents
   ```

2. Using `dirname` with a relative path:
   ```csh
   dirname ./scripts/run.sh
   ```
   Output:
   ```
   ./scripts
   ```

3. Handling multiple file paths:
   ```csh
   dirname /var/log/syslog /usr/local/bin/script.sh
   ```
   Output:
   ```
   /var/log
   /usr/local/bin
   ```

4. Using `dirname` with an empty string:
   ```csh
   dirname ""
   ```
   Output:
   ```
   (no output)
   ```

## Tips
- Always ensure that the input path is valid to avoid unexpected results.
- You can chain `dirname` with other commands using pipes for more complex operations.
- Use `dirname` in scripts to dynamically handle file paths, making your scripts more flexible and robust.