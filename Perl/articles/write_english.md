<!--
Meta Description: # Writing Data in Perl: Understanding the `write` Function ## Synopsis The `write` function in Perl is used to output formatted data to a filehandle, ...
Meta Keywords: format, write, data, filehandle, output
-->

# Writing Data in Perl: Understanding the `write` Function

## Synopsis
The `write` function in Perl is used to output formatted data to a filehandle, allowing for the creation of structured reports and formatted text output.

## Documentation
### Purpose
The `write` function is primarily utilized for printing formatted data to a specified filehandle based on a predefined format. This is particularly useful for generating structured reports or logs.

### Usage
To use the `write` function, you first need to define a format using the `format` keyword. The `write` function then outputs data according to this format to a filehandle, which can be either a file or the default output (STDOUT).

#### Syntax
```perl
format NAME = 
    ... pattern ...
.

write FILEHANDLE;
```

### Details
- **Format Declaration**: Before calling `write`, you need to define a format with the `format` keyword. Each format can have multiple fields that dictate how the data will be presented.
- **Filehandle**: The filehandle can be an open file or STDOUT. If omitted, it defaults to the currently selected output filehandle.
- **Automatic Formatting**: The `write` function automatically handles spacing and alignment according to the defined format.
  
### Format Specifiers
- **`@<`**: Left justify data within a specified width.
- **`@>`**: Right justify data within a specified width.
- **`^<`**: Center data within a specified width.
- **`$`**: Used for dollar formatting.

## Examples
### Basic Example
Here’s a simple example demonstrating the use of `write`:

```perl
# Define a format
format MYFORMAT =
------------------------------------
Name:       @<<<<<<<<<<<<<<<<<<
Age:        @<<
------------------------------------
.

# Prepare data
my $name = "Alice";
my $age = 30;

# Write to STDOUT using the defined format
write;
```

### Writing to a File
To write formatted output to a file:

```perl
open my $fh, '>', 'output.txt' or die "Cannot open output.txt: $!";
select $fh;  # Change the default filehandle to $fh

# Define a format
format MYFORMAT =
------------------------------------
Name:       @<<<<<<<<<<<<<<<<<<
Age:        @<<
------------------------------------
.

# Prepare and write data
my @data = (
    ["Alice", 30],
    ["Bob", 25]
);

foreach my $person (@data) {
    my ($name, $age) = @$person;
    write;  # Call write for each person
}

close $fh;  # Close the filehandle
```

## Explanation
### Common Pitfalls
- **Undefined Formats**: Ensure that the format is defined before calling `write`. If not, it will result in an error.
- **Filehandle Selection**: Always check which filehandle is currently selected using `select`, especially when writing to files.
- **Automatic Formating Limitations**: If the output exceeds the defined width, the data may not display correctly; ensure that your format accommodates the longest expected input.

### Additional Notes
- The `write` function is not used as frequently as other output methods like `print`, mainly due to its complexity and the need for format definitions.
- It can be beneficial in generating reports where uniformity is critical, such as in financial statements or structured logs.

## One Line Summary
The `write` function in Perl outputs formatted data to a filehandle, enabling the creation of structured and aligned text reports.