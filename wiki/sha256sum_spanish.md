# [Linux] C Shell (csh) sha256sum Uso: Calcular sumas de verificación SHA-256

## Overview
El comando `sha256sum` se utiliza para calcular y verificar la suma de verificación SHA-256 de archivos. Esta suma de verificación es una representación única del contenido de un archivo, lo que permite comprobar su integridad.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
sha256sum [opciones] [argumentos]
```

## Common Options
- `-b`: Procesa archivos binarios.
- `-c`: Verifica las sumas de verificación de los archivos listados en un archivo.
- `-h`: Muestra la ayuda y la información sobre el uso del comando.
- `--quiet`: Suprime la salida de mensajes de error.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `sha256sum`:

1. Calcular la suma de verificación de un archivo:
   ```csh
   sha256sum archivo.txt
   ```

2. Calcular la suma de verificación de varios archivos:
   ```csh
   sha256sum archivo1.txt archivo2.txt
   ```

3. Verificar sumas de verificación a partir de un archivo:
   Primero, crea un archivo con las sumas de verificación:
   ```csh
   sha256sum archivo.txt > checksum.sha256
   ```
   Luego, verifica las sumas de verificación:
   ```csh
   sha256sum -c checksum.sha256
   ```

4. Procesar un archivo binario:
   ```csh
   sha256sum -b archivo.bin
   ```

## Tips
- Siempre verifica las sumas de verificación después de transferir archivos importantes para asegurarte de que no se hayan corrompido.
- Utiliza el archivo de sumas de verificación para mantener un registro de la integridad de tus archivos a lo largo del tiempo.
- Considera usar `--quiet` si deseas evitar la salida de errores en scripts automatizados.