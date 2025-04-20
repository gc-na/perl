# [Unix] C Shell (csh) if: Conditional execution of commands

## Overview
The `if` command in C Shell (csh) is used to execute commands based on the evaluation of a condition. It allows scripts to make decisions and perform different actions depending on whether certain conditions are true or false.

## Usage
The basic syntax of the `if` command is as follows:

```csh
if (condition) then
    command1
else
    command2
endif
```

## Common Options
- `then`: Indicates the start of the commands to be executed if the condition is true.
- `else`: Specifies the commands to be executed if the condition is false.
- `endif`: Marks the end of the `if` statement.

## Common Examples

### Example 1: Simple Condition Check
Check if a file exists and print a message accordingly.

```csh
if (-e myfile.txt) then
    echo "File exists."
else
    echo "File does not exist."
endif
```

### Example 2: Numeric Comparison
Compare two numbers and print which one is greater.

```csh
set num1 = 10
set num2 = 20

if ($num1 > $num2) then
    echo "$num1 is greater than $num2."
else
    echo "$num2 is greater than or equal to $num1."
endif
```

### Example 3: String Comparison
Check if two strings are equal.

```csh
set str1 = "hello"
set str2 = "world"

if ("$str1" == "$str2") then
    echo "Strings are equal."
else
    echo "Strings are not equal."
endif
```

## Tips
- Always ensure that conditions are enclosed in parentheses.
- Use proper indentation for better readability of nested `if` statements.
- Remember to use `endif` to close the `if` block; otherwise, you may encounter syntax errors.