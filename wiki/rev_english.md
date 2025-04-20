# [Unix] C Shell (csh) rev: Reverse lines of a file

## Overview
The `rev` command is used to reverse the characters of each line in a given file or standard input. This can be particularly useful for text manipulation or when working with data that requires a specific format.

## Usage
The basic syntax of the `rev` command is as follows:

```
rev [options] [arguments]
```

## Common Options
- `-o, --output=FILE`: Write the reversed output to the specified file instead of standard output.
- `-h, --help`: Display a help message with usage information.
- `-V, --version`: Show the version information of the `rev` command.

## Common Examples
Here are some practical examples of how to use the `rev` command:

1. **Reversing text from a file:**
   To reverse the lines of a file named `example.txt`, you can use:
   ```csh
   rev example.txt
   ```

2. **Reversing text from standard input:**
   You can also reverse text directly from the command line:
   ```csh
   echo "Hello World" | rev
   ```

3. **Reversing and saving output to a new file:**
   To reverse the contents of `example.txt` and save it to `reversed.txt`, use:
   ```csh
   rev example.txt > reversed.txt
   ```

4. **Reversing multiple files:**
   You can reverse the contents of multiple files at once:
   ```csh
   rev file1.txt file2.txt
   ```

## Tips
- When using `rev`, remember that it operates on a line-by-line basis, so each line will be reversed independently.
- If you want to keep the original file intact while saving the reversed output, always redirect the output to a new file.
- Use `cat` in combination with `rev` to view the contents of a file in reverse without modifying the original file:
  ```csh
  cat example.txt | rev
  ```