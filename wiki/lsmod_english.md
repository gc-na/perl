# [Linux] C Shell (csh) lsmod用法: Display loaded kernel modules

## Overview
The `lsmod` command in C Shell is used to display the currently loaded kernel modules in the Linux operating system. It provides a list of all modules that are currently active, along with their dependencies.

## Usage
The basic syntax of the `lsmod` command is as follows:

```csh
lsmod [options] [arguments]
```

## Common Options
While `lsmod` does not have many options, here are a couple of commonly used ones:

- `-h`, `--help`: Displays help information about the command.
- `-v`, `--version`: Shows the version of the `lsmod` command.

## Common Examples

1. **Display all loaded modules:**
   ```csh
   lsmod
   ```

2. **Display help information:**
   ```csh
   lsmod --help
   ```

3. **Show version of lsmod:**
   ```csh
   lsmod --version
   ```

## Tips
- Use `lsmod` in combination with other commands like `modinfo` to get detailed information about specific modules.
- Regularly check loaded modules to troubleshoot hardware issues or conflicts.
- Remember that `lsmod` only shows modules that are currently loaded; it does not list available modules that are not loaded.