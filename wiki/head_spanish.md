# [Linux] C Shell (csh) head uso: Muestra las primeras líneas de un archivo

## Overview
El comando `head` en C Shell (csh) se utiliza para mostrar las primeras líneas de uno o más archivos. Es útil para obtener una vista rápida del contenido de un archivo sin necesidad de abrirlo completamente.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
head [opciones] [argumentos]
```

## Common Options
- `-n [número]`: Especifica el número de líneas que se mostrarán. Por defecto, se muestran 10 líneas.
- `-q`: Suprime la impresión del encabezado de los archivos cuando se muestran múltiples archivos.
- `-v`: Muestra el encabezado de cada archivo incluso si solo hay un archivo.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `head`:

1. Mostrar las primeras 10 líneas de un archivo llamado `archivo.txt`:
   ```csh
   head archivo.txt
   ```

2. Mostrar las primeras 5 líneas de un archivo:
   ```csh
   head -n 5 archivo.txt
   ```

3. Mostrar las primeras 10 líneas de varios archivos:
   ```csh
   head archivo1.txt archivo2.txt
   ```

4. Mostrar las primeras 3 líneas de un archivo y su encabezado:
   ```csh
   head -v -n 3 archivo.txt
   ```

5. Mostrar las primeras 15 líneas de un archivo sin encabezado:
   ```csh
   head -q -n 15 archivo.txt
   ```

## Tips
- Utiliza `head` en combinación con otros comandos, como `grep`, para filtrar y visualizar rápidamente los resultados.
- Si necesitas ver las últimas líneas de un archivo, considera usar el comando `tail`, que complementa a `head`.
- Recuerda que puedes redirigir la salida de `head` a otro archivo usando el operador `>` si deseas guardar las líneas mostradas.