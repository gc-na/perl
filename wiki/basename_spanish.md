# [Linux] C Shell (csh) basename Uso: Extraer el nombre de un archivo sin su ruta

## Overview
El comando `basename` se utiliza para extraer el nombre de un archivo de su ruta completa, eliminando cualquier prefijo de directorio. Esto es útil cuando se necesita trabajar solo con el nombre del archivo.

## Usage
La sintaxis básica del comando `basename` es la siguiente:

```csh
basename [opciones] [argumentos]
```

## Common Options
- `-a`: Procesa múltiples nombres de archivo y devuelve solo los nombres base.
- `-s`: Elimina un sufijo específico del nombre del archivo.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `basename`:

1. **Extraer el nombre de un archivo de una ruta completa:**

   ```csh
   basename /ruta/al/archivo.txt
   ```

   Salida:
   ```
   archivo.txt
   ```

2. **Eliminar un sufijo específico:**

   ```csh
   basename /ruta/al/archivo.txt .txt
   ```

   Salida:
   ```
   archivo
   ```

3. **Procesar múltiples nombres de archivo:**

   ```csh
   basename -a /ruta/al/archivo1.txt /ruta/al/archivo2.txt
   ```

   Salida:
   ```
   archivo1.txt
   archivo2.txt
   ```

## Tips
- Utiliza `basename` en scripts para simplificar el manejo de nombres de archivos.
- Combina `basename` con otros comandos como `find` para obtener nombres de archivos de manera eficiente.
- Recuerda que `basename` solo elimina la ruta y el sufijo especificado, así que asegúrate de que los argumentos sean correctos para evitar resultados inesperados.