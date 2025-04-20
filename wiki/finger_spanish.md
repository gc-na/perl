# [Linux] C Shell (csh) finger uso: Muestra información sobre usuarios del sistema

## Overview
El comando `finger` se utiliza para mostrar información sobre los usuarios que están conectados al sistema. Proporciona detalles como el nombre de usuario, el nombre completo, la hora de inicio de sesión y el estado de la sesión.

## Usage
La sintaxis básica del comando `finger` es la siguiente:

```csh
finger [opciones] [argumentos]
```

## Common Options
- `-l`: Muestra información detallada sobre los usuarios.
- `-m`: Permite buscar usuarios por nombre parcial.
- `-s`: Muestra un resumen breve de la información de los usuarios.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `finger`:

1. Mostrar información de todos los usuarios conectados:
   ```csh
   finger
   ```

2. Mostrar información detallada de un usuario específico:
   ```csh
   finger nombre_usuario
   ```

3. Mostrar un resumen breve de todos los usuarios conectados:
   ```csh
   finger -s
   ```

4. Buscar usuarios por nombre parcial:
   ```csh
   finger -m parte_del_nombre
   ```

## Tips
- Utiliza `finger` regularmente para monitorear quién está conectado al sistema y su actividad.
- Combina `finger` con otros comandos como `grep` para filtrar resultados específicos.
- Recuerda que la información mostrada por `finger` puede depender de la configuración del sistema y de los permisos de usuario.