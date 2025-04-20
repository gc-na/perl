# [Linux] C Shell (csh) stat Uso: Obtener información sobre archivos y sistemas de archivos

## Overview
El comando `stat` se utiliza para mostrar información detallada sobre archivos y sistemas de archivos. Proporciona datos como el tamaño del archivo, las fechas de acceso y modificación, y los permisos de archivo.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
stat [options] [arguments]
```

## Common Options
- `-c` : Permite especificar un formato de salida personalizado.
- `-f` : Muestra información sobre el sistema de archivos en lugar de un archivo específico.
- `--help` : Muestra la ayuda sobre el uso del comando.
- `--version` : Muestra la versión del comando `stat`.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `stat`:

1. **Mostrar información de un archivo específico:**
   ```csh
   stat archivo.txt
   ```

2. **Obtener información en un formato específico:**
   ```csh
   stat -c '%s bytes' archivo.txt
   ```

3. **Mostrar información del sistema de archivos:**
   ```csh
   stat -f /
   ```

4. **Ver la versión del comando:**
   ```csh
   stat --version
   ```

## Tips
- Utiliza la opción `-c` para personalizar la salida y obtener solo la información que necesitas.
- Si trabajas con múltiples archivos, puedes pasar varios nombres de archivo al comando `stat` para obtener información sobre todos ellos a la vez.
- Recuerda que los permisos y las fechas pueden ser cruciales para la gestión de archivos, así que revisa esta información frecuentemente.