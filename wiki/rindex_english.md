<!--
Meta Description: # Understanding `rindex` in Perl: Searching for Substrings from the End ## Synopsis The `rindex` function in Perl is used to find the position of the ...
Meta Keywords: substring, string, rindex, position, index
-->

# Understanding `rindex` in Perl: Searching for Substrings from the End

## Synopsis
The `rindex` function in Perl is used to find the position of the last occurrence of a substring within a string, starting the search from the end of the string. It returns the index of the substring or `-1` if the substring is not found.

## Documentation
### Purpose
The `rindex` function provides a way to search for substrings in a string, specifically looking for the last occurrence. This is particularly useful when you want to perform operations based on the last appearance of a substring rather than the first.

### Usage
The syntax for using `rindex` is as follows:

```perl
rindex(STRING, SUBSTRING, [POSITION])
```

- **STRING**: The string in which you want to search for the substring.
- **SUBSTRING**: The substring you are searching for.
- **POSITION** (optional): The position in the string from which to start the search. The search begins from the end of the string, moving backwards towards the start.

### Return Value
- Returns the index (0-based) of the last occurrence of the substring.
- Returns `-1` if the substring is not found.

### Example
Here are a few examples to demonstrate the usage of `rindex`:

#### Example 1: Basic Usage
```perl
my $string = "Hello, world! Welcome to the world of Perl.";
my $substring = "world";
my $position = rindex($string, $substring);
print "The last occurrence of '$substring' is at index: $position\n";  
```
**Output:** `The last occurrence of 'world' is at index: 30`

#### Example 2: Using the Position Parameter
```perl
my $string = "abcdeabcde";
my $substring = "abc";
my $position = rindex($string, $substring, 7);
print "The last occurrence of '$substring' before index 7 is at index: $position\n";  
```
**Output:** `The last occurrence of 'abc' before index 7 is at index: 0`
  
## Explanation
### Common Pitfalls
- **Case Sensitivity**: The `rindex` function is case-sensitive. For example, searching for "World" will not match "world".
- **Negative Position**: If the `POSITION` parameter is negative, the search starts from the end of the string, which might yield unexpected results if the index is beyond the length of the string.

### Additional Notes
- `rindex` counts positions starting from 0, which means the first character is at index 0, the second at index 1, and so forth.
- If the substring is an empty string, `rindex` will return the position `0` as it is considered to be found at the beginning of the string.

## One Line Summary
The `rindex` function in Perl efficiently locates the last occurrence of a substring within a string, returning its index or `-1` if not found.