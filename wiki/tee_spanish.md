# [Linux] C Shell (csh) tee uso: Redirigir la salida a múltiples destinos

## Overview
El comando `tee` en C Shell (csh) se utiliza para leer la entrada estándar y escribirla tanto en la salida estándar como en uno o más archivos. Esto permite que los usuarios vean la salida de un comando en la terminal mientras también la guardan en un archivo para su posterior referencia.

## Usage
La sintaxis básica del comando `tee` es la siguiente:

```csh
tee [options] [arguments]
```

## Common Options
- `-a`: Añade la salida al final del archivo en lugar de sobrescribirlo.
- `-i`: Ignora las señales de interrupción.

## Common Examples

1. **Guardar la salida de un comando en un archivo**:
   ```csh
   ls -l | tee archivo.txt
   ```
   Este comando lista los archivos en el directorio actual y guarda la salida en `archivo.txt`.

2. **Añadir la salida a un archivo existente**:
   ```csh
   echo "Nueva línea" | tee -a archivo.txt
   ```
   Este comando añade "Nueva línea" al final de `archivo.txt` sin sobrescribir el contenido existente.

3. **Ver la salida en la terminal y en múltiples archivos**:
   ```csh
   ps aux | tee archivo1.txt archivo2.txt
   ```
   Este comando muestra los procesos en ejecución en la terminal y guarda la salida en `archivo1.txt` y `archivo2.txt`.

## Tips
- Utiliza la opción `-a` si deseas conservar el contenido existente de un archivo y añadirle nueva información.
- Combinando `tee` con otros comandos, puedes crear flujos de trabajo más complejos, como redirigir la salida de un script a varios archivos de registro.
- Recuerda que `tee` puede ser útil en scripts para depurar y registrar la salida de comandos sin perderla en la terminal.