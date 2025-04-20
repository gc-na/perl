# [Linux] C Shell (csh) gzip Uso: Comprimir archivos

## Overview
El comando `gzip` se utiliza para comprimir archivos en sistemas Unix y Linux. Su función principal es reducir el tamaño de los archivos, lo que facilita su almacenamiento y transferencia.

## Usage
La sintaxis básica del comando `gzip` es la siguiente:

```bash
gzip [opciones] [argumentos]
```

## Common Options
- `-d`: Descomprime un archivo.
- `-k`: Mantiene el archivo original después de la compresión.
- `-v`: Muestra información detallada sobre el proceso de compresión.
- `-r`: Comprime recursivamente todos los archivos en un directorio.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `gzip`:

1. Comprimir un archivo:
   ```bash
   gzip archivo.txt
   ```

2. Descomprimir un archivo:
   ```bash
   gzip -d archivo.txt.gz
   ```

3. Comprimir un archivo y mantener el original:
   ```bash
   gzip -k archivo.txt
   ```

4. Comprimir todos los archivos en un directorio de forma recursiva:
   ```bash
   gzip -r /ruta/al/directorio
   ```

5. Ver detalles de la compresión:
   ```bash
   gzip -v archivo.txt
   ```

## Tips
- Siempre verifica el espacio disponible en disco antes de comprimir archivos grandes.
- Utiliza la opción `-k` si deseas conservar los archivos originales después de la compresión.
- Para descomprimir archivos `.gz`, recuerda usar la opción `-d` o simplemente `gunzip`.