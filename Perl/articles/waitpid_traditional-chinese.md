<!--
Meta Description: # waitpid 在 Perl 中的使用指南 ## 概述 `waitpid` 是 Perl 中的一個系統調用，用於等待特定子進程的結束，並獲取其退出狀態。這對於進程管理和資源釋放至關重要。 ## 文件說明 `waitpid` 函數的主要目的是讓父進程等待指定的子進程結束。這樣做可以防止產生孤兒進程...
Meta Keywords: pid, waitpid, child_pid, perl, wnohang
-->

# waitpid 在 Perl 中的使用指南

## 概述
`waitpid` 是 Perl 中的一個系統調用，用於等待特定子進程的結束，並獲取其退出狀態。這對於進程管理和資源釋放至關重要。

## 文件說明
`waitpid` 函數的主要目的是讓父進程等待指定的子進程結束。這樣做可以防止產生孤兒進程，並能夠收集子進程的退出狀態。

### 語法
```perl
$pid = waitpid($pid, $options);
```

- **$pid**: 要等待的子進程的進程ID。如果 `-1` 被傳入，則等待任何子進程結束。
- **$options**: 控制等待行為的選項，通常為 `0` 或 `WNOHANG`。`0` 意味著父進程會阻塞直到子進程結束，而 `WNOHANG` 則使父進程不會阻塞，立即返回。

### 返回值
- 返回值為結束的子進程的進程ID。如果沒有符合條件的子進程，則返回 `-1`。若發生錯誤，則返回 `-1` 並設置 `$!`。

## 範例
### 基本使用範例
```perl
use strict;
use warnings;

my $pid = fork();

if ($pid) {
    # 父進程
    my $child_pid = waitpid($pid, 0);
    print "Child process $child_pid has finished.\n";
} elsif (defined $pid) {
    # 子進程
    sleep(2);  # 模擬一些工作
    exit(0);
} else {
    die "Fork failed: $!";
}
```

### 非阻塞等待子進程
```perl
use strict;
use warnings;

my $pid = fork();

if ($pid) {
    # 父進程
    while (1) {
        my $child_pid = waitpid($pid, WNOHANG);
        if ($child_pid == 0) {
            print "Child is still running...\n";
            sleep(1);
        } elsif ($child_pid == $pid) {
            print "Child process $child_pid has finished.\n";
            last;
        } elsif ($child_pid == -1) {
            print "No child process found.\n";
            last;
        }
    }
} elsif (defined $pid) {
    # 子進程
    sleep(5);  # 模擬一些工作
    exit(0);
} else {
    die "Fork failed: $!";
}
```

## 解釋
在使用 `waitpid` 時，需注意以下事項：

1. **子進程存在性**：如果父進程調用 `waitpid` 時，子進程已經結束，則可能會立即返回。
2. **錯誤處理**：使用 `waitpid` 時，需檢查返回值，以確保正確處理進程終止狀態。
3. **選項選擇**：使用 `WNOHANG` 時，父進程不會被阻塞，這在需要保持界面響應性時非常有用。

## 一句話總結
`waitpid` 是 Perl 中用於等待特定子進程結束的函數，能有效管理進程和資源。