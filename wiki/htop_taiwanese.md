# [台灣] C Shell (csh) htop 使用法: 系統監控工具

## Overview
htop 是一個互動式的系統監控工具，能夠顯示系統的運行狀態，包括 CPU 使用率、記憶體使用情況和正在運行的進程。與傳統的 top 命令相比，htop 提供了更友好的界面和更多的功能。

## Usage
基本語法如下：
```csh
htop [options] [arguments]
```

## Common Options
- `-d <delay>`: 設定更新的延遲時間（以秒為單位）。
- `-u <user>`: 僅顯示指定用戶的進程。
- `-p <pid>`: 僅顯示指定進程的詳細信息。
- `--sort-key <key>`: 設定排序的依據，例如 CPU 或記憶體使用率。

## Common Examples
- 啟動 htop：
```csh
htop
```

- 設定更新延遲為 2 秒：
```csh
htop -d 2
```

- 僅顯示用戶 "john" 的進程：
```csh
htop -u john
```

- 僅顯示進程 ID 為 1234 的進程：
```csh
htop -p 1234
```

- 使用 CPU 使用率排序：
```csh
htop --sort-key PERCENT_CPU
```

## Tips
- 使用方向鍵來導航進程列表，並按 `F9` 來終止選中的進程。
- 可以按 `F2` 進入設置菜單，調整顯示選項以符合你的需求。
- 利用 `F3` 和 `F4` 來搜尋和過濾進程，這對於管理大量進程時非常有用。