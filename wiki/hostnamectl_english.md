# [Linux] C Shell (csh) hostnamectl用法: Manage system hostname and related settings

## Overview
The `hostnamectl` command is used to manage the system hostname and related settings in Linux. It allows users to view and change the hostname, as well as configure other related parameters such as the static hostname, transient hostname, and pretty hostname.

## Usage
The basic syntax of the `hostnamectl` command is as follows:

```bash
hostnamectl [options] [arguments]
```

## Common Options
- `set-hostname`: Set the system's hostname.
- `set-icon-name`: Set the icon name for the system.
- `set-chassis`: Set the chassis type of the system.
- `status`: Show the current hostname and related settings.
- `help`: Display help information about the command.

## Common Examples
- **View current hostname and settings:**
  ```bash
  hostnamectl status
  ```

- **Set a new static hostname:**
  ```bash
  hostnamectl set-hostname my-new-hostname
  ```

- **Set a pretty hostname:**
  ```bash
  hostnamectl set-hostname "My New Hostname" --pretty
  ```

- **Set the chassis type to 'desktop':**
  ```bash
  hostnamectl set-chassis desktop
  ```

## Tips
- Always check the current hostname with `hostnamectl status` before making changes.
- Use quotes around hostnames that contain spaces or special characters.
- Remember that changing the hostname may require a restart or re-login to take full effect.