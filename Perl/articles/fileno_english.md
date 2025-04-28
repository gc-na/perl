<!--
Meta Description: # Understanding `fileno` in Perl: A Comprehensive Guide ## Synopsis The `fileno` function in Perl is used to retrieve the file descriptor associated w...
Meta Keywords: fileno, file, descriptor, filehandle, perl
-->

# Understanding `fileno` in Perl: A Comprehensive Guide

## Synopsis
The `fileno` function in Perl is used to retrieve the file descriptor associated with a given filehandle, enabling low-level file operations and efficient resource management.

## Documentation
### Purpose
The `fileno` function provides a way to obtain the file descriptor number for a filehandle. This is particularly useful when you need to perform operations that require raw file descriptors, such as using system calls or interfacing with lower-level system libraries.

### Usage
The syntax for using `fileno` is straightforward:

```perl
my $fileno = fileno($filehandle);
```

Where `$filehandle` is a valid filehandle, such as those opened with `open`, `IO::File`, or standard input/output/error filehandles (`STDIN`, `STDOUT`, `STDERR`). If the filehandle is not associated with an open file, `fileno` returns `undef`.

### Details
- **Return Value**: `fileno` returns the file descriptor as a non-negative integer if the filehandle is valid; otherwise, it returns `undef`.
- **Error Handling**: It is essential to check if the filehandle is valid before calling `fileno` to avoid unexpected `undef` values.
- **Filehandles**: The function works with both user-defined and built-in filehandles.
- **Context**: `fileno` can be used in scalar context only.

## Examples
### Basic Example
Here’s a basic example demonstrating how to use `fileno`:

```perl
use strict;
use warnings;

# Open a file for reading
open my $fh, '<', 'example.txt' or die "Cannot open file: $!";

# Get the file descriptor
my $fd = fileno($fh);
print "File descriptor: $fd\n";

# Clean up
close $fh;
```

### Example with Standard Input
You can also use `fileno` with standard filehandles:

```perl
# Get the file descriptor for STDIN
my $stdin_fd = fileno(STDIN);
print "Standard input file descriptor: $stdin_fd\n";
```

## Explanation
### Common Pitfalls
- **Undefined Filehandles**: Calling `fileno` with an undefined or closed filehandle will result in `undef`. Always ensure your filehandle is valid and open before using `fileno`.
- **Not Checking Return Values**: Failing to check the return value of `fileno` can lead to errors in your program if you attempt to use an invalid file descriptor.

### Additional Notes
- `fileno` is particularly useful when you need to use the file descriptor in system calls like `select`, `poll`, or when interfacing with C libraries through XS or FFI.
- If you're working with a `IO::Socket` object, `fileno` will return the underlying file descriptor, which can be useful for network programming.

## One Line Summary
The `fileno` function in Perl retrieves the file descriptor for a given filehandle, facilitating low-level file operations.