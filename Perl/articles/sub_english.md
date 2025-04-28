<!--
Meta Description: # Understanding Perl's "sub" Keyword: Defining Subroutines ## Synopsis The `sub` keyword in Perl is used to define subroutines, which are reusable blo...
Meta Keywords: perl, sub, return, subroutine, subroutines
-->

# Understanding Perl's "sub" Keyword: Defining Subroutines

## Synopsis
The `sub` keyword in Perl is used to define subroutines, which are reusable blocks of code that perform specific tasks, helping to structure and organize code effectively.

## Documentation
In Perl, the `sub` keyword is integral for creating subroutines, allowing developers to encapsulate functionalities into manageable and reusable components. Subroutines can take parameters, return values, and help in reducing code duplication.

### Purpose
Subroutines serve to:
- Modularize code for better readability and maintenance.
- Allow code reuse across different parts of a program.
- Enable the creation of complex functions that can be broken down into simpler, manageable parts.

### Usage
The basic syntax for defining a subroutine with the `sub` keyword is as follows:

```perl
sub name_of_subroutine {
    # Code to be executed
}
```

To call a subroutine, use:

```perl
name_of_subroutine();
```

### Parameters and Return Values
Subroutines can accept parameters, which are accessed using the `@_` array. To return values, use the `return` statement.

Example of a subroutine with parameters and a return value:

```perl
sub add {
    my ($a, $b) = @_;
    return $a + $b;
}

my $result = add(5, 3); # $result will be 8
```

## Examples

### Basic Subroutine Definition
```perl
sub greet {
    print "Hello, World!\n";
}

greet(); # Outputs: Hello, World!
```

### Subroutine with Parameters
```perl
sub multiply {
    my ($x, $y) = @_;
    return $x * $y;
}

my $product = multiply(4, 5); # $product will be 20
```

### Subroutine Returning Multiple Values
```perl
sub divide {
    my ($num) = @_;
    return int($num / 2), $num % 2; # returns quotient and remainder
}

my ($quotient, $remainder) = divide(10); # $quotient will be 5, $remainder will be 0
```

## Explanation
While using subroutines, it's important to note a few common pitfalls:

- **Variable Scope**: Variables declared inside a subroutine are local to that subroutine unless explicitly marked as global using `our` or `use vars`.
- **Parameter Handling**: Always remember that subroutine parameters are passed via the `@_` array. Forgetting to dereference this can lead to unexpected results.
- **Returning Values**: If you want to return multiple values, ensure that they are returned in a list context. Simply using `return` without array context will lead to only the first value being returned.

Using `sub` effectively can streamline your Perl programming, enhance modularity, and improve code maintenance.

## One Line Summary
The `sub` keyword in Perl is used to define subroutines, enabling code modularity and reusability.