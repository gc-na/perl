# [Unix] C Shell (csh) scp Uso: Securely copy files between hosts

## Overview
The `scp` (secure copy) command is used to securely transfer files and directories between two hosts over a network. It utilizes SSH (Secure Shell) for data transfer, ensuring that the data is encrypted during the process.

## Usage
The basic syntax of the `scp` command is as follows:

```bash
scp [options] [source] [destination]
```

## Common Options
- `-r`: Recursively copy entire directories.
- `-P port`: Specify the port to connect to on the remote host.
- `-i identity_file`: Select the file from which the identity (private key) for public key authentication is read.
- `-v`: Enable verbose mode, which provides detailed information about the transfer process.

## Common Examples
1. **Copy a file from local to remote:**
   ```bash
   scp localfile.txt user@remotehost:/path/to/destination/
   ```

2. **Copy a file from remote to local:**
   ```bash
   scp user@remotehost:/path/to/remotefile.txt /local/destination/
   ```

3. **Copy a directory recursively from local to remote:**
   ```bash
   scp -r localdirectory/ user@remotehost:/path/to/destination/
   ```

4. **Copy a file using a specific port:**
   ```bash
   scp -P 2222 localfile.txt user@remotehost:/path/to/destination/
   ```

5. **Copy a file using a specific identity file:**
   ```bash
   scp -i ~/.ssh/id_rsa localfile.txt user@remotehost:/path/to/destination/
   ```

## Tips
- Always ensure that the SSH service is running on the remote host before attempting to use `scp`.
- Use the `-v` option for troubleshooting if you encounter issues during file transfer.
- When transferring large files or directories, consider using `rsync` for better performance and resuming capabilities.