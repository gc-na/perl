# [Linux] C Shell (csh) modprobe用法: Load kernel modules

## Overview
The `modprobe` command is used in Linux to load and unload kernel modules. It intelligently manages module dependencies, ensuring that all required modules are loaded when a specific module is requested.

## Usage
The basic syntax of the `modprobe` command is as follows:

```bash
modprobe [options] [arguments]
```

## Common Options
- `-r`, `--remove`: Unload a module.
- `-n`, `--dry-run`: Show what would be done without actually performing the action.
- `-v`, `--verbose`: Provide more detailed output during execution.
- `--show-depends`: Display the dependencies of the specified module.

## Common Examples
Here are some practical examples of using the `modprobe` command:

1. **Load a Module**
   To load a module, such as `dummy`, you can use:
   ```bash
   modprobe dummy
   ```

2. **Unload a Module**
   To unload the same module, you would use:
   ```bash
   modprobe -r dummy
   ```

3. **Check Module Dependencies**
   To see the dependencies for a specific module, use:
   ```bash
   modprobe --show-depends dummy
   ```

4. **Dry Run Loading a Module**
   To simulate loading a module without actually doing it, run:
   ```bash
   modprobe -n dummy
   ```

5. **Verbose Loading of a Module**
   To load a module with detailed output, use:
   ```bash
   modprobe -v dummy
   ```

## Tips
- Always check for dependencies using `--show-depends` before loading a module to avoid issues.
- Use the `-n` option to test commands before executing them, especially in critical systems.
- Keep your kernel modules updated to ensure compatibility with the latest kernel version.