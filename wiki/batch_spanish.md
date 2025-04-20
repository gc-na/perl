# [Linux] C Shell (csh) batch uso: Ejecutar trabajos en segundo plano

## Overview
El comando `batch` en C Shell (csh) permite a los usuarios programar la ejecución de comandos o scripts para que se realicen en un momento posterior, específicamente cuando el sistema tiene recursos disponibles. Esto es útil para tareas que requieren mucho tiempo y que no necesitan ser ejecutadas de inmediato.

## Usage
La sintaxis básica del comando `batch` es la siguiente:

```csh
batch [opciones] [argumentos]
```

## Common Options
- `-l`: Utiliza el entorno de inicio de sesión.
- `-m`: Envía un correo electrónico al usuario cuando se completa el trabajo.
- `-q`: Especifica una cola de trabajo.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `batch`:

1. **Ejecutar un script en segundo plano:**
   ```csh
   echo "sh /ruta/al/script.sh" | batch
   ```

2. **Programar un comando para que se ejecute más tarde:**
   ```csh
   echo "tar -czf backup.tar.gz /ruta/al/directorio" | batch
   ```

3. **Ejecutar múltiples comandos:**
   ```csh
   {
       echo "echo 'Tarea 1 completada'" 
       echo "echo 'Tarea 2 completada'"
   } | batch
   ```

## Tips
- Asegúrate de que los comandos o scripts que deseas ejecutar estén correctamente escritos y sean accesibles desde el entorno donde se ejecutará `batch`.
- Utiliza la opción `-m` si deseas recibir notificaciones por correo electrónico sobre la finalización de tus trabajos.
- Revisa la cola de trabajos si tienes múltiples tareas programadas para evitar conflictos o sobrecarga del sistema.