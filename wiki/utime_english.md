<!--
Meta Description: # Perl utime: Update File Access and Modification Times ## Synopsis The `utime` function in Perl is used to update the access and modification times o...
Meta Keywords: time, files, timestamps, utime, file
-->

# Perl utime: Update File Access and Modification Times

## Synopsis
The `utime` function in Perl is used to update the access and modification times of files. It allows you to set the timestamps for one or more files, enabling precise control over file metadata.

## Documentation
### Purpose
The primary purpose of the `utime` function is to modify the timestamps of files in the filesystem. This can be useful for various tasks, such as scripting backups, managing file versions, or simulating file activity.

### Usage
The `utime` function is invoked in the following manner:

```perl
utime($access_time, $modification_time, @files);
```

- **$access_time**: The new access time for the specified files. If set to `undef`, the current time is used.
- **$modification_time**: The new modification time for the specified files. If set to `undef`, the current time is used.
- **@files**: A list of filenames whose timestamps are to be updated.

**Returns**: The function returns a true value on success and `undef` on failure. If it fails, the `$!` variable will contain the error message.

### Details
- **Timestamps**: Both `$access_time` and `$modification_time` should be provided as epoch seconds (seconds since January 1, 1970). You can use the `time()` function to obtain the current epoch time.
- **File Existence**: The files specified must exist; otherwise, `utime` will fail.
- **Permissions**: The user must have sufficient permissions to modify the timestamps of the files.

## Examples

### Example 1: Update Timestamps to Current Time
```perl
use strict;
use warnings;

my @files = ('example.txt', 'sample.txt');
utime(time(), time(), @files) or die "Failed to update timestamps: $!";
```
This example updates the access and modification times of `example.txt` and `sample.txt` to the current time.

### Example 2: Set Custom Timestamps
```perl
use strict;
use warnings;

my @files = ('example.txt');
my $access_time = time() - 3600;  # Access time set to 1 hour ago
my $modification_time = time() - 7200;  # Modification time set to 2 hours ago

utime($access_time, $modification_time, @files) or die "Failed to update timestamps: $!";
```
In this example, the access time is set to one hour ago and the modification time is set to two hours ago for `example.txt`.

## Explanation
### Common Pitfalls
- **File Not Found**: If a specified file does not exist, `utime` will fail, so always check if files exist before invoking the function.
- **Permission Issues**: Ensure that you have the necessary permissions to modify the files. Lack of write permission will result in a failure.
- **Incorrect Time Format**: The timestamps must be in epoch format. Be cautious if using other time formats.

### Additional Notes
- On some operating systems, the `utime` function may not work as expected if the filesystem does not support setting timestamps.
- When using `utime` in scripts that are run by different users, consider the implications of changing file timestamps on shared resources.

## One Line Summary
The `utime` function in Perl updates the access and modification timestamps of specified files, allowing for precise file metadata management.