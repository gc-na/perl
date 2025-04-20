# [Linux] C Shell (csh) script uso: Grabar sesiones de terminal

## Overview
El comando `script` en C Shell (csh) se utiliza para grabar una sesión de terminal en un archivo. Esto es útil para documentar el trabajo realizado en la terminal, permitiendo a los usuarios revisar los comandos ejecutados y sus salidas más tarde.

## Usage
La sintaxis básica del comando `script` es la siguiente:

```csh
script [options] [archivo]
```

## Common Options
- `-a`: Añadir la salida al final del archivo existente en lugar de sobrescribirlo.
- `-f`: Forzar la escritura de la salida en el archivo en tiempo real.
- `-q`: Ejecutar en modo silencioso, sin mostrar mensajes de inicio y final.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `script`:

1. **Grabar una sesión en un archivo por defecto:**
   ```csh
   script
   ```
   Esto comenzará a grabar la sesión en un archivo llamado `typescript`.

2. **Grabar una sesión en un archivo específico:**
   ```csh
   script mi_sesion.txt
   ```
   Esto grabará la sesión en el archivo `mi_sesion.txt`.

3. **Añadir a un archivo existente:**
   ```csh
   script -a mi_sesion.txt
   ```
   Esto añadirá la nueva sesión al final de `mi_sesion.txt`.

4. **Grabar en tiempo real:**
   ```csh
   script -f mi_sesion.txt
   ```
   Esto grabará la sesión en `mi_sesion.txt` y actualizará el archivo en tiempo real.

5. **Ejecutar en modo silencioso:**
   ```csh
   script -q mi_sesion.txt
   ```
   Esto grabará la sesión sin mostrar mensajes de inicio y final.

## Tips
- Asegúrate de terminar la grabación usando el comando `exit` o presionando `Ctrl+D` para que el archivo se cierre correctamente.
- Revisa el archivo generado después de la sesión para asegurarte de que toda la información necesaria ha sido grabada.
- Utiliza la opción `-f` si necesitas ver la salida en tiempo real, especialmente útil en sesiones largas.