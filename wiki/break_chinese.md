# [操作系统] C Shell (csh) break 用法: 退出循环

## 概述
`break` 命令用于在 C Shell 脚本或交互式会话中退出循环。当程序执行到 `break` 命令时，循环将立即终止，控制权将转移到循环之后的代码。

## 用法
基本语法如下：
```
break [选项] [参数]
```

## 常用选项
- `n`：指定要退出的循环层数。如果不提供，默认退出最内层的循环。

## 常见示例
以下是一些使用 `break` 命令的实际示例：

### 示例 1: 退出最内层循环
```csh
foreach i (1 2 3 4 5)
    if ($i == 3) then
        break
    endif
    echo $i
end
```
输出：
```
1
2
```

### 示例 2: 退出多层循环
```csh
set outer = 1
while ($outer <= 3)
    set inner = 1
    while ($inner <= 5)
        if ($inner == 3) then
            break 2
        endif
        echo "$outer - $inner"
        @ inner++
    end
    @ outer++
end
```
输出：
```
1 - 1
1 - 2
```

## 提示
- 在复杂的嵌套循环中使用 `break n` 可以更精确地控制退出的层级。
- 使用 `break` 时，确保在适当的条件下调用，以避免意外终止循环。
- 结合 `continue` 命令使用，可以更灵活地控制循环的执行流程。