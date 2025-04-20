# [Linux] C Shell (csh) pidstat: Monitoreo del uso de recursos de procesos

## Overview
El comando `pidstat` se utiliza para monitorear el uso de recursos de procesos en sistemas Linux. Proporciona información detallada sobre el uso de CPU, memoria y otros recursos por parte de los procesos en ejecución, lo que es útil para la administración y optimización del rendimiento del sistema.

## Usage
La sintaxis básica del comando `pidstat` es la siguiente:

```bash
pidstat [opciones] [argumentos]
```

## Common Options
- `-h`: Muestra los encabezados de las columnas en formato legible.
- `-r`: Muestra el uso de memoria por proceso.
- `-u`: Muestra el uso de CPU por proceso.
- `-p <pid>`: Especifica el ID de proceso para monitorear.
- `-t`: Muestra estadísticas de todos los hilos de un proceso.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `pidstat`:

1. **Monitorear el uso de CPU de todos los procesos:**
   ```bash
   pidstat -u 1
   ```
   Este comando muestra el uso de CPU de todos los procesos cada segundo.

2. **Monitorear el uso de memoria de un proceso específico:**
   ```bash
   pidstat -r -p 1234 1
   ```
   Reemplaza `1234` con el ID del proceso que deseas monitorear. Este comando muestra el uso de memoria del proceso cada segundo.

3. **Monitorear todos los hilos de un proceso:**
   ```bash
   pidstat -t -p 5678 1
   ```
   Este comando proporciona estadísticas de uso de CPU y memoria para todos los hilos del proceso con ID `5678`.

4. **Mostrar estadísticas con encabezados:**
   ```bash
   pidstat -h -u 1
   ```
   Esto muestra el uso de CPU con encabezados de columna legibles cada segundo.

## Tips
- Utiliza `pidstat` junto con otras herramientas como `top` o `htop` para obtener una visión más completa del rendimiento del sistema.
- Puedes redirigir la salida de `pidstat` a un archivo para un análisis posterior usando `>` para guardar los resultados.
- Experimenta con diferentes intervalos de tiempo para encontrar la frecuencia de monitoreo que mejor se adapte a tus necesidades.