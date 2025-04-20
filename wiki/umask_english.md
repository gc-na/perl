# [Unix] C Shell (csh) umask Uso: Set file creation permissions

## Overview
The `umask` command in C Shell (csh) is used to set the default file creation permissions for new files and directories. It defines the permissions that will not be set on newly created files, effectively determining the default access rights.

## Usage
The basic syntax of the `umask` command is as follows:

```csh
umask [options] [arguments]
```

## Common Options
- `-S`: Display the current umask in symbolic format.
- `-p`: Print the current umask value without changing it.
- `numeric`: Set the umask value using a numeric mode (e.g., `022`).

## Common Examples
1. **Check the current umask value:**
   ```csh
   umask
   ```

2. **Set a new umask value:**
   ```csh
   umask 027
   ```
   This command sets the umask to `027`, which means new files will have permissions of `640` and new directories will have `750`.

3. **Display the umask in symbolic format:**
   ```csh
   umask -S
   ```

4. **Set umask to allow all permissions for the owner and read permissions for the group:**
   ```csh
   umask 007
   ```
   This sets the umask so that new files will have `660` permissions.

5. **Print the current umask value without changing it:**
   ```csh
   umask -p
   ```

## Tips
- Always check your current umask before setting a new one to avoid unintended permission issues.
- Use symbolic notation for easier readability when setting umask values.
- Remember that the umask value is subtracted from the default permissions (usually `666` for files and `777` for directories).