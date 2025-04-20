# [台灣] C Shell (csh) tmux 使用法: 多工終端管理工具

## Overview
tmux 是一個終端多工管理器，允許使用者在單一窗口中運行多個會話。它可以讓你分割窗口、創建新會話，並在不同的會話之間輕鬆切換，特別適合需要同時監控多個任務的使用者。

## Usage
基本語法如下：
```csh
tmux [options] [arguments]
```

## Common Options
- `new`: 創建一個新的 tmux 會話。
- `attach`: 附加到已存在的 tmux 會話。
- `detach`: 從當前會話中分離。
- `list-sessions`: 列出所有的 tmux 會話。
- `kill-session`: 終止指定的 tmux 會話。

## Common Examples
- 創建新的 tmux 會話：
  ```csh
  tmux new -s mysession
  ```
- 附加到已存在的會話：
  ```csh
  tmux attach -t mysession
  ```
- 分離當前會話：
  ```csh
  Ctrl-b d
  ```
- 列出所有的 tmux 會話：
  ```csh
  tmux list-sessions
  ```
- 終止指定的會話：
  ```csh
  tmux kill-session -t mysession
  ```

## Tips
- 使用 `Ctrl-b` 作為預設的前綴鍵，可以讓你執行 tmux 的各種命令。
- 嘗試使用窗口分割功能，讓你可以同時查看多個終端輸出。
- 定期保存你的 tmux 配置，以便在需要時快速恢復工作環境。