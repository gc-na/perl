# [Linux] C Shell (csh) renice Uso: Cambiar la prioridad de un proceso

## Overview
El comando `renice` se utiliza para cambiar la prioridad de ejecución de uno o más procesos en un sistema operativo Unix. Al ajustar la prioridad, puedes influir en la cantidad de recursos del sistema que un proceso puede utilizar, lo que puede ser útil para mejorar el rendimiento de otros procesos.

## Usage
La sintaxis básica del comando `renice` es la siguiente:

```
renice [opciones] [valores] [PID]
```

## Common Options
- `-n`: Especifica el nuevo valor de prioridad. Un número más bajo indica mayor prioridad.
- `-p`: Permite especificar el identificador del proceso (PID) al que se le cambiará la prioridad.
- `-g`: Cambia la prioridad de todos los procesos en un grupo de procesos específico.
- `-u`: Cambia la prioridad de todos los procesos de un usuario específico.

## Common Examples
1. Cambiar la prioridad de un proceso específico:
   ```csh
   renice -n 10 -p 1234
   ```
   Este comando establece la prioridad del proceso con PID 1234 a 10.

2. Cambiar la prioridad de todos los procesos de un usuario:
   ```csh
   renice -n 5 -u nombre_usuario
   ```
   Aquí, todos los procesos del usuario `nombre_usuario` se les asigna una prioridad de 5.

3. Cambiar la prioridad de un grupo de procesos:
   ```csh
   renice -n -5 -g 5678
   ```
   Este comando cambia la prioridad de todos los procesos en el grupo con ID 5678 a -5, dándoles mayor prioridad.

## Tips
- Utiliza `renice` con precaución, ya que establecer una prioridad demasiado alta puede afectar negativamente el rendimiento del sistema.
- Verifica la prioridad actual de los procesos usando el comando `ps` antes de realizar cambios.
- Recuerda que solo los usuarios con privilegios adecuados pueden aumentar la prioridad de un proceso (valores negativos).