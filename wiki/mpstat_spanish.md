# [Linux] C Shell (csh) mpstat Uso: Monitoreo de estadísticas de CPU

## Overview
El comando `mpstat` se utiliza para mostrar estadísticas de uso de la CPU en sistemas Unix y Linux. Proporciona información sobre la carga de trabajo de cada procesador, lo que permite a los administradores del sistema identificar cuellos de botella y optimizar el rendimiento.

## Usage
La sintaxis básica del comando `mpstat` es la siguiente:

```bash
mpstat [opciones] [argumentos]
```

## Common Options
- `-P ALL`: Muestra estadísticas para todos los procesadores.
- `-u`: Muestra el uso de la CPU en porcentaje.
- `-r`: Muestra estadísticas de E/S de disco.
- `-h`: Muestra la salida en un formato más legible.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `mpstat`:

1. Mostrar estadísticas de todos los procesadores:
   ```bash
   mpstat -P ALL
   ```

2. Mostrar el uso de la CPU en porcentaje:
   ```bash
   mpstat -u
   ```

3. Monitorear las estadísticas de CPU cada 5 segundos:
   ```bash
   mpstat 5
   ```

4. Mostrar estadísticas de E/S de disco:
   ```bash
   mpstat -r
   ```

## Tips
- Utiliza `mpstat` junto con otras herramientas como `vmstat` y `iostat` para obtener una visión más completa del rendimiento del sistema.
- Considera ejecutar `mpstat` en intervalos regulares para registrar el rendimiento a lo largo del tiempo y detectar tendencias.
- Asegúrate de tener permisos adecuados para ejecutar el comando y acceder a las estadísticas del sistema.