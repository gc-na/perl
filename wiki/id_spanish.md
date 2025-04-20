# [Linux] C Shell (csh) id: Muestra información del usuario actual

## Overview
El comando `id` en C Shell (csh) se utiliza para mostrar información sobre el usuario actual, incluyendo su UID (Identificador de Usuario), GID (Identificador de Grupo) y los grupos a los que pertenece.

## Usage
La sintaxis básica del comando es la siguiente:

```
id [opciones] [argumentos]
```

## Common Options
- `-u`: Muestra solo el UID del usuario actual.
- `-g`: Muestra solo el GID del grupo principal del usuario actual.
- `-G`: Muestra todos los GID de los grupos a los que pertenece el usuario.
- `-n`: Muestra el nombre en lugar del número para UID y GID.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `id`:

1. Mostrar la información completa del usuario actual:
   ```csh
   id
   ```

2. Mostrar solo el UID del usuario actual:
   ```csh
   id -u
   ```

3. Mostrar solo el GID del grupo principal del usuario actual:
   ```csh
   id -g
   ```

4. Mostrar todos los GID de los grupos a los que pertenece el usuario:
   ```csh
   id -G
   ```

5. Mostrar el nombre del usuario y del grupo principal:
   ```csh
   id -n
   ```

## Tips
- Utiliza `id` sin opciones para obtener una visión general rápida de tu identidad en el sistema.
- Combina `id` con otros comandos para realizar tareas de administración de usuarios y grupos.
- Recuerda que el comando `id` puede ser útil para verificar permisos y accesos en sistemas multiusuario.