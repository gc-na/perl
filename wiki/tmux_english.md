# [Linux] C Shell (csh) tmux 用法: Terminal multiplexer

## Overview
The `tmux` command is a terminal multiplexer that allows users to create, manage, and navigate multiple terminal sessions from a single window. It is particularly useful for managing long-running processes and for organizing work in a more efficient manner.

## Usage
The basic syntax of the `tmux` command is as follows:

```bash
tmux [options] [arguments]
```

## Common Options
- `new`: Start a new tmux session.
- `attach`: Attach to an existing tmux session.
- `detach`: Detach from the current tmux session.
- `list-sessions`: List all active tmux sessions.
- `kill-session`: Terminate a specified tmux session.

## Common Examples
Here are some practical examples of how to use `tmux`:

1. **Start a new tmux session**:
   ```bash
   tmux new -s mysession
   ```

2. **Attach to an existing session**:
   ```bash
   tmux attach -t mysession
   ```

3. **Detach from the current session**:
   Press `Ctrl-b` followed by `d`.

4. **List all active sessions**:
   ```bash
   tmux list-sessions
   ```

5. **Kill a specific session**:
   ```bash
   tmux kill-session -t mysession
   ```

## Tips
- Use `Ctrl-b` followed by `c` to create a new window within your tmux session.
- Split the terminal window vertically with `Ctrl-b` followed by `%` and horizontally with `Ctrl-b` followed by `"` for better multitasking.
- Customize your tmux configuration by editing the `.tmux.conf` file in your home directory to enhance your workflow.