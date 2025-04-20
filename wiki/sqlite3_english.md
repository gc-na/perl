# [Linux] C Shell (csh) sqlite3用法: 交互式数据库管理

## Overview
The `sqlite3` command is a command-line interface for SQLite, a lightweight, serverless, self-contained SQL database engine. It allows users to create, manage, and query SQLite databases directly from the terminal.

## Usage
The basic syntax of the `sqlite3` command is as follows:

```bash
sqlite3 [options] [arguments]
```

## Common Options
- `-help` : Displays help information about the command.
- `-version` : Shows the version of SQLite being used.
- `-init <file>` : Executes the SQL commands in the specified file upon startup.
- `-batch` : Runs in batch mode, which is useful for scripting.
- `-cmd <command>` : Executes a command before entering the interactive prompt.

## Common Examples
Here are some practical examples of using the `sqlite3` command:

1. **Creating a new database:**
   ```bash
   sqlite3 mydatabase.db
   ```

2. **Creating a table in the database:**
   ```bash
   sqlite3 mydatabase.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);"
   ```

3. **Inserting data into a table:**
   ```bash
   sqlite3 mydatabase.db "INSERT INTO users (name, age) VALUES ('Alice', 30);"
   ```

4. **Querying data from a table:**
   ```bash
   sqlite3 mydatabase.db "SELECT * FROM users;"
   ```

5. **Exporting query results to a CSV file:**
   ```bash
   sqlite3 -header -csv mydatabase.db "SELECT * FROM users;" > users.csv
   ```

## Tips
- Always back up your database before performing operations that modify data.
- Use the `.schema` command within the SQLite prompt to view the structure of your tables.
- For batch processing, consider using the `-batch` option to suppress interactive prompts.
- Familiarize yourself with SQL syntax, as it is essential for effective database manipulation using `sqlite3`.