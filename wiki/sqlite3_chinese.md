# [操作系统] C Shell (csh) sqlite3 使用方法: 交互式数据库管理工具

## 概述
sqlite3 是一个轻量级的关系数据库管理系统，允许用户通过命令行与 SQLite 数据库进行交互。它支持 SQL 查询，数据插入、更新和删除等操作，非常适合小型应用和嵌入式系统。

## 用法
sqlite3 命令的基本语法如下：

```csh
sqlite3 [选项] [参数]
```

## 常用选项
- `-help`：显示帮助信息。
- `-version`：显示 sqlite3 的版本信息。
- `-init <file>`：在启动时执行指定的 SQL 文件。
- `-batch`：以批处理模式运行，不显示提示符。

## 常见示例
1. **创建一个新的数据库**：
   ```csh
   sqlite3 mydatabase.db
   ```

2. **执行 SQL 文件**：
   ```csh
   sqlite3 mydatabase.db < script.sql
   ```

3. **查询数据**：
   ```csh
   sqlite3 mydatabase.db "SELECT * FROM mytable;"
   ```

4. **插入数据**：
   ```csh
   sqlite3 mydatabase.db "INSERT INTO mytable (name, age) VALUES ('Alice', 30);"
   ```

5. **导出查询结果到 CSV 文件**：
   ```csh
   sqlite3 -header -csv mydatabase.db "SELECT * FROM mytable;" > output.csv
   ```

## 提示
- 使用 `.exit` 命令可以安全退出 sqlite3。
- 在执行复杂查询时，建议将 SQL 语句保存在文件中，以便于管理和重用。
- 定期备份数据库文件，以防数据丢失。