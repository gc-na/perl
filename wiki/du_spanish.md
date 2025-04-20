# [Linux] C Shell (csh) du Uso: Muestra el uso del disco de archivos y directorios

## Overview
El comando `du` (disk usage) se utiliza para estimar y mostrar el uso del espacio en disco de archivos y directorios. Es una herramienta útil para identificar qué archivos o carpetas están ocupando más espacio en el sistema.

## Usage
La sintaxis básica del comando `du` es la siguiente:

```csh
du [opciones] [argumentos]
```

## Common Options
- `-h`: Muestra el tamaño en un formato legible para humanos (por ejemplo, KB, MB).
- `-s`: Muestra solo el total para cada argumento, sin listar los subdirectorios.
- `-c`: Muestra un total acumulado al final de la salida.
- `-a`: Incluye archivos individuales en la salida, no solo directorios.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `du`:

1. **Mostrar el uso del disco de un directorio específico:**
   ```csh
   du /ruta/al/directorio
   ```

2. **Mostrar el uso del disco en un formato legible para humanos:**
   ```csh
   du -h /ruta/al/directorio
   ```

3. **Mostrar solo el total del uso del disco para un directorio:**
   ```csh
   du -s /ruta/al/directorio
   ```

4. **Incluir archivos individuales en la salida:**
   ```csh
   du -a /ruta/al/directorio
   ```

5. **Mostrar el uso del disco con un total acumulado:**
   ```csh
   du -c /ruta/al/directorio/*
   ```

## Tips
- Utiliza la opción `-h` para facilitar la lectura de los tamaños, especialmente en directorios grandes.
- Combina `-s` y `-c` para obtener un resumen rápido del uso del disco en múltiples directorios.
- Recuerda que `du` puede tardar un poco en ejecutarse en directorios con muchos archivos, así que ten paciencia.