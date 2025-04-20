# [Linux] C Shell (csh) head用法: Display the beginning of a file

## Overview
The `head` command in C Shell (csh) is used to display the first few lines of a file. By default, it shows the first 10 lines, but this can be adjusted with options. This command is particularly useful for quickly viewing the contents of files without opening them entirely.

## Usage
The basic syntax of the `head` command is as follows:

```csh
head [options] [arguments]
```

## Common Options
- `-n <number>`: Specify the number of lines to display from the start of the file. For example, `-n 5` will show the first 5 lines.
- `-q`: Suppresses the output of the file name when multiple files are specified.
- `-v`: Always print the file name before the output, even if only one file is provided.

## Common Examples
Here are some practical examples of using the `head` command:

1. Display the first 10 lines of a file named `example.txt`:
   ```csh
   head example.txt
   ```

2. Display the first 5 lines of a file:
   ```csh
   head -n 5 example.txt
   ```

3. Display the first 15 lines of multiple files:
   ```csh
   head -n 15 file1.txt file2.txt
   ```

4. Show the first 10 lines of a file without displaying the file name:
   ```csh
   head -q example.txt
   ```

5. Always show the file name before the output:
   ```csh
   head -v example.txt
   ```

## Tips
- Use `head` in combination with other commands like `grep` or `less` to filter or paginate output effectively.
- When working with large files, `head` can save time by allowing you to quickly check the beginning of the file without loading it entirely.
- Remember that `head` reads from standard input if no file is specified, which can be useful in pipelines. For example:
  ```csh
  cat largefile.txt | head -n 10
  ```