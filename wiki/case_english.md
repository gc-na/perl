# [Unix] C Shell (csh) case <Uso equivalente en inglés>: Pattern matching and execution

## Overview
The `case` command in C Shell (csh) is used for pattern matching and executing commands based on the value of a variable. It allows you to perform different actions depending on the input, making it a powerful tool for scripting and automation.

## Usage
The basic syntax of the `case` command is as follows:

```csh
case expression in
    pattern1) command1 ;;
    pattern2) command2 ;;
    ...
    *) default_command ;;
end
```

## Common Options
The `case` command does not have specific options like many other commands. Instead, it relies on patterns and commands defined within its structure. Here are the components you will typically use:

- `expression`: The variable or value to be matched against patterns.
- `pattern`: The pattern to match the expression. It can include wildcards like `*` and `?`.
- `command`: The command to execute if the pattern matches.
- `*`: A catch-all pattern that matches anything not previously matched.

## Common Examples

### Example 1: Basic Pattern Matching
```csh
set fruit = "apple"
case $fruit in
    apple) echo "It's an apple!" ;;
    banana) echo "It's a banana!" ;;
    *) echo "Unknown fruit." ;;
end
```

### Example 2: Using Wildcards
```csh
set file = "report_2023.txt"
case $file in
    report_*.txt) echo "It's a report file." ;;
    *) echo "Not a report file." ;;
end
```

### Example 3: Multiple Patterns
```csh
set color = "red"
case $color in
    red|blue) echo "It's a primary color." ;;
    green) echo "It's a secondary color." ;;
    *) echo "Unknown color." ;;
end
```

## Tips
- Use wildcards effectively to match multiple patterns with a single case statement.
- Always include a default case (`*`) to handle unexpected values and avoid silent failures.
- Keep your patterns and commands organized for better readability, especially in complex scripts.