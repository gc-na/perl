# [Sistema Operativo] C Shell (csh) ftp Uso: Transferencia de archivos a través de la red

## Overview
El comando `ftp` (File Transfer Protocol) se utiliza para transferir archivos entre un cliente y un servidor a través de una red. Permite a los usuarios conectarse a un servidor FTP, subir y bajar archivos, y realizar diversas operaciones relacionadas con la gestión de archivos.

## Usage
La sintaxis básica del comando `ftp` es la siguiente:

```bash
ftp [opciones] [argumentos]
```

## Common Options
- `-i`: Desactiva el modo interactivo, lo que permite transferencias de archivos sin solicitar confirmación.
- `-v`: Muestra información detallada sobre la conexión y la transferencia de archivos.
- `-n`: Evita que `ftp` intente iniciar sesión automáticamente al conectarse al servidor.
- `-p`: Utiliza un puerto pasivo para la transferencia de archivos, útil en redes con firewalls.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `ftp`:

1. **Conectar a un servidor FTP:**
   ```bash
   ftp ftp.ejemplo.com
   ```

2. **Subir un archivo al servidor:**
   ```bash
   ftp> put archivo.txt
   ```

3. **Bajar un archivo del servidor:**
   ```bash
   ftp> get archivo.txt
   ```

4. **Listar archivos en el directorio del servidor:**
   ```bash
   ftp> ls
   ```

5. **Cambiar el directorio en el servidor:**
   ```bash
   ftp> cd /ruta/del/directorio
   ```

## Tips
- Siempre verifica la conexión y la autenticidad del servidor FTP antes de transferir archivos.
- Utiliza el modo pasivo (`-p`) si experimentas problemas de conexión en redes con restricciones.
- Recuerda cerrar la sesión correctamente con el comando `bye` o `quit` después de finalizar tus transferencias.