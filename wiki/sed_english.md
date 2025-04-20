# [Linux] C Shell (csh) sed用法: Stream editor for filtering and transforming text

## Overview
The `sed` command, short for stream editor, is a powerful utility in Unix-like operating systems used for parsing and transforming text. It reads input line by line, applies specified operations, and outputs the modified text. This makes it particularly useful for tasks such as text substitution, deletion, and insertion.

## Usage
The basic syntax of the `sed` command is as follows:

```bash
sed [options] [arguments]
```

## Common Options
- `-e`: Allows the execution of multiple editing commands.
- `-i`: Edits files in place, modifying the original file directly.
- `-n`: Suppresses automatic printing of the pattern space; useful when you want to control what gets output.
- `s/pattern/replacement/`: Substitutes the first occurrence of `pattern` with `replacement` in each line.

## Common Examples

### 1. Basic Substitution
Replace the first occurrence of "apple" with "orange" in a file:

```bash
sed 's/apple/orange/' filename.txt
```

### 2. Global Substitution
Replace all occurrences of "apple" with "orange" in a file:

```bash
sed 's/apple/orange/g' filename.txt
```

### 3. In-Place Editing
Directly modify a file by replacing "apple" with "orange":

```bash
sed -i 's/apple/orange/g' filename.txt
```

### 4. Deleting Lines
Delete lines that contain the word "banana":

```bash
sed '/banana/d' filename.txt
```

### 5. Print Specific Lines
Print only lines 2 to 4 from a file:

```bash
sed -n '2,4p' filename.txt
```

## Tips
- Always make a backup of your files before using the `-i` option to prevent accidental data loss.
- Use the `-n` option in combination with the `p` command to control output and only print lines that match specific criteria.
- Test your `sed` commands without the `-i` option first to ensure they produce the desired output before making changes to files.