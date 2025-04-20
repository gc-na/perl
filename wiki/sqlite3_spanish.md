# [Linux] C Shell (csh) sqlite3 Uso: Interactuar con bases de datos SQLite

## Overview
El comando `sqlite3` se utiliza para interactuar con bases de datos SQLite. Permite a los usuarios ejecutar consultas SQL, crear y modificar bases de datos, y gestionar datos de manera eficiente.

## Usage
La sintaxis básica del comando `sqlite3` es la siguiente:

```bash
sqlite3 [opciones] [argumentos]
```

## Common Options
- `-init <archivo>`: Ejecuta comandos desde el archivo especificado al iniciar.
- `-batch`: Modo por lotes, ideal para scripts, no muestra el prompt.
- `-header`: Muestra los nombres de las columnas en la salida.
- `-version`: Muestra la versión de SQLite instalada.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `sqlite3`:

1. **Crear una nueva base de datos:**

   ```bash
   sqlite3 mi_base_de_datos.db
   ```

2. **Ejecutar un archivo de comandos SQL:**

   ```bash
   sqlite3 mi_base_de_datos.db -init mis_comandos.sql
   ```

3. **Mostrar la versión de SQLite:**

   ```bash
   sqlite3 -version
   ```

4. **Crear una tabla y agregar datos:**

   ```bash
   sqlite3 mi_base_de_datos.db "CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT);"
   sqlite3 mi_base_de_datos.db "INSERT INTO usuarios (nombre) VALUES ('Juan');"
   ```

5. **Consultar datos de una tabla:**

   ```bash
   sqlite3 mi_base_de_datos.db "SELECT * FROM usuarios;"
   ```

## Tips
- Siempre realiza copias de seguridad de tus bases de datos antes de realizar cambios importantes.
- Utiliza el modo `-batch` cuando ejecutes scripts para evitar la interacción manual.
- Familiarízate con las consultas SQL básicas para aprovechar al máximo `sqlite3`.