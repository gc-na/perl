# [Linux] C Shell (csh) users uso equivalente: Muestra información sobre los usuarios conectados

## Overview
El comando `users` en C Shell (csh) se utiliza para mostrar los nombres de los usuarios que están actualmente conectados al sistema. Es una herramienta simple pero efectiva para obtener información sobre la actividad de los usuarios en un entorno multiusuario.

## Usage
La sintaxis básica del comando `users` es la siguiente:

```
users [opciones] [argumentos]
```

## Common Options
- `-n`: Muestra el número de usuarios únicos conectados.
- `-r`: Muestra solo los usuarios que están conectados en este momento.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `users`:

1. **Mostrar todos los usuarios conectados:**
   ```csh
   users
   ```

2. **Mostrar el número de usuarios únicos conectados:**
   ```csh
   users -n
   ```

3. **Mostrar solo los usuarios conectados en este momento:**
   ```csh
   users -r
   ```

## Tips
- Utiliza `users` en combinación con otros comandos como `who` o `w` para obtener información más detallada sobre los usuarios conectados.
- Recuerda que el comando `users` solo muestra los nombres de los usuarios, no proporciona información adicional como el tiempo de conexión o la actividad actual. Para eso, considera usar `who` o `w`.