# [Linux] C Shell (csh) mtr Uso: Combina traceroute y ping

## Overview
The `mtr` command, short for "My Traceroute," is a network diagnostic tool that combines the functionalities of the `ping` and `traceroute` commands. It provides real-time analysis of the route packets take to a network host, helping users identify network issues and latency.

## Usage
The basic syntax of the `mtr` command is as follows:

```
mtr [options] [hostname]
```

## Common Options
- `-r`: Run in report mode, which provides a summary of the results.
- `-c <count>`: Set the number of pings to send.
- `-i <interval>`: Specify the interval between pings in seconds.
- `-p`: Show the port number in the output.
- `-n`: Show numerical addresses instead of resolving hostnames.

## Common Examples
Here are some practical examples of using the `mtr` command:

1. **Basic usage to check a host:**
   ```shell
   mtr example.com
   ```

2. **Run in report mode for a summary:**
   ```shell
   mtr -r example.com
   ```

3. **Send a specific number of pings:**
   ```shell
   mtr -c 10 example.com
   ```

4. **Set a custom interval between pings:**
   ```shell
   mtr -i 2 example.com
   ```

5. **Display numerical addresses only:**
   ```shell
   mtr -n example.com
   ```

## Tips
- Use `mtr` with the `-r` option for a quick summary of the network path without continuous output.
- Combine the `-c` option with `-r` to limit the number of pings and get a concise report.
- If you are troubleshooting a slow connection, consider using the `-i` option to adjust the interval for more detailed analysis.