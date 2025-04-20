# [Linux] C Shell (csh) history 命令: View command history

## Overview
The `history` command in C Shell (csh) is used to display a list of previously executed commands in the current shell session. This allows users to easily recall and reuse commands without having to retype them.

## Usage
The basic syntax of the `history` command is as follows:

```csh
history [options] [arguments]
```

## Common Options
- `-c`: Clear the history list.
- `-n`: Read the history from the history file and append it to the current history list.
- `-r`: Read the history from the history file and replace the current history list.
- `-w`: Write the current history list to the history file.

## Common Examples

1. **Display the command history:**
   ```csh
   history
   ```

2. **Clear the command history:**
   ```csh
   history -c
   ```

3. **Read history from the history file:**
   ```csh
   history -r
   ```

4. **Write the current history to the history file:**
   ```csh
   history -w
   ```

5. **Display the last 10 commands:**
   ```csh
   history 10
   ```

## Tips
- Use `!n` to execute the command at position `n` in the history list.
- To quickly repeat the last command, simply type `!!`.
- Consider using `history -w` regularly to save your command history, especially before closing the terminal.