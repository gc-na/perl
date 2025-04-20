# [Unix] C Shell (csh) getopts用法: Command-line option parsing

## Overview
The `getopts` command in C Shell (csh) is used for parsing command-line options and arguments. It allows scripts to handle options in a standardized way, making it easier to manage user inputs.

## Usage
The basic syntax of the `getopts` command is as follows:

```csh
getopts optstring variable
```

- `optstring`: A string that defines the valid options.
- `variable`: The name of the variable that will store the option found.

## Common Options
- `optstring`: A string of characters where each character represents a valid option. If an option requires an argument, it is followed by a colon (`:`).
- `variable`: The name of the variable that will hold the current option being processed.

## Common Examples

### Example 1: Basic Option Parsing
This example demonstrates how to parse single-letter options.

```csh
#!/bin/csh

set optstring = "ab"
while (1)
    getopts $optstring option
    if ($? != 0) break
    switch ($option)
        case "a":
            echo "Option A selected"
            breaksw
        case "b":
            echo "Option B selected"
            breaksw
        default:
            echo "Invalid option"
    endsw
end
```

### Example 2: Options with Arguments
In this example, we show how to handle options that require arguments.

```csh
#!/bin/csh

set optstring = "a:b:"
while (1)
    getopts $optstring option
    if ($? != 0) break
    switch ($option)
        case "a":
            echo "Option A selected with argument: $OPTARG"
            breaksw
        case "b":
            echo "Option B selected with argument: $OPTARG"
            breaksw
        default:
            echo "Invalid option"
    endsw
end
```

### Example 3: Handling Invalid Options
This example illustrates how to handle invalid options gracefully.

```csh
#!/bin/csh

set optstring = "abc"
while (1)
    getopts $optstring option
    if ($? != 0) break
    switch ($option)
        case "a":
            echo "Option A selected"
            breaksw
        case "b":
            echo "Option B selected"
            breaksw
        case "c":
            echo "Option C selected"
            breaksw
        default:
            echo "Invalid option: $option"
    endsw
end
```

## Tips
- Always check the return status of `getopts` to determine if parsing was successful.
- Use `OPTARG` to access the argument associated with an option that requires one.
- Keep your `optstring` organized and clearly define which options require arguments for better readability and maintenance.