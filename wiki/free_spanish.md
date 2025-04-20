# [Linux] C Shell (csh) free uso: Muestra la memoria disponible en el sistema

## Overview
El comando `free` en C Shell (csh) se utiliza para mostrar la cantidad de memoria libre y utilizada en el sistema. Proporciona información sobre la memoria física, la memoria swap y los buffers utilizados por el kernel, lo que es útil para monitorear el rendimiento del sistema.

## Usage
La sintaxis básica del comando `free` es la siguiente:

```csh
free [opciones] [argumentos]
```

## Common Options
- `-h`: Muestra la memoria en un formato legible para humanos (por ejemplo, en KB, MB).
- `-m`: Muestra la memoria en megabytes.
- `-g`: Muestra la memoria en gigabytes.
- `-s [segundos]`: Actualiza la salida cada [segundos] especificados.
- `-t`: Muestra un total de la memoria utilizada y libre.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `free`:

1. Mostrar la memoria en un formato legible para humanos:
   ```csh
   free -h
   ```

2. Mostrar la memoria en megabytes:
   ```csh
   free -m
   ```

3. Mostrar la memoria en gigabytes:
   ```csh
   free -g
   ```

4. Actualizar la salida cada 5 segundos:
   ```csh
   free -s 5
   ```

5. Mostrar un total de la memoria utilizada y libre:
   ```csh
   free -t
   ```

## Tips
- Utiliza la opción `-h` para obtener una salida más comprensible, especialmente en sistemas con mucha memoria.
- Combina `free` con otros comandos como `watch` para monitorear la memoria en tiempo real:
  ```csh
  watch free -h
  ```
- Revisa la memoria swap junto con la memoria física para obtener una visión completa del estado del sistema.