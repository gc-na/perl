# [Linux] C Shell (csh) timedatectl用法: Manage system time and date settings

## Overview
The `timedatectl` command is used to query and change the system clock and its settings in Linux. It allows users to manage time zones, synchronize the system clock with network time servers, and display the current time and date settings.

## Usage
The basic syntax of the `timedatectl` command is as follows:

```bash
timedatectl [options] [arguments]
```

## Common Options
- `status`: Displays the current time, date, and time zone settings.
- `set-time <time>`: Sets the system clock to a specified time.
- `set-timezone <timezone>`: Changes the system's time zone.
- `set-ntp <boolean>`: Enables or disables NTP (Network Time Protocol) synchronization.
- `list-timezones`: Lists all available time zones.

## Common Examples
Here are some practical examples of using the `timedatectl` command:

### 1. Display Current Time and Date
To check the current system time and date settings, use:

```bash
timedatectl status
```

### 2. Set the System Time
To set the system time to a specific value, for example, `2023-10-01 12:00:00`, use:

```bash
timedatectl set-time '2023-10-01 12:00:00'
```

### 3. Change the Time Zone
To change the system's time zone to `America/New_York`, use:

```bash
timedatectl set-timezone America/New_York
```

### 4. Enable NTP Synchronization
To enable automatic time synchronization with NTP servers, use:

```bash
timedatectl set-ntp true
```

### 5. List Available Time Zones
To see a list of all available time zones, use:

```bash
timedatectl list-timezones
```

## Tips
- Always check the current time and date settings before making changes to avoid confusion.
- Use the `list-timezones` option to find the correct time zone string for your location.
- Ensure you have the necessary permissions (usually root) to change system time settings.