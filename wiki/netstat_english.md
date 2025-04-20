# [Linux] C Shell (csh) netstat Uso: Display network connections and statistics

## Overview
The `netstat` command is a powerful tool used to display network connections, routing tables, interface statistics, and more. It helps users monitor network activity and diagnose network issues.

## Usage
The basic syntax of the `netstat` command is as follows:

```
netstat [options] [arguments]
```

## Common Options
- `-a`: Show all active connections and listening ports.
- `-n`: Display addresses and port numbers in numerical form rather than resolving them to hostnames.
- `-r`: Display the routing table.
- `-i`: Show network interface statistics.
- `-p`: Show the process ID and name associated with each connection.

## Common Examples
Here are some practical examples of using the `netstat` command:

1. **Display all active connections:**
   ```csh
   netstat -a
   ```

2. **Show active connections with numerical addresses:**
   ```csh
   netstat -an
   ```

3. **View the routing table:**
   ```csh
   netstat -r
   ```

4. **List network interface statistics:**
   ```csh
   netstat -i
   ```

5. **Show connections along with the associated process IDs:**
   ```csh
   netstat -p
   ```

## Tips
- Use the `-n` option to speed up the output by avoiding DNS lookups, especially useful on busy networks.
- Combine options for more detailed output, such as `netstat -anp` to see all connections with process information.
- Regularly check your network connections to identify any unauthorized access or unusual activity.