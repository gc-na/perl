# [Linux] C Shell (csh) md5sum uso: Calcular y verificar sumas de verificación MD5

## Overview
El comando `md5sum` se utiliza para calcular y verificar la suma de verificación MD5 de archivos. MD5 es un algoritmo de hash que produce un valor de 128 bits, comúnmente representado como un número hexadecimal de 32 caracteres. Este comando es útil para verificar la integridad de los archivos.

## Usage
La sintaxis básica del comando `md5sum` es la siguiente:

```bash
md5sum [opciones] [argumentos]
```

## Common Options
- `-b`: Procesa archivos en modo binario.
- `-c`: Verifica las sumas de verificación de los archivos listados en un archivo.
- `-t`: Calcula la suma de verificación de un archivo de texto.
- `--help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `md5sum`:

1. **Calcular la suma de verificación de un archivo:**

   ```bash
   md5sum archivo.txt
   ```

2. **Guardar la suma de verificación en un archivo:**

   ```bash
   md5sum archivo.txt > archivo.md5
   ```

3. **Verificar la suma de verificación usando un archivo de verificación:**

   ```bash
   md5sum -c archivo.md5
   ```

4. **Calcular la suma de verificación en modo binario:**

   ```bash
   md5sum -b archivo.bin
   ```

## Tips
- Siempre verifica las sumas de verificación después de transferir archivos importantes para asegurarte de que no se hayan corrompido.
- Utiliza el archivo de verificación para comprobar múltiples archivos a la vez, lo que ahorra tiempo y esfuerzo.
- Recuerda que MD5 no es adecuado para aplicaciones de seguridad crítica, ya que se han encontrado vulnerabilidades en el algoritmo. Considera usar SHA-256 para mayor seguridad.