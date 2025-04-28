<!--
Meta Description: # Perl Alarm Function: Controlling Timeouts in Perl Scripts ## Synopsis The `alarm` function in Perl is used to schedule a signal (SIGALRM) to be sent...
Meta Keywords: alarm, perl, signal, seconds, sigalrm
-->

# Perl Alarm Function: Controlling Timeouts in Perl Scripts

## Synopsis
The `alarm` function in Perl is used to schedule a signal (SIGALRM) to be sent to the process after a specified number of seconds, allowing for the implementation of timeouts in scripts.

## Documentation
The `alarm` function is a built-in Perl function that sets an alarm clock for the program. When the specified number of seconds elapses, the operating system sends the SIGALRM signal to the running process. This can be particularly useful for controlling the execution time of operations, such as network requests or lengthy computations.

### Purpose
- To implement timeouts for operations that may hang or take too long to complete.
- To provide a mechanism for interrupting long-running processes.

### Usage
```perl
alarm SECONDS;
```
Where `SECONDS` is the number of seconds after which the SIGALRM signal will be sent.

### Details
- If `SECONDS` is set to zero, it disables any existing alarm.
- The alarm can trigger a custom signal handler if one is defined, or it will terminate the program if no handler is set up.
- The SIGALRM signal is not supported on all operating systems, so its behavior may vary.

## Examples
### Example 1: Basic Usage
```perl
#!/usr/bin/perl
use strict;
use warnings;

# Set an alarm for 5 seconds
alarm(5);

# Simulate a long-running operation
while (1) {
    print "Working...\n";
    sleep(1);
}
```
In this example, after 5 seconds, the program will receive a SIGALRM signal, which by default will terminate the program.

### Example 2: Using a Signal Handler
```perl
#!/usr/bin/perl
use strict;
use warnings;

# Define a signal handler for SIGALRM
$SIG{ALRM} = sub {
    print "Timeout occurred!\n";
    exit;
};

# Set an alarm for 3 seconds
alarm(3);

# Simulate a long-running operation
while (1) {
    print "Working...\n";
    sleep(1);
}
```
Here, instead of terminating, the program will execute the defined signal handler when the alarm goes off.

## Explanation
- **Common Pitfalls**: Forgetting to reset the alarm can lead to unexpected behavior, especially if the program is interrupted or runs longer than intended.
- **Gotchas**: The alarm does not interrupt system calls that may be blocking. For example, an alarm will not interrupt a `sleep` call that is still executing.
- **Additional Notes**: The behavior of `alarm` and `SIGALRM` can differ based on the operating system. It is essential to consult the appropriate documentation for the environment where the script will run.

## One Line Summary
The `alarm` function in Perl is used to schedule a timeout for operations by sending a SIGALRM signal after a specified duration.