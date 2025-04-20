# [Linux] C Shell (csh) tmux 使用方法: 终端复用工具

## 概述
tmux 是一个终端复用工具，它允许用户在一个单一的窗口中管理多个终端会话。用户可以在不同的窗格中同时运行多个程序，方便进行多任务处理。

## 使用方法
tmux 的基本语法如下：

```bash
tmux [options] [arguments]
```

## 常用选项
- `new`：创建一个新的 tmux 会话。
- `attach`：附加到一个已经存在的 tmux 会话。
- `detach`：从当前会话中分离。
- `list-sessions`：列出所有当前的 tmux 会话。
- `kill-session`：终止指定的 tmux 会话。

## 常见示例
1. 创建一个新的 tmux 会话：
   ```bash
   tmux new -s mysession
   ```

2. 附加到一个已存在的会话：
   ```bash
   tmux attach -t mysession
   ```

3. 分离当前会话：
   ```bash
   Ctrl-b d
   ```

4. 列出所有会话：
   ```bash
   tmux list-sessions
   ```

5. 终止一个会话：
   ```bash
   tmux kill-session -t mysession
   ```

## 小贴士
- 使用 `Ctrl-b` 组合键可以进入 tmux 命令模式，之后可以输入其他命令。
- 可以使用 `tmux split-window` 命令将当前窗口分割成多个窗格，方便同时查看多个程序的输出。
- 定期保存会话，以便在需要时快速恢复工作环境。