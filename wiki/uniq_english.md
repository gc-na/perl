# [Linux] C Shell (csh) uniq Uso: Remove duplicate lines from sorted files

## Overview
The `uniq` command in C Shell (csh) is used to filter out repeated lines in a sorted file. It reads the input and outputs only the unique lines, making it useful for data processing and analysis.

## Usage
The basic syntax of the `uniq` command is as follows:

```
uniq [options] [arguments]
```

## Common Options
- `-c`: Prefix each line with the number of occurrences.
- `-d`: Only print duplicate lines.
- `-u`: Only print unique lines (lines that are not repeated).
- `-i`: Ignore case when comparing lines.

## Common Examples
Here are some practical examples of how to use the `uniq` command:

1. **Basic usage**: Remove duplicates from a sorted file.
   ```csh
   uniq sorted_file.txt
   ```

2. **Count occurrences**: Show how many times each line appears.
   ```csh
   uniq -c sorted_file.txt
   ```

3. **Show only duplicates**: Display lines that appear more than once.
   ```csh
   uniq -d sorted_file.txt
   ```

4. **Show only unique lines**: Display lines that are not repeated.
   ```csh
   uniq -u sorted_file.txt
   ```

5. **Ignore case**: Remove duplicates while ignoring case sensitivity.
   ```csh
   uniq -i sorted_file.txt
   ```

## Tips
- Always sort your input file before using `uniq`, as it only removes adjacent duplicate lines.
- Use the `-c` option to quickly identify how many times each line appears, which can be helpful for data analysis.
- Combine `uniq` with other commands like `sort` to enhance its functionality, for example:
  ```csh
  sort unsorted_file.txt | uniq
  ```
- Remember that `uniq` processes input from standard input as well, so you can pipe data directly into it.