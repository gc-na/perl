# [台灣] C Shell (csh) lsmod 使用方式: 列出已載入的模組

## Overview
`lsmod` 是一個用於顯示當前已載入的內核模組的命令。這個命令可以幫助使用者了解系統中哪些模組正在運行，並提供模組的相關資訊。

## Usage
基本語法如下：

```shell
lsmod [options] [arguments]
```

## Common Options
- `-h`, `--help`: 顯示幫助資訊。
- `-v`, `--verbose`: 顯示詳細的輸出資訊。

## Common Examples
1. **列出所有已載入的模組**：
   ```shell
   lsmod
   ```

2. **顯示幫助資訊**：
   ```shell
   lsmod --help
   ```

3. **顯示詳細資訊**：
   ```shell
   lsmod --verbose
   ```

## Tips
- 定期檢查已載入的模組，可以幫助你了解系統的運行狀態。
- 若發現不必要的模組，可以考慮卸載以釋放系統資源。
- 使用 `modinfo <module_name>` 可以獲取特定模組的更多資訊。