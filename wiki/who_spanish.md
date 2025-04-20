# [Linux] C Shell (csh) who uso: Muestra quién está conectado al sistema

## Overview
El comando `who` en C Shell (csh) se utiliza para mostrar una lista de los usuarios que están actualmente conectados al sistema. Proporciona información sobre los usuarios, como sus nombres de usuario, terminales, y la hora de inicio de sesión.

## Usage
La sintaxis básica del comando `who` es la siguiente:

```
who [opciones] [argumentos]
```

## Common Options
- `-a`: Muestra toda la información disponible, incluyendo usuarios y sus tiempos de inactividad.
- `-b`: Muestra la hora de arranque del sistema.
- `-q`: Muestra solo los nombres de los usuarios conectados y el número total de usuarios.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `who`:

1. **Mostrar usuarios conectados:**
   ```csh
   who
   ```

2. **Mostrar información detallada de los usuarios:**
   ```csh
   who -a
   ```

3. **Mostrar la hora de arranque del sistema:**
   ```csh
   who -b
   ```

4. **Mostrar solo los nombres de los usuarios conectados:**
   ```csh
   who -q
   ```

## Tips
- Utiliza `who` regularmente para monitorear la actividad de los usuarios en el sistema.
- Combina `who` con otros comandos como `grep` para filtrar información específica.
- Recuerda que la salida de `who` puede variar según los permisos de usuario y la configuración del sistema.