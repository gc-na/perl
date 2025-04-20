# [Linux] C Shell (csh) sha256sum uso equivalente: Calculate SHA-256 checksums

## Overview
The `sha256sum` command is used to compute and verify SHA-256 checksums for files. This is particularly useful for ensuring data integrity by allowing users to compare the checksum of a file against a known value.

## Usage
The basic syntax of the `sha256sum` command is as follows:

```csh
sha256sum [options] [arguments]
```

## Common Options
- `-b`: Read the input files in binary mode.
- `-c`: Check the SHA-256 checksums against the provided checksum file.
- `-h`: Display help information about the command.
- `--quiet`: Suppress output messages.

## Common Examples
Here are some practical examples of using the `sha256sum` command:

1. **Calculate the SHA-256 checksum of a file:**
   ```csh
   sha256sum myfile.txt
   ```

2. **Save the checksum to a file:**
   ```csh
   sha256sum myfile.txt > myfile.txt.sha256
   ```

3. **Verify a file against a checksum file:**
   ```csh
   sha256sum -c myfile.txt.sha256
   ```

4. **Calculate the checksum of multiple files:**
   ```csh
   sha256sum file1.txt file2.txt file3.txt
   ```

## Tips
- Always verify checksums after downloading files to ensure they have not been corrupted.
- Use the `-c` option with a checksum file to automate the verification process.
- Consider using the `-b` option when dealing with binary files to avoid issues with newline characters.