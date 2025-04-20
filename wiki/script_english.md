# [Linux] C Shell (csh) script uso: Create a typescript of terminal session

## Overview
The `script` command in C Shell (csh) is used to create a typescript of your terminal session. This allows you to record all the input and output of your terminal session into a file, which can be useful for documentation, debugging, or sharing your work with others.

## Usage
The basic syntax of the `script` command is as follows:

```csh
script [options] [file]
```

## Common Options
- `-a`: Append the output to the specified file instead of overwriting it.
- `-q`: Run in quiet mode, suppressing the start and stop messages.
- `-t`: Record timing information for the session, which can be useful for playback.

## Common Examples
Here are some practical examples of using the `script` command:

1. **Basic usage**: Start recording your session to a file named `typescript`.
   ```csh
   script typescript
   ```

2. **Appending to an existing file**: Append the session output to an existing file.
   ```csh
   script -a typescript
   ```

3. **Quiet mode**: Record your session without displaying start and stop messages.
   ```csh
   script -q typescript
   ```

4. **Recording with timing**: Record your session along with timing information.
   ```csh
   script -t typescript
   ```

## Tips
- Always check the contents of your typescript file after your session to ensure everything was recorded as expected.
- Use the `-a` option if you want to keep adding to the same file over multiple sessions.
- Consider using `cat` or `less` to view your typescript file, especially if it contains a lot of output.