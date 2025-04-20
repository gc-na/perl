# [Linux] C Shell (csh) netstat uso: Muestra conexiones de red y estadísticas

## Overview
El comando `netstat` se utiliza para mostrar las conexiones de red, las tablas de enrutamiento y una serie de estadísticas de red. Es una herramienta útil para diagnosticar problemas de red y para obtener información sobre el estado de las conexiones en un sistema.

## Usage
La sintaxis básica del comando es la siguiente:

```
netstat [opciones] [argumentos]
```

## Common Options
- `-a`: Muestra todas las conexiones y puertos de escucha.
- `-t`: Muestra solo las conexiones TCP.
- `-u`: Muestra solo las conexiones UDP.
- `-n`: Muestra direcciones y números de puerto en formato numérico.
- `-r`: Muestra la tabla de enrutamiento.
- `-s`: Muestra estadísticas por protocolo.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `netstat`:

1. **Mostrar todas las conexiones y puertos de escucha:**
   ```csh
   netstat -a
   ```

2. **Mostrar solo las conexiones TCP:**
   ```csh
   netstat -t
   ```

3. **Mostrar conexiones UDP en formato numérico:**
   ```csh
   netstat -u -n
   ```

4. **Mostrar la tabla de enrutamiento:**
   ```csh
   netstat -r
   ```

5. **Mostrar estadísticas por protocolo:**
   ```csh
   netstat -s
   ```

## Tips
- Utiliza la opción `-n` para acelerar la salida, ya que evita la resolución de nombres de host.
- Combina opciones para obtener información más específica, por ejemplo, `netstat -at` para ver solo las conexiones TCP activas.
- Revisa regularmente las conexiones de red para detectar actividad inusual que pueda indicar problemas de seguridad.