# [Unix] C Shell (csh) id <Usage equivalent in English>: Display user and group information

## Overview
The `id` command in C Shell (csh) is used to display the user ID (UID) and group ID (GID) of the current user, as well as the groups to which the user belongs. This command is useful for understanding user permissions and group memberships in a Unix-like environment.

## Usage
The basic syntax of the `id` command is as follows:

```
id [options] [arguments]
```

## Common Options
- `-u`: Display only the effective user ID.
- `-g`: Display only the effective group ID.
- `-G`: Display all group IDs for the user.
- `-n`: Display the name instead of the numeric ID.

## Common Examples

1. **Display user and group information:**
   ```csh
   id
   ```

2. **Display only the effective user ID:**
   ```csh
   id -u
   ```

3. **Display only the effective group ID:**
   ```csh
   id -g
   ```

4. **Display all group IDs for the user:**
   ```csh
   id -G
   ```

5. **Display the user name instead of the numeric user ID:**
   ```csh
   id -n
   ```

## Tips
- Use `id` without any options to get a quick overview of your user and group information.
- Combine options to tailor the output to your needs, such as `id -Gn` to get group names instead of IDs.
- Remember that the `id` command can also be used with a username as an argument to check the information for a different user, e.g., `id username`.