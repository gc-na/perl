# [Linux] C Shell (csh) last comando: muestra los últimos inicios de sesión

## Overview
El comando `last` en C Shell (csh) se utiliza para mostrar una lista de los últimos inicios de sesión de los usuarios en el sistema. Esta herramienta es útil para monitorear la actividad del sistema y verificar quién ha accedido recientemente.

## Usage
La sintaxis básica del comando es la siguiente:

```
last [opciones] [argumentos]
```

## Common Options
- `-n`: Especifica el número de entradas que se mostrarán.
- `-R`: Suprime la impresión de la información de la dirección IP.
- `-f`: Permite especificar un archivo de registro alternativo en lugar de `/var/log/wtmp`.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `last`:

1. Mostrar los últimos inicios de sesión:
   ```csh
   last
   ```

2. Mostrar solo los últimos 5 inicios de sesión:
   ```csh
   last -n 5
   ```

3. Mostrar inicios de sesión sin información de dirección IP:
   ```csh
   last -R
   ```

4. Usar un archivo de registro alternativo:
   ```csh
   last -f /ruta/al/archivo
   ```

## Tips
- Utiliza `last -n` para limitar la salida y hacerla más manejable, especialmente en sistemas con mucho historial.
- Revisa regularmente los inicios de sesión para detectar accesos no autorizados.
- Combina `last` con otros comandos como `grep` para filtrar resultados específicos, por ejemplo, para buscar un usuario en particular:
  ```csh
  last | grep nombre_usuario
  ```