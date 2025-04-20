# [Linux] C Shell (csh) iconv 用法: Convert character encoding

## Overview
The `iconv` command is a utility that converts text from one character encoding to another. It is particularly useful when dealing with files that may not be in the desired encoding format, allowing users to ensure compatibility across different systems and applications.

## Usage
The basic syntax of the `iconv` command is as follows:

```csh
iconv [options] [arguments]
```

## Common Options
- `-f, --from-code=CODE`: Specifies the encoding of the input text.
- `-t, --to-code=CODE`: Specifies the encoding for the output text.
- `-o, --output=FILE`: Redirects the output to a specified file instead of standard output.
- `-l, --list`: Lists all available encodings.

## Common Examples
Here are some practical examples of using the `iconv` command:

1. **Convert a file from UTF-8 to ISO-8859-1:**

   ```csh
   iconv -f UTF-8 -t ISO-8859-1 input.txt -o output.txt
   ```

2. **Convert a file and display the output in the terminal:**

   ```csh
   iconv -f UTF-8 -t UTF-16 input.txt
   ```

3. **List all available encodings:**

   ```csh
   iconv -l
   ```

4. **Convert a string from Windows-1252 to UTF-8:**

   ```csh
   echo "Hello, World!" | iconv -f WINDOWS-1252 -t UTF-8
   ```

## Tips
- Always check the encoding of your input file before conversion to avoid data loss or corruption.
- Use the `-o` option to save the converted output to a file, especially for large files.
- If you're unsure about the encoding, use the `-l` option to list available encodings and find the correct one.