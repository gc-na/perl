# [Linux] C Shell (csh) grep用法: Search text using patterns

## Overview
The `grep` command is a powerful utility used to search for specific patterns within files or input provided to it. It stands for "Global Regular Expression Print" and is commonly used in Unix-like operating systems for text processing.

## Usage
The basic syntax of the `grep` command is as follows:

```csh
grep [options] [arguments]
```

## Common Options
Here are some common options you can use with `grep`:

- `-i`: Ignore case distinctions in both the pattern and the input files.
- `-v`: Invert the match to select non-matching lines.
- `-r`: Recursively search through directories.
- `-n`: Prefix each line of output with the line number within the file.
- `-l`: Only print the names of files with matching lines, once for each file.

## Common Examples
Here are some practical examples of using `grep`:

1. **Basic search for a word in a file:**
   ```csh
   grep "example" myfile.txt
   ```

2. **Case-insensitive search:**
   ```csh
   grep -i "example" myfile.txt
   ```

3. **Search recursively in a directory:**
   ```csh
   grep -r "example" /path/to/directory
   ```

4. **Show line numbers of matches:**
   ```csh
   grep -n "example" myfile.txt
   ```

5. **Find files that contain a specific word:**
   ```csh
   grep -l "example" *.txt
   ```

## Tips
- Use `grep` in combination with other commands using pipes to filter output effectively.
- Regular expressions can enhance your search patterns, allowing for more complex queries.
- When searching through large files, consider using `less` or `more` to paginate the output for easier reading.