# [Linux] C Shell (csh) nslookup Uso: Query DNS information

## Overview
The `nslookup` command is a network utility used to query the Domain Name System (DNS) to obtain domain name or IP address mapping information. It helps in troubleshooting DNS-related issues by allowing users to look up DNS records for specific domains.

## Usage
The basic syntax of the `nslookup` command is as follows:

```
nslookup [options] [arguments]
```

## Common Options
- `-type=TYPE`: Specify the type of DNS record to query (e.g., A, AAAA, MX, etc.).
- `-timeout=seconds`: Set the time to wait for a response from the DNS server.
- `-port=port`: Specify the port number to use for the DNS query (default is 53).
- `-debug`: Enable debugging output to help diagnose issues.

## Common Examples
Here are several practical examples of using the `nslookup` command:

1. **Basic Domain Lookup**
   ```
   nslookup example.com
   ```

2. **Lookup a Specific Record Type (MX)**
   ```
   nslookup -type=MX example.com
   ```

3. **Query a Specific DNS Server**
   ```
   nslookup example.com 8.8.8.8
   ```

4. **Set a Custom Timeout**
   ```
   nslookup -timeout=5 example.com
   ```

5. **Debugging Output**
   ```
   nslookup -debug example.com
   ```

## Tips
- Always specify the type of record you are interested in for more precise results.
- Use a reliable DNS server (like Google’s 8.8.8.8) for queries to avoid issues with your local DNS.
- If you encounter issues, the `-debug` option can provide valuable insights into what might be going wrong.