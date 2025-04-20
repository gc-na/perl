# [Linux] C Shell (csh) traceroute uso: Muestra la ruta que toman los paquetes a un destino

## Overview
El comando `traceroute` se utiliza para rastrear la ruta que siguen los paquetes de datos desde el origen hasta un destino específico en una red. Proporciona información sobre cada salto en la ruta, lo que puede ser útil para diagnosticar problemas de conectividad y latencia.

## Usage
La sintaxis básica del comando `traceroute` es la siguiente:

```csh
traceroute [opciones] [argumentos]
```

## Common Options
- `-m <n>`: Establece el número máximo de saltos.
- `-w <n>`: Define el tiempo de espera en segundos para cada respuesta.
- `-q <n>`: Especifica el número de consultas por salto.
- `-n`: Muestra las direcciones IP en lugar de resolver los nombres de host.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `traceroute`:

1. Rastrear la ruta a un sitio web:
   ```csh
   traceroute www.ejemplo.com
   ```

2. Establecer un número máximo de saltos a 15:
   ```csh
   traceroute -m 15 www.ejemplo.com
   ```

3. Usar el modo numérico para evitar la resolución de nombres:
   ```csh
   traceroute -n 8.8.8.8
   ```

4. Cambiar el tiempo de espera a 2 segundos:
   ```csh
   traceroute -w 2 www.ejemplo.com
   ```

## Tips
- Utiliza la opción `-n` si deseas obtener resultados más rápidos al evitar la resolución de nombres.
- Si experimentas problemas de conectividad, observa los saltos donde el tiempo de respuesta aumenta significativamente.
- Prueba con diferentes opciones para ajustar el comportamiento de `traceroute` según tus necesidades específicas.