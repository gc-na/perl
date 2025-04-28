<!--
Meta Description: # socketpair: Creating Inter-Process Communication Sockets in Perl ## Synopsis `socketpair` is a Perl function that creates a pair of connected socket...
Meta Keywords: socketpair, sock1, sock2, sockets, use
-->

# socketpair: Creating Inter-Process Communication Sockets in Perl

## Synopsis
`socketpair` is a Perl function that creates a pair of connected sockets for inter-process communication (IPC). It is typically used for communication between parent and child processes or between two related processes.

## Documentation
### Purpose
The `socketpair` function in Perl is designed to facilitate communication between two processes through a pair of sockets. These sockets can be used in various ways, such as sending and receiving data, allowing bidirectional communication between processes.

### Usage
To use `socketpair`, you must first import it from the `IO::Socket` module. Here's the basic syntax:

```perl
use IO::Socket;

socketpair(my $sock1, my $sock2, AF_UNIX, SOCK_STREAM, 0) or die "socketpair: $!";
```

### Parameters
- **$sock1** and **$sock2**: These are scalar references that will hold the created socket handles.
- **AF_UNIX**: This indicates that the sockets will use the Unix domain.
- **SOCK_STREAM**: This specifies the type of socket, which in this case is a stream socket.
- **0**: This is the protocol number, and `0` lets the OS choose the default protocol.

### Return Value
The `socketpair` function returns `true` on success and `undef` on failure, allowing you to handle errors appropriately using the `die` function or similar error-handling mechanisms.

## Examples
### Basic Example
Here’s a simple example demonstrating how to create a socket pair and send a message between the two sockets:

```perl
use strict;
use warnings;
use IO::Socket;

my ($sock1, $sock2);
socketpair($sock1, $sock2, AF_UNIX, SOCK_STREAM) or die "socketpair: $!";

# Send a message from sock1
print $sock1 "Hello from sock1!\n";

# Receive the message on sock2
my $message = <$sock2>;
print "sock2 received: $message";

# Close the sockets
close($sock1);
close($sock2);
```

### Forking Example
In a forking scenario, `socketpair` is especially useful for parent-child communication:

```perl
use strict;
use warnings;
use IO::Socket;
use POSIX ":sys_wait_h";

my ($sock1, $sock2);
socketpair($sock1, $sock2, AF_UNIX, SOCK_STREAM) or die "socketpair: $!";

my $pid = fork();

if (defined $pid && $pid == 0) {  # Child process
    close($sock1);  # Close unused socket
    print $sock2 "Message from child process\n";
    close($sock2);
    exit(0);
} else {  # Parent process
    close($sock2);  # Close unused socket
    my $message = <$sock1>;
    print "Parent received: $message";
    close($sock1);
    waitpid($pid, 0);  # Wait for child process to finish
}
```

## Explanation
### Common Pitfalls
- **Socket Closure**: Always ensure that you close any sockets you open to prevent resource leaks.
- **Error Handling**: Always check the return value of `socketpair`. If it fails, it will return `undef`, and you should handle the error appropriately.
- **Blocking Behavior**: Depending on the mode of the sockets, reads and writes can block. Consider using non-blocking modes if necessary.

### Gotchas
- The use of `AF_UNIX` limits the application to Unix-like operating systems. For cross-platform applications, consider using `AF_INET` with TCP sockets.
- Ensure that your Perl script runs with appropriate permissions to create sockets, especially in restricted environments.

## One Line Summary
`socketpair` in Perl creates a pair of connected sockets for efficient inter-process communication.