# [Linux] C Shell (csh) nohup 使用方法: 使进程在退出终端后继续运行

## 概述
`nohup` 命令用于在用户退出终端后继续运行指定的命令。它可以防止进程因终端关闭而被终止，常用于长时间运行的任务。

## 用法
基本语法如下：
```csh
nohup [选项] [参数]
```

## 常用选项
- `-h`：显示帮助信息。
- `-p`：将输出重定向到指定的文件。
- `-n`：不将输出重定向到 `nohup.out` 文件。

## 常见示例
1. **运行一个长时间的脚本**
   ```csh
   nohup ./long_running_script.sh &
   ```
   这条命令会在后台运行 `long_running_script.sh`，即使用户退出终端，脚本仍会继续执行。

2. **将输出重定向到指定文件**
   ```csh
   nohup ./my_process > output.log &
   ```
   这条命令会将 `my_process` 的输出保存到 `output.log` 文件中。

3. **使用 nohup 运行 Python 脚本**
   ```csh
   nohup python my_script.py &
   ```
   这条命令会在后台运行 Python 脚本 `my_script.py`。

## 小贴士
- 使用 `&` 将命令放入后台运行，以便可以继续使用终端。
- 定期检查输出文件，以确保进程正常运行。
- 在使用 `nohup` 时，确保命令的路径正确，以避免找不到命令的错误。