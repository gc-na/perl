<!--
Meta Description: # Understanding the Perl `map` Function: Syntax, Usage, and Examples ## Synopsis The `map` function in Perl is a powerful built-in feature that transf...
Meta Keywords: map, list, block, perl, expression
-->

# Understanding the Perl `map` Function: Syntax, Usage, and Examples

## Synopsis
The `map` function in Perl is a powerful built-in feature that transforms a list by applying a specified block of code or expression to each element, returning a new list containing the results.

## Documentation
The `map` function is used for transforming lists in Perl. It takes a block of code or an expression and applies it to each element of a list, producing a new list. The syntax is as follows:

```perl
my @new_list = map { BLOCK } @original_list;
```

Or, using an expression instead of a block:

```perl
my @new_list = map EXPR, @original_list;
```

### Purpose
The main purpose of `map` is to facilitate the transformation of data. It is particularly useful for applying operations like modifying strings, changing data formats, or filtering values in a concise manner.

### Usage
- **Block Form**: When using a block, you define the code to be executed for each element within curly braces `{}`.
- **Expression Form**: You can also provide a single expression that will be evaluated for each element in the list.

### Details
`map` iterates over the input list and evaluates the provided code or expression for each element. It returns a new list composed of the results of these evaluations. It is important to note that `map` does not modify the original list; it creates a new one instead.

### Important Points:
- If the input list is empty, `map` will return an empty list.
- `map` is often used in combination with other functions for complex data processing tasks.

## Examples

### Basic Example
Transforming a list of numbers by squaring each value:

```perl
my @numbers = (1, 2, 3, 4);
my @squared = map { $_ ** 2 } @numbers;
print "@squared";  # Output: 1 4 9 16
```

### Using an Expression
Converting an array of strings to uppercase:

```perl
my @words = ('apple', 'banana', 'cherry');
my @uppercase = map { uc($_) } @words;
print "@uppercase";  # Output: APPLE BANANA CHERRY
```

### Filtering with `map`
Extracting the lengths of a list of strings:

```perl
my @fruits = ('apple', 'banana', 'kiwi');
my @lengths = map { length($_) } @fruits;
print "@lengths";  # Output: 5 6 4
```

## Explanation
While `map` is a straightforward function, there are common pitfalls users may encounter:
- **Misunderstanding Scope**: Variables defined inside the block are not accessible outside of it unless declared with `my`.
- **Returning Undefined**: If the block does not explicitly return a value, it may lead to unexpected results, especially when the block contains conditional logic.
- **Performance**: Using `map` on very large lists can have performance implications. In such cases, consider whether `grep` may be more suitable for filtering or if a simple loop would be more efficient.

## One Line Summary
The `map` function in Perl efficiently transforms lists by applying a block of code or expression to each element, returning a new list with the results.