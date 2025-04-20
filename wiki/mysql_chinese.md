# [Linux] C Shell (csh) mysql 用法: 数据库管理命令

## 概述
`mysql` 命令是一个用于与 MySQL 数据库服务器进行交互的客户端工具。用户可以通过它执行 SQL 查询、管理数据库和表，以及进行数据操作。

## 用法
基本语法如下：
```bash
mysql [options] [arguments]
```

## 常用选项
- `-u`：指定用户名。
- `-p`：提示输入密码。
- `-h`：指定数据库服务器的主机名。
- `-D`：指定要使用的数据库。
- `-e`：直接执行 SQL 语句。

## 常见示例
1. 连接到本地 MySQL 数据库：
   ```bash
   mysql -u root -p
   ```

2. 连接到远程 MySQL 数据库：
   ```bash
   mysql -h 192.168.1.100 -u user -p
   ```

3. 选择特定数据库并执行 SQL 查询：
   ```bash
   mysql -u user -p -D database_name -e "SELECT * FROM table_name;"
   ```

4. 导出数据库到 SQL 文件：
   ```bash
   mysqldump -u user -p database_name > backup.sql
   ```

5. 从 SQL 文件导入数据：
   ```bash
   mysql -u user -p database_name < backup.sql
   ```

## 提示
- 确保使用强密码以保护数据库安全。
- 使用 `-e` 选项可以快速执行 SQL 语句，适合脚本自动化。
- 定期备份数据库，以防数据丢失。