# [Linux] C Shell (csh) history Uso equivalente: Muestra el historial de comandos ejecutados

## Overview
El comando `history` en C Shell (csh) se utiliza para mostrar una lista de los comandos que han sido ejecutados en la sesión actual. Esto permite a los usuarios revisar y reutilizar comandos anteriores sin tener que volver a escribirlos.

## Usage
La sintaxis básica del comando `history` es la siguiente:

```
history [options] [arguments]
```

## Common Options
- `-c`: Borra el historial de comandos.
- `-n`: Lee el historial desde el archivo de historial y lo agrega a la lista actual.
- `-r`: Lee el historial desde el archivo de historial sin agregarlo a la lista actual.
- `-w`: Escribe el historial actual en el archivo de historial.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `history`:

1. **Mostrar el historial de comandos:**
   ```csh
   history
   ```

2. **Borrar el historial de comandos:**
   ```csh
   history -c
   ```

3. **Leer el historial desde un archivo:**
   ```csh
   history -r
   ```

4. **Escribir el historial actual en el archivo:**
   ```csh
   history -w
   ```

5. **Ejecutar un comando del historial (por número):**
   Supongamos que el comando que deseas volver a ejecutar tiene el número 5 en el historial.
   ```csh
   !5
   ```

## Tips
- Utiliza `history` frecuentemente para revisar los comandos que has ejecutado y mejorar tu flujo de trabajo.
- Puedes combinar el uso de `history` con otros comandos como `grep` para buscar comandos específicos en tu historial.
- Recuerda que el historial se guarda por sesión, así que asegúrate de usar `history -w` si deseas conservarlo para futuras sesiones.