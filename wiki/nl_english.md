# [Linux] C Shell (csh) nl用法: Number lines in text files

## Overview
The `nl` command in C Shell (csh) is used to number the lines of a file. It is particularly useful for adding line numbers to text files, making it easier to reference specific lines in scripts or documents.

## Usage
The basic syntax of the `nl` command is as follows:

```
nl [options] [arguments]
```

## Common Options
- `-b`: Specifies how to number lines. Options include `a` (number all lines), `t` (number only non-empty lines), and `n` (number no lines).
- `-f`: Specifies the number of blank lines to be treated as a single line.
- `-h`: Allows you to specify a header to be printed before the numbered lines.
- `-w`: Sets the width of the line numbers.

## Common Examples
Here are some practical examples of using the `nl` command:

1. **Number all lines in a file:**
   ```csh
   nl myfile.txt
   ```

2. **Number only non-empty lines:**
   ```csh
   nl -b t myfile.txt
   ```

3. **Set a specific width for line numbers:**
   ```csh
   nl -w 4 myfile.txt
   ```

4. **Add a header before the numbered lines:**
   ```csh
   nl -h "Line Numbers:" myfile.txt
   ```

5. **Number lines while ignoring blank lines:**
   ```csh
   nl -b n myfile.txt
   ```

## Tips
- Use the `-w` option to ensure line numbers align properly, especially in larger files.
- Combine `nl` with other commands using pipes for more complex processing, such as `cat myfile.txt | nl`.
- Consider redirecting the output to a new file if you want to save the numbered lines:
  ```csh
  nl myfile.txt > numbered_file.txt
  ```