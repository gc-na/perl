<!--
Meta Description: # Perl 中的 socketpair 函數：多用途的雙向通信管道 ## 摘要 `socketpair` 是 Perl 中一個用於創建一對連接的套接字的函數，主要用於進程間通信（IPC）。這個函數提供了一種高效的方式來在同一台機器上的不同進程之間進行數據交換。 ## 文檔 ### 目的 `sock...
Meta Keywords: socketpair, perl, child_socket, parent_socket, close
-->

# Perl 中的 socketpair 函數：多用途的雙向通信管道

## 摘要
`socketpair` 是 Perl 中一個用於創建一對連接的套接字的函數，主要用於進程間通信（IPC）。這個函數提供了一種高效的方式來在同一台機器上的不同進程之間進行數據交換。

## 文檔
### 目的
`socketpair` 函數用於創建一對雙向通信的套接字，這對套接字可以在同一台計算機的不同進程之間進行通信。它通常在需要兩個進程互相傳送信息時使用，比如在執行子進程時。

### 使用方法
語法如下：
```perl
socketpair(SOCKET1, SOCKET2, DOMAIN, TYPE, PROTOCOL);
```

- **SOCKET1** 和 **SOCKET2** 是將被創建的兩個套接字的標識符（句柄）。
- **DOMAIN** 是套接字的域，通常可以選擇 `AF_UNIX` 或 `AF_INET`。
- **TYPE** 是套接字的類型，通常使用 `SOCK_STREAM` 或 `SOCK_DGRAM`。
- **PROTOCOL** 是某些套接字類型的特定協議，通常設置為 0。

### 返回值
成功時，`socketpair` 返回 0，失敗時返回 -1 並通過 `$!` 獲取錯誤信息。

## 示例
### 基本用法
以下是一個簡單的示例，展示如何使用 `socketpair` 創建一對套接字並進行基本的數據傳輸：
```perl
use strict;
use warnings;
use IO::Socket;

my ($child_socket, $parent_socket);
socketpair($child_socket, $parent_socket, AF_UNIX, SOCK_STREAM) or die "socketpair: $!";

if (fork() == 0) {
    # 子進程
    close $parent_socket;
    print $child_socket "Hello from child process\n";
    close $child_socket;
    exit(0);
} else {
    # 父進程
    close $child_socket;
    my $response = <$parent_socket>;
    print "Received from child: $response";
    close $parent_socket;
}
```

## 解釋
在使用 `socketpair` 時，需要注意以下幾點：

1. **域限制**：`AF_UNIX` 只能用於同一台機器上的進程。因此，如果需要跨網絡進行通信，則應考慮使用 `AF_INET`。
2. **數據流方向**：`socketpair` 創建的套接字是全雙工的，這意味著兩個套接字可以同時進行讀寫操作，但在某些情況下可能會導致數據競爭。
3. **錯誤處理**：在使用 `socketpair` 時，要確保對返回值進行適當的錯誤檢查，特別是在生產環境中，以避免未處理的異常情況。

## 一句總結
`socketpair` 函數是 Perl 中用於創建一對雙向套接字的強大工具，方便進程間通信。