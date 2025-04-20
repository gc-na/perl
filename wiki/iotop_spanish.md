# [Linux] C Shell (csh) iotop Uso: Monitoreo del uso de I/O de procesos

## Overview
El comando `iotop` se utiliza para monitorear el uso de entrada/salida (I/O) de los procesos en un sistema Linux. Muestra información en tiempo real sobre qué procesos están utilizando más recursos de I/O, lo que es útil para identificar cuellos de botella en el rendimiento del sistema.

## Usage
La sintaxis básica del comando `iotop` es la siguiente:

```bash
iotop [opciones] [argumentos]
```

## Common Options
- `-o`: Muestra solo los procesos que están realizando operaciones de I/O.
- `-b`: Ejecuta `iotop` en modo batch, ideal para redirección a un archivo.
- `-n NUM`: Especifica el número de iteraciones que `iotop` debe realizar antes de salir.
- `-d SEG`: Define el intervalo de actualización en segundos.

## Common Examples
1. **Monitorear procesos en tiempo real**:
   ```bash
   iotop
   ```

2. **Mostrar solo procesos que están realizando I/O**:
   ```bash
   iotop -o
   ```

3. **Ejecutar en modo batch y guardar la salida en un archivo**:
   ```bash
   iotop -b -n 10 > iotop_output.txt
   ```

4. **Actualizar cada 2 segundos y mostrar solo procesos activos**:
   ```bash
   iotop -o -d 2
   ```

## Tips
- Utiliza el modo batch para registrar el uso de I/O durante un período específico, lo que puede ser útil para análisis posteriores.
- Combina `iotop` con otros comandos como `grep` para filtrar resultados específicos.
- Asegúrate de tener permisos adecuados, ya que `iotop` puede requerir privilegios de superusuario para mostrar información completa sobre todos los procesos.