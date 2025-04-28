<!--
Meta Description: # Readline in Perl: The Essential Guide to Reading Input ## Synopsis The `readline` function in Perl is a powerful tool for reading input from filehan...
Meta Keywords: line, readline, from, filehandle, perl
-->

# Readline in Perl: The Essential Guide to Reading Input

## Synopsis
The `readline` function in Perl is a powerful tool for reading input from filehandles, including standard input. It allows for efficient line-by-line processing of data, making it an essential feature for file manipulation and user interaction in Perl scripts.

## Documentation
### Purpose
The `readline` function is used to read lines from a filehandle or an array. It can handle input from various sources, including files and user input through the command line.

### Usage
The basic syntax of `readline` is as follows:

```perl
my $line = readline($filehandle);
```

Where `$filehandle` is the filehandle from which you want to read. If you omit the filehandle, `readline` will read from the default filehandle, which is `STDIN`.

### Details
- **Return Value**: `readline` returns the line read from the specified filehandle. If the end of the file is reached, it returns `undef`.
- **Context**: In a scalar context, `readline` returns a single line. In a list context, it returns all remaining lines as an array.
- **Chomp**: It is common to `chomp` the result of `readline` to remove the newline character from the end of the line.

## Examples
### Example 1: Basic Usage
```perl
# Reading from a file
open my $fh, '<', 'example.txt' or die "Cannot open file: $!";
while (my $line = readline($fh)) {
    chomp $line;  # Remove newline character
    print "$line\n";
}
close $fh;
```

### Example 2: Reading from STDIN
```perl
# Reading user input
print "Enter some text (Ctrl+D to end):\n";
while (my $line = readline(*STDIN)) {
    chomp $line;
    print "You entered: $line\n";
}
```

### Example 3: Reading Multiple Lines
```perl
# Reading all lines from a file into an array
open my $fh, '<', 'example.txt' or die "Cannot open file: $!";
my @lines = readline($fh);
close $fh;

# Process each line
foreach my $line (@lines) {
    chomp $line;
    print "$line\n";
}
```

## Explanation
### Common Pitfalls
- **End of File Handling**: Be cautious of reaching the end of a file. If you continue to call `readline` after reaching EOF, it will return `undef`, which may lead to infinite loops if not handled properly.
- **Context Awareness**: Remember that `readline` behaves differently in scalar and list contexts. Ensure that you are using the correct context for your needs.

### Gotchas
- **Filehandle Not Defined**: If you pass an undefined filehandle to `readline`, it will raise a runtime error. Always check that your filehandle is valid before using it.
- **Chomp Usage**: Failing to use `chomp` may lead to unexpected newline characters in your output. Always consider whether the inclusion of newline characters is appropriate for your application.

## One Line Summary
The `readline` function in Perl is a versatile method for reading lines from filehandles or arrays, crucial for effective input processing in scripts.