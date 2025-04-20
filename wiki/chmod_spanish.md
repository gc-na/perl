# [Linux] C Shell (csh) chmod uso: Cambiar permisos de archivos y directorios

## Overview
El comando `chmod` se utiliza para cambiar los permisos de acceso de archivos y directorios en sistemas operativos Unix y Linux. Permite a los usuarios definir quién puede leer, escribir o ejecutar un archivo.

## Usage
La sintaxis básica del comando `chmod` es la siguiente:

```csh
chmod [opciones] [argumentos]
```

## Common Options
- `-R`: Aplica los cambios de permisos de manera recursiva a todos los archivos y subdirectorios.
- `-v`: Muestra información detallada sobre los cambios realizados.
- `-c`: Muestra información sobre los cambios solo si se han realizado modificaciones.

## Common Examples
1. **Cambiar permisos a un archivo específico:**
   ```csh
   chmod 755 archivo.txt
   ```
   Este comando establece permisos de lectura, escritura y ejecución para el propietario, y permisos de lectura y ejecución para el grupo y otros.

2. **Cambiar permisos de manera recursiva:**
   ```csh
   chmod -R 644 directorio/
   ```
   Esto aplica permisos de lectura y escritura al propietario, y solo lectura al grupo y otros para todos los archivos dentro del directorio.

3. **Mostrar cambios realizados:**
   ```csh
   chmod -v 700 script.sh
   ```
   Este comando cambia los permisos del archivo `script.sh` y muestra un mensaje indicando que se han realizado cambios.

4. **Cambiar permisos solo si es necesario:**
   ```csh
   chmod -c 600 archivo_secreto.txt
   ```
   Aquí, `chmod` cambiará los permisos de `archivo_secreto.txt` y solo mostrará un mensaje si los permisos han cambiado.

## Tips
- Siempre verifica los permisos actuales de un archivo con `ls -l` antes de realizar cambios.
- Utiliza permisos restrictivos (como 700 o 600) para archivos sensibles.
- Recuerda que los permisos se pueden expresar tanto en notación octal (como 755) como en notación simbólica (como u+rwx,g+rx,o+rx).