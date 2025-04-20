# [Linux] C Shell (csh) sftp uso: Transferencia segura de archivos

## Overview
El comando `sftp` (SSH File Transfer Protocol) se utiliza para transferir archivos de manera segura entre un cliente y un servidor a través de una conexión SSH. Proporciona un método seguro para acceder, transferir y gestionar archivos en sistemas remotos.

## Usage
La sintaxis básica del comando `sftp` es la siguiente:

```csh
sftp [opciones] [usuario@host]
```

## Common Options
- `-P`: Especifica el puerto a utilizar para la conexión.
- `-b`: Permite ejecutar comandos desde un archivo en lugar de interactuar en la línea de comandos.
- `-o`: Permite especificar opciones de configuración adicionales, como el tiempo de espera de conexión.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `sftp`:

1. Conectar a un servidor SFTP:
   ```csh
   sftp usuario@servidor.com
   ```

2. Transferir un archivo desde el cliente al servidor:
   ```csh
   put archivo.txt
   ```

3. Descargar un archivo del servidor al cliente:
   ```csh
   get archivo_remoto.txt
   ```

4. Listar archivos en el directorio remoto:
   ```csh
   ls
   ```

5. Ejecutar comandos desde un archivo:
   ```csh
   sftp -b comandos.txt usuario@servidor.com
   ```

## Tips
- Asegúrate de tener configuradas las claves SSH para una conexión más segura y sin necesidad de contraseña.
- Utiliza el comando `lcd` para cambiar el directorio local antes de transferir archivos.
- Familiarízate con los comandos de `sftp` como `mkdir`, `rmdir`, y `rename` para gestionar archivos y directorios en el servidor remoto.