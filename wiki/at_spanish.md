# [Linux] C Shell (csh) at: Programar tareas para ejecución futura

## Overview
El comando `at` se utiliza para programar la ejecución de comandos o scripts en un momento específico en el futuro. Es útil para tareas que no necesitan ejecutarse inmediatamente, permitiendo que los usuarios planifiquen trabajos que se ejecutarán automáticamente.

## Usage
La sintaxis básica del comando `at` es la siguiente:

```
at [opciones] [hora]
```

## Common Options
- `-f`: Especifica un archivo que contiene los comandos a ejecutar.
- `-l`: Lista los trabajos programados para el usuario actual.
- `-d`: Elimina un trabajo programado.
- `-m`: Envía un correo electrónico al usuario cuando el trabajo se completa.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `at`:

1. **Programar un comando para ejecutarse a las 3 PM:**
   ```csh
   echo "echo 'Hola, mundo'" | at 15:00
   ```

2. **Ejecutar un script a las 10:30 AM del día siguiente:**
   ```csh
   at 10:30 tomorrow -f /ruta/al/script.sh
   ```

3. **Listar trabajos programados:**
   ```csh
   at -l
   ```

4. **Eliminar un trabajo programado (suponiendo que el ID del trabajo es 1):**
   ```csh
   at -d 1
   ```

5. **Programar un comando para ejecutarse en 5 minutos:**
   ```csh
   echo "echo 'Tarea ejecutada'" | at now + 5 minutes
   ```

## Tips
- Asegúrate de que el servicio `atd` esté en funcionamiento en tu sistema para que los trabajos programados se ejecuten correctamente.
- Utiliza el comando `at -l` frecuentemente para revisar tus trabajos programados y evitar duplicaciones.
- Considera usar el flag `-m` si deseas recibir notificaciones por correo electrónico cuando se complete un trabajo.