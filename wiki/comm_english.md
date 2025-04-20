# [Linux] C Shell (csh) comm 命令: Compare two sorted files line by line

## Overview
The `comm` command in C Shell is used to compare two sorted files line by line. It outputs the lines that are unique to each file and the lines that are common to both files, making it a useful tool for identifying differences and similarities between two datasets.

## Usage
The basic syntax of the `comm` command is as follows:

```csh
comm [options] [file1] [file2]
```

## Common Options
- `-1`: Suppress the output of lines unique to the first file.
- `-2`: Suppress the output of lines unique to the second file.
- `-3`: Suppress the output of lines that are common to both files.
- `-i`: Ignore case differences when comparing lines.

## Common Examples

1. **Basic Comparison**:
   To compare two sorted files and display all differences:
   ```csh
   comm file1.txt file2.txt
   ```

2. **Suppress Unique Lines from First File**:
   To show only the lines unique to the second file and the common lines:
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. **Suppress Common Lines**:
   To display only the unique lines from both files:
   ```csh
   comm -12 file1.txt file2.txt
   ```

4. **Case-Insensitive Comparison**:
   To compare two files while ignoring case:
   ```csh
   comm -i file1.txt file2.txt
   ```

## Tips
- Ensure that both files are sorted before using `comm`, as the command requires sorted input for accurate comparison.
- Use the `-1`, `-2`, and `-3` options in combination to customize the output based on your needs.
- Redirect the output to a file if you want to save the comparison results for later analysis:
   ```csh
   comm file1.txt file2.txt > comparison_results.txt
   ```