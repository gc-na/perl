# [Unix] C Shell (csh) popd用法: Manage directory stack

## Overview
The `popd` command in C Shell (csh) is used to remove the top directory from the directory stack and change the current directory to that directory. It is particularly useful for navigating back to previously visited directories without needing to type the full path.

## Usage
The basic syntax of the `popd` command is as follows:

```csh
popd [options]
```

## Common Options
- `-n`: This option allows you to display the directory stack without changing the current directory.
- `+n`: This option allows you to pop a directory from a specific position in the stack, where `n` is the index of the directory (starting from 0 for the top of the stack).
- `-n`: Similar to `+n`, but it pops the directory from the end of the stack.

## Common Examples
Here are some practical examples of using the `popd` command:

1. **Basic Usage**: Return to the previous directory.
   ```csh
   popd
   ```

2. **Using with Directory Stack**: If you have navigated to multiple directories, you can pop back to the last one.
   ```csh
   pushd /path/to/first-directory
   pushd /path/to/second-directory
   popd
   ```

3. **Popping from a Specific Position**: If you want to pop a directory from a specific position in the stack.
   ```csh
   pushd /path/to/first-directory
   pushd /path/to/second-directory
   pushd /path/to/third-directory
   popd +1  # Pops the second directory in the stack
   ```

4. **Display Stack without Changing Directory**: To view the current directory stack without changing the directory.
   ```csh
   popd -n
   ```

## Tips
- Always check your directory stack with the `dirs` command before using `popd` to ensure you're aware of your current position.
- Combine `pushd` and `popd` for efficient directory navigation, especially in scripts or when working on complex projects.
- Remember that the directory stack is maintained only for the current shell session; it will reset when you start a new session.