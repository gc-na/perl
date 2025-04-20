# [Linux] C Shell (csh) switch用法: Conditional branching in scripts

## Overview
The `switch` command in C Shell (csh) is used for conditional branching, allowing users to execute different blocks of code based on the value of a variable. It simplifies the process of making decisions in scripts by providing a cleaner syntax compared to multiple `if` statements.

## Usage
The basic syntax of the `switch` command is as follows:

```csh
switch (expression)
    case pattern1:
        commands
        breaksw
    case pattern2:
        commands
        breaksw
    default:
        commands
        breaksw
endsw
```

## Common Options
- `case pattern:`: Defines a pattern to match against the expression.
- `breaksw`: Exits the `switch` block after executing the matched case.
- `default:`: A fallback case that executes if no patterns match.

## Common Examples

### Example 1: Basic Switch Statement
```csh
set color = "red"
switch ($color)
    case "red":
        echo "Color is red"
        breaksw
    case "blue":
        echo "Color is blue"
        breaksw
    default:
        echo "Color is unknown"
        breaksw
endsw
```

### Example 2: Matching Multiple Patterns
```csh
set fruit = "apple"
switch ($fruit)
    case "apple":
    case "banana":
        echo "This is a fruit"
        breaksw
    default:
        echo "Not a fruit"
        breaksw
endsw
```

### Example 3: Using Default Case
```csh
set day = "Monday"
switch ($day)
    case "Saturday":
        echo "It's the weekend!"
        breaksw
    case "Sunday":
        echo "It's the weekend!"
        breaksw
    default:
        echo "It's a weekday."
        breaksw
endsw
```

## Tips
- Always include a `default` case to handle unexpected values.
- Use `breaksw` to prevent fall-through behavior, ensuring only the matched case executes.
- Keep your patterns simple and clear for better readability and maintenance of your scripts.