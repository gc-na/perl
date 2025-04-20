# [Linux] C Shell (csh) psql用法: PostgreSQL命令行客户端

## Overview
The `psql` command is a terminal-based front-end for interacting with PostgreSQL databases. It allows users to execute SQL commands, manage database objects, and perform administrative tasks directly from the command line.

## Usage
The basic syntax of the `psql` command is as follows:

```bash
psql [options] [arguments]
```

## Common Options
- `-h` : Specifies the host of the database server.
- `-p` : Specifies the port number to connect to the database server.
- `-U` : Specifies the username to connect to the database.
- `-d` : Specifies the database name to connect to.
- `-W` : Prompts for the password of the user.
- `-c` : Allows you to execute a single command and then exit.

## Common Examples
Here are some practical examples of using the `psql` command:

1. **Connect to a Database**
   ```bash
   psql -U username -d database_name
   ```

2. **Connect to a Database on a Specific Host and Port**
   ```bash
   psql -h localhost -p 5432 -U username -d database_name
   ```

3. **Execute a SQL Command Directly**
   ```bash
   psql -U username -d database_name -c "SELECT * FROM table_name;"
   ```

4. **List All Databases**
   ```bash
   psql -U username -c "\l"
   ```

5. **Export Query Results to a File**
   ```bash
   psql -U username -d database_name -c "COPY (SELECT * FROM table_name) TO '/path/to/file.csv' WITH CSV;"
   ```

## Tips
- Always use the `-W` option to ensure you are prompted for a password, enhancing security.
- Use the `\?` command inside `psql` to get help on available commands and options.
- To exit `psql`, simply type `\q` and hit Enter.
- For complex queries, consider writing them in a `.sql` file and executing them with `psql -f filename.sql`.