<!--
Meta Description: # Understanding `wantarray` in Perl: A Guide to Contextual Return Values ## Synopsis `wantarray` is a built-in Perl function that determines the conte...
Meta Keywords: context, wantarray, return, scalar, list
-->

# Understanding `wantarray` in Perl: A Guide to Contextual Return Values

## Synopsis
`wantarray` is a built-in Perl function that determines the context in which a subroutine is called, allowing developers to return different values based on whether the calling context is scalar, list, or void.

## Documentation

### Purpose
The `wantarray` function is primarily used within subroutines to assess how the subroutine was invoked. It helps in providing context-sensitive return values: returning a list when called in list context, a single scalar when called in scalar context, or performing no action when called in void context.

### Usage
To use `wantarray`, simply call it within a subroutine. It returns:
- `true` (a defined value) if the calling context is a list context.
- `false` (undef) if the calling context is void.
- `0` if the calling context is scalar.

Here’s the syntax:
```perl
sub example {
    if (wantarray) {
        return (1, 2, 3);  # List context
    } elsif (defined wantarray) {
        return 42;         # Scalar context
    }
    # Void context: Do nothing
}
```

### Details
In Perl, context is important for understanding how values are treated. The three primary contexts are:
- **List Context**: Used when a subroutine is expected to return multiple values.
- **Scalar Context**: Used when a subroutine is expected to return a single value.
- **Void Context**: Used when the return value is not needed.

`wantarray` helps in writing versatile subroutines that can adapt their outputs based on how they are called.

## Examples

### Example 1: Returning Different Values Based on Context
```perl
sub context_example {
    if (wantarray) {
        return (1, 2, 3);  # Returns a list
    } elsif (defined wantarray) {
        return 100;        # Returns a single scalar
    }
    # No return value in void context
}

my @list = context_example();  # @list will contain (1, 2, 3)
my $scalar = context_example(); # $scalar will be 100
context_example();               # No value returned
```

### Example 2: Using `wantarray` with `map`
```perl
sub process_data {
    my @data = (1, 2, 3);
    if (wantarray) {
        return map { $_ * 2 } @data;  # Returns (2, 4, 6) in list context
    } elsif (defined wantarray) {
        return scalar(@data) * 2;     # Returns 6 in scalar context
    }
}

my @result = process_data();       # @result = (2, 4, 6)
my $count = process_data();        # $count = 6
```

## Explanation
### Common Pitfalls
- **Forgetting to Check Context**: Not using `wantarray` when a subroutine can be called in different contexts may lead to unexpected results.
- **Confusing Scalar and List Context**: Developers may mistakenly assume that a subroutine called in list context will always return a single value, leading to bugs in their programs.

### Additional Notes
- `wantarray` is particularly useful in library and utility functions where flexibility in return types can significantly enhance usability.
- It’s important to note that there is no need to call `wantarray` in every subroutine; it is only necessary when the context is critical to the function's operation.

## One Line Summary
`wantarray` is a Perl built-in function that checks the calling context of a subroutine to enable context-sensitive return values.