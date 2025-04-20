# [Linux] C Shell (csh) vmstat Uso: Monitoreo del estado de la memoria y procesos

## Overview
El comando `vmstat` se utiliza para reportar información sobre procesos, memoria, paginación, bloqueos de E/S y actividad del CPU en sistemas Unix y Linux. Es una herramienta útil para el monitoreo del rendimiento del sistema.

## Usage
La sintaxis básica del comando `vmstat` es la siguiente:

```csh
vmstat [opciones] [intervalo] [número]
```

## Common Options
- `-a`: Muestra información sobre la memoria activa y inactiva.
- `-m`: Muestra estadísticas de la memoria de páginas.
- `-s`: Muestra un resumen de las estadísticas del sistema.
- `intervalo`: Especifica el intervalo en segundos entre cada actualización.
- `número`: Especifica cuántas veces se debe mostrar la información.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `vmstat`:

1. **Mostrar estadísticas de memoria y CPU cada 2 segundos:**
   ```csh
   vmstat 2
   ```

2. **Mostrar estadísticas de memoria activa e inactiva:**
   ```csh
   vmstat -a
   ```

3. **Mostrar un resumen de estadísticas del sistema:**
   ```csh
   vmstat -s
   ```

4. **Mostrar estadísticas cada 5 segundos, 10 veces:**
   ```csh
   vmstat 5 10
   ```

## Tips
- Utiliza `vmstat` junto con otros comandos como `top` o `iostat` para obtener una visión más completa del rendimiento del sistema.
- Monitorea el uso de memoria y CPU durante períodos de alta carga para identificar cuellos de botella.
- Guarda la salida de `vmstat` en un archivo para análisis posterior usando redirección, por ejemplo:
  ```csh
  vmstat 2 > salida_vmstat.txt
  ```