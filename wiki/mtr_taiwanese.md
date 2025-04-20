# [台灣] C Shell (csh) mtr 使用方法: 網路路徑追蹤工具

## Overview
mtr（My Traceroute）是一個結合了 ping 和 traceroute 功能的網路診斷工具。它可以用來追蹤數據包在網路中的路徑，並顯示每一跳的延遲和丟包情況，幫助用戶分析網路連接的質量。

## Usage
基本語法如下：
```
mtr [options] [arguments]
```

## Common Options
- `-r`：以報告模式運行，顯示一個簡短的報告。
- `-c <count>`：指定發送的探測包數量。
- `-i <interval>`：設置發送探測包的間隔時間（以秒為單位）。
- `-p`：顯示每一跳的端口號。
- `-n`：不解析主機名稱，僅顯示 IP 地址。

## Common Examples
以下是一些常見的使用範例：

1. 基本使用，追蹤到指定主機：
   ```bash
   mtr example.com
   ```

2. 以報告模式運行，並限制發送 10 個包：
   ```bash
   mtr -r -c 10 example.com
   ```

3. 設定每 2 秒發送一次探測包：
   ```bash
   mtr -i 2 example.com
   ```

4. 顯示每一跳的端口號：
   ```bash
   mtr -p example.com
   ```

5. 僅顯示 IP 地址，不解析主機名稱：
   ```bash
   mtr -n example.com
   ```

## Tips
- 在進行網路故障排除時，使用 `-r` 選項可以快速獲得報告，便於分析。
- 嘗試不同的 `-c` 和 `-i` 值，以獲得更精確的延遲和丟包數據。
- 使用 `-n` 選項可以加快顯示速度，特別是在 DNS 解析較慢的情況下。