# [Linux] C Shell (csh) wget用法: Download files from the web

## Overview
The `wget` command is a powerful utility used for downloading files from the web. It supports various protocols, including HTTP, HTTPS, and FTP, making it versatile for retrieving content from different sources.

## Usage
The basic syntax of the `wget` command is as follows:

```bash
wget [options] [arguments]
```

## Common Options
- `-O <file>`: Save the downloaded file with a specified name.
- `-q`: Operate in quiet mode, suppressing output.
- `-c`: Continue an incomplete download from where it left off.
- `-r`: Download files recursively, useful for downloading entire websites.
- `--limit-rate=<rate>`: Limit the download speed to a specified rate.

## Common Examples
Here are some practical examples of using `wget`:

1. **Download a single file:**
   ```bash
   wget http://example.com/file.zip
   ```

2. **Download a file and save it with a different name:**
   ```bash
   wget -O myfile.zip http://example.com/file.zip
   ```

3. **Continue an interrupted download:**
   ```bash
   wget -c http://example.com/largefile.zip
   ```

4. **Download an entire website recursively:**
   ```bash
   wget -r http://example.com
   ```

5. **Limit the download speed:**
   ```bash
   wget --limit-rate=200k http://example.com/largefile.zip
   ```

## Tips
- Use the `-q` option for scripts to minimize output and make logs cleaner.
- When downloading large files, consider using the `-c` option to avoid starting over if the download fails.
- For recursive downloads, be cautious as it can consume significant bandwidth and storage space.