# [Linux] C Shell (csh) w: [muestra quién está conectado]

## Overview
El comando `w` en C Shell (csh) se utiliza para mostrar información sobre los usuarios que están actualmente conectados al sistema, así como su actividad. Proporciona detalles como el nombre de usuario, el terminal, el tiempo de actividad y el comando que están ejecutando.

## Usage
La sintaxis básica del comando es la siguiente:

```
w [opciones] [argumentos]
```

## Common Options
- `-h`: Omite la línea de encabezado.
- `-s`: Muestra una salida más concisa, sin detalles adicionales.
- `-f`: Muestra el nombre completo del host en lugar del nombre corto.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `w`:

1. **Mostrar todos los usuarios conectados:**
   ```csh
   w
   ```

2. **Mostrar usuarios conectados sin encabezado:**
   ```csh
   w -h
   ```

3. **Mostrar información de usuarios en formato conciso:**
   ```csh
   w -s
   ```

4. **Mostrar información con nombres de host completos:**
   ```csh
   w -f
   ```

## Tips
- Utiliza `w` regularmente para monitorear la actividad de los usuarios en sistemas compartidos.
- Combina `w` con otros comandos como `grep` para filtrar resultados específicos.
- Recuerda que la información mostrada puede variar según los permisos de usuario y la configuración del sistema.