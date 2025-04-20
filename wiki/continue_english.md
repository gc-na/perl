# [Unix] C Shell (csh) continue 用法等价: Resume execution of a loop

## Overview
The `continue` command in C Shell (csh) is used within loops to skip the remaining commands in the current iteration and proceed to the next iteration of the loop. This is particularly useful when you want to bypass certain conditions without terminating the entire loop.

## Usage
The basic syntax of the `continue` command is as follows:

```csh
continue [n]
```

Here, `n` is an optional argument that specifies how many levels of nested loops to continue. If `n` is not provided, it defaults to 1, meaning it will continue the innermost loop.

## Common Options
- `n`: Specifies the number of nested loops to continue. If you have multiple nested loops, you can use this option to skip to the next iteration of a specific loop level.

## Common Examples

### Example 1: Basic usage in a loop
In this example, the loop iterates through numbers 1 to 5, but skips the number 3.

```csh
foreach i (1 2 3 4 5)
    if ($i == 3) then
        continue
    endif
    echo $i
end
```
**Output:**
```
1
2
4
5
```

### Example 2: Continuing a nested loop
Here’s an example with nested loops where we skip the inner loop when `j` is 2.

```csh
foreach i (1 2)
    foreach j (1 2 3)
        if ($j == 2) then
            continue 2
        endif
        echo "$i $j"
    end
end
```
**Output:**
```
1 1
1 3
2 1
2 3
```

### Example 3: Using `continue` with a condition
In this example, we only print even numbers from 1 to 10.

```csh
foreach i (1 2 3 4 5 6 7 8 9 10)
    if ($i % 2 != 0) then
        continue
    endif
    echo $i
end
```
**Output:**
```
2
4
6
8
10
```

## Tips
- Use `continue` to make your loops cleaner by avoiding deeply nested `if` statements.
- Always ensure that the condition for `continue` is clearly defined to avoid skipping unintended iterations.
- When using nested loops, specify the correct level with `n` to avoid confusion about which loop is being continued.