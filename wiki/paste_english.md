# [Linux] C Shell (csh) paste用法: Combine lines of files

## Overview
The `paste` command in C Shell (csh) is used to merge lines of files horizontally. It takes multiple input files and combines their corresponding lines into a single line, separating them with a specified delimiter (default is a tab).

## Usage
The basic syntax of the `paste` command is as follows:

```csh
paste [options] [arguments]
```

## Common Options
- `-d`: Specify a custom delimiter instead of the default tab.
- `-s`: Paste the lines of each file sequentially instead of in parallel.
- `-z`: Treats the input as null-terminated strings instead of newline-terminated.

## Common Examples

1. **Basic usage with two files**:
   Combine lines from `file1.txt` and `file2.txt`:
   ```csh
   paste file1.txt file2.txt
   ```

2. **Using a custom delimiter**:
   Combine lines from `file1.txt` and `file2.txt` with a comma as the delimiter:
   ```csh
   paste -d ',' file1.txt file2.txt
   ```

3. **Sequential pasting**:
   Combine lines from `file1.txt` into a single line, pasting them one after the other:
   ```csh
   paste -s file1.txt
   ```

4. **Pasting with null-terminated strings**:
   Combine files treating input as null-terminated:
   ```csh
   paste -z file1.txt file2.txt
   ```

## Tips
- When using custom delimiters, ensure that the delimiter does not appear in the original files to avoid confusion.
- Use the `-s` option when you want to create a single line output from a file, which can be useful for summarizing data.
- If you are combining many files, consider using wildcards (e.g., `*.txt`) to simplify your command.