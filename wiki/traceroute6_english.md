# [Linux] C Shell (csh) traceroute6用法: Trace IPv6 Network Paths

## Overview
The `traceroute6` command is used to trace the route that packets take to reach a specified destination over an IPv6 network. It helps in diagnosing network issues by showing the path and measuring transit delays of packets across the network.

## Usage
The basic syntax of the `traceroute6` command is as follows:

```bash
traceroute6 [options] [arguments]
```

## Common Options
- `-m <max_ttl>`: Set the maximum time-to-live (TTL) for the packets.
- `-n`: Show numerical addresses instead of resolving hostnames.
- `-p <port>`: Specify the destination port number to use.
- `-w <timeout>`: Set the timeout for each probe in seconds.

## Common Examples
Here are some practical examples of using the `traceroute6` command:

1. **Basic traceroute to an IPv6 address:**
   ```bash
   traceroute6 2001:db8::1
   ```

2. **Traceroute with a maximum TTL of 30:**
   ```bash
   traceroute6 -m 30 2001:db8::1
   ```

3. **Traceroute showing numerical addresses only:**
   ```bash
   traceroute6 -n 2001:db8::1
   ```

4. **Traceroute to a specific port:**
   ```bash
   traceroute6 -p 80 2001:db8::1
   ```

5. **Traceroute with a custom timeout of 2 seconds:**
   ```bash
   traceroute6 -w 2 2001:db8::1
   ```

## Tips
- Always use the `-n` option if you want faster results, as it avoids DNS lookups.
- Adjust the `-m` option based on your network's expected hop count to avoid unnecessary probes.
- Use `traceroute6` in combination with other network diagnostic tools like `ping` for comprehensive troubleshooting.