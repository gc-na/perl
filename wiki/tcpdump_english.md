# [Linux] C Shell (csh) tcpdump用法: Capture network packets

## Overview
The `tcpdump` command is a powerful network packet analyzer that allows users to capture and display the packets being transmitted or received over a network to which the computer is attached. It is widely used for network troubleshooting, analysis, and security auditing.

## Usage
The basic syntax of the `tcpdump` command is as follows:

```bash
tcpdump [options] [arguments]
```

## Common Options
- `-i <interface>`: Specify the network interface to listen on (e.g., `eth0`).
- `-n`: Do not resolve hostnames; display IP addresses instead.
- `-v`: Enable verbose output; provides more details about the packets.
- `-c <count>`: Capture only a specified number of packets.
- `-w <file>`: Write the captured packets to a file instead of displaying them on the screen.
- `-r <file>`: Read packets from a file instead of capturing them live.

## Common Examples
- Capture packets on the default network interface:
  ```bash
  tcpdump
  ```

- Capture packets on a specific interface (e.g., `eth0`):
  ```bash
  tcpdump -i eth0
  ```

- Capture and display packets without resolving hostnames:
  ```bash
  tcpdump -n
  ```

- Capture only 10 packets:
  ```bash
  tcpdump -c 10
  ```

- Write captured packets to a file named `capture.pcap`:
  ```bash
  tcpdump -w capture.pcap
  ```

- Read packets from a previously saved file:
  ```bash
  tcpdump -r capture.pcap
  ```

## Tips
- Always run `tcpdump` with appropriate permissions (often requires root access).
- Use filters to limit the output to specific traffic (e.g., `tcpdump port 80` to capture only HTTP traffic).
- Analyze captured packets with tools like Wireshark for a more user-friendly interface.
- Be cautious when capturing packets in a production environment, as it may impact performance.