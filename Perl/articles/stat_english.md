<!--
Meta Description: # Understanding the Perl `stat` Function: A Comprehensive Guide ## Synopsis The Perl `stat` function retrieves detailed information about a file, incl...
Meta Keywords: file, stat, perl, size, info
-->

# Understanding the Perl `stat` Function: A Comprehensive Guide

## Synopsis
The Perl `stat` function retrieves detailed information about a file, including its size, permissions, and timestamps, allowing developers to perform file management operations efficiently.

## Documentation
The `stat` function in Perl is used to obtain status information about a file. It returns a list of 13 values that describe the file's attributes. This function can be invoked in two ways: using a filehandle or a filename.

### Purpose
The primary purpose of `stat` is to provide metadata about files, which can be useful for various file manipulation tasks such as determining file size, checking file type, and monitoring modification times.

### Usage
The syntax for `stat` is as follows:

```perl
@file_info = stat(FILEHANDLE);
```
or
```perl
@file_info = stat('filename');
```

### Return Values
The `stat` function returns a list of values, which can be assigned to an array. The typical values returned are:

1. File's inode number
2. Device ID
3. File's mode (permissions)
4. Number of hard links
5. User ID of the file's owner
6. Group ID of the file's owner
7. Size of the file in bytes
8. Last access time (epoch)
9. Last modification time (epoch)
10. Last change time (epoch)
11. File's block size
12. Number of blocks allocated
13. File type (directory, regular file, etc.)

If the file does not exist, `stat` will return `undef`.

## Examples

### Basic Usage
Here’s a simple example of how to use `stat` with a filename:

```perl
my $filename = 'example.txt';
my @info = stat($filename);

if (@info) {
    print "File Size: $info[7] bytes\n";              # Size of the file
    print "Last Modified: " . localtime($info[9]) . "\n"; # Last modification time
} else {
    warn "Could not stat file: $!";
}
```

### Using `stat` with Filehandles
You can also use `stat` with filehandles. Here’s how:

```perl
open my $fh, '<', 'example.txt' or die "Cannot open file: $!";
my @info = stat($fh);
close $fh;

if (@info) {
    print "File Size: $info[7] bytes\n";
} else {
    warn "Could not stat file: $!";
}
```

## Explanation
While using `stat`, there are a few common pitfalls to be aware of:

- **File Existence**: Always check if the file exists before calling `stat`, as it will return `undef` for non-existent files.
- **File Permissions**: Ensure that your script has the necessary permissions to read the file; otherwise, `stat` will fail.
- **Context Sensitivity**: The context in which `stat` is called can change its behavior; if used in scalar context, it returns the inode number instead of an array.

## One Line Summary
The Perl `stat` function retrieves comprehensive metadata about a file, enabling efficient file management and manipulation.