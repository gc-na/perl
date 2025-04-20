# [Linux] C Shell (csh) mysql uso: Interactuar con bases de datos MySQL

## Overview
El comando `mysql` se utiliza para interactuar con bases de datos MySQL desde la línea de comandos. Permite a los usuarios ejecutar consultas SQL, gestionar bases de datos y realizar diversas operaciones administrativas.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
mysql [options] [arguments]
```

## Common Options
- `-u [usuario]`: Especifica el nombre de usuario para conectarse a la base de datos.
- `-p`: Solicita la contraseña del usuario.
- `-h [host]`: Define el host donde se encuentra el servidor MySQL (por defecto es localhost).
- `-D [base_de_datos]`: Selecciona la base de datos a utilizar al iniciar la sesión.
- `-e "[consulta]"`: Permite ejecutar una consulta SQL directamente desde la línea de comandos.

## Common Examples
1. Conectar a MySQL con un usuario y solicitar contraseña:
   ```bash
   mysql -u mi_usuario -p
   ```

2. Conectar a una base de datos específica:
   ```bash
   mysql -u mi_usuario -p -D mi_base_de_datos
   ```

3. Ejecutar una consulta SQL directamente:
   ```bash
   mysql -u mi_usuario -p -e "SELECT * FROM mi_tabla;"
   ```

4. Conectar a un servidor remoto:
   ```bash
   mysql -u mi_usuario -p -h 192.168.1.100
   ```

## Tips
- Siempre utiliza la opción `-p` para proteger tu contraseña y evitar que se muestre en la línea de comandos.
- Familiarízate con las consultas SQL básicas para aprovechar al máximo el uso de `mysql`.
- Considera utilizar archivos de configuración para almacenar credenciales y opciones de conexión, lo que puede simplificar el proceso de conexión.