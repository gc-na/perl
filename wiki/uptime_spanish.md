# [Linux] C Shell (csh) uptime Uso: Muestra el tiempo de actividad del sistema

## Overview
El comando `uptime` en C Shell (csh) se utiliza para mostrar cuánto tiempo ha estado funcionando el sistema desde su último arranque. También proporciona información sobre el número de usuarios conectados y la carga promedio del sistema en los últimos 1, 5 y 15 minutos.

## Usage
La sintaxis básica del comando es la siguiente:

```
uptime [opciones]
```

## Common Options
- `-p`: Muestra el tiempo de actividad en un formato legible por humanos.
- `-s`: Muestra la fecha y hora en que se inició el sistema.

## Common Examples

### Ejemplo 1: Tiempo de actividad básico
Para ver el tiempo de actividad del sistema, simplemente ejecuta:

```
uptime
```

### Ejemplo 2: Tiempo de actividad en formato legible
Para mostrar el tiempo de actividad en un formato más amigable, puedes usar la opción `-p`:

```
uptime -p
```

### Ejemplo 3: Fecha y hora de inicio del sistema
Para ver cuándo se inició el sistema, utiliza la opción `-s`:

```
uptime -s
```

## Tips
- Usa `uptime` regularmente para monitorear el rendimiento de tu sistema y asegurarte de que no haya problemas de carga.
- Combina `uptime` con otros comandos como `who` para obtener más información sobre los usuarios conectados y el estado del sistema.
- Si estás administrando un servidor, considera programar un script que registre el tiempo de actividad en intervalos regulares para análisis posteriores.