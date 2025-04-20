# [Linux] C Shell (csh) chage用法: Manage user password expiration settings

## Overview
The `chage` command is used to change user password expiry information in Linux systems. It allows administrators to set and manage password aging policies for user accounts, ensuring that users update their passwords regularly for security purposes.

## Usage
The basic syntax of the `chage` command is as follows:

```bash
chage [options] [username]
```

## Common Options
- `-l`: List the current password expiration information for the specified user.
- `-m`: Set the minimum number of days between password changes.
- `-M`: Set the maximum number of days a password is valid.
- `-I`: Set the number of days of inactivity before the account is disabled.
- `-E`: Set the date on which the user account will be disabled.

## Common Examples
Here are some practical examples of how to use the `chage` command:

1. **List password expiration information for a user:**
   ```bash
   chage -l username
   ```

2. **Set the minimum password age to 7 days:**
   ```bash
   chage -m 7 username
   ```

3. **Set the maximum password age to 90 days:**
   ```bash
   chage -M 90 username
   ```

4. **Set the account to expire after 30 days of inactivity:**
   ```bash
   chage -I 30 username
   ```

5. **Set the account to expire on a specific date (e.g., 2023-12-31):**
   ```bash
   chage -E 2023-12-31 username
   ```

## Tips
- Always check the current settings with the `-l` option before making changes to avoid unintended consequences.
- Consider setting a reminder for users to change their passwords as they approach the expiration date.
- Use the `-E` option carefully, as it can lock users out of their accounts if not managed properly.