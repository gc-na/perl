# [Unix] C Shell (csh) expr 用法: Evaluate expressions and perform calculations

## Overview
The `expr` command in C Shell (csh) is used to evaluate expressions and perform basic arithmetic operations. It can handle integer arithmetic, string operations, and logical comparisons, making it a versatile tool for scripting and command-line tasks.

## Usage
The basic syntax of the `expr` command is as follows:

```csh
expr [options] [arguments]
```

## Common Options
- `+` : Addition of two numbers.
- `-` : Subtraction of two numbers.
- `*` : Multiplication of two numbers (note that `*` must be escaped or quoted).
- `/` : Division of two numbers.
- `%` : Modulus operation (remainder of division).
- `=` : String comparison for equality.
- `!=` : String comparison for inequality.
- `>` : Greater than comparison.
- `<` : Less than comparison.
- `>=` : Greater than or equal to comparison.
- `<=` : Less than or equal to comparison.

## Common Examples

1. **Basic Arithmetic Addition**
   ```csh
   expr 5 + 3
   ```
   This command outputs `8`, which is the result of adding 5 and 3.

2. **Subtraction**
   ```csh
   expr 10 - 4
   ```
   The output will be `6`, the result of subtracting 4 from 10.

3. **Multiplication**
   ```csh
   expr 7 \* 6
   ```
   This will give `42`. Note the backslash before the asterisk to prevent shell interpretation.

4. **Division**
   ```csh
   expr 20 / 4
   ```
   The output is `5`, the result of dividing 20 by 4.

5. **Modulus**
   ```csh
   expr 10 % 3
   ```
   This command returns `1`, which is the remainder of dividing 10 by 3.

6. **String Comparison**
   ```csh
   expr "hello" = "hello"
   ```
   This will output `1`, indicating that the two strings are equal.

7. **Logical Comparison**
   ```csh
   expr 5 \> 3
   ```
   The output will be `1`, meaning that 5 is greater than 3.

## Tips
- Always escape the multiplication operator (`*`) to avoid shell interpretation issues.
- Use parentheses for complex expressions to ensure the correct order of operations.
- Remember that `expr` only works with integers; for floating-point arithmetic, consider using other tools like `bc`.
- When using string comparisons, ensure that the strings are enclosed in quotes to avoid unexpected results.