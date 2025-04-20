# [Linux] C Shell (csh) tmux uso: Multiplexor de terminal

## Overview
El comando `tmux` es un multiplexor de terminal que permite a los usuarios crear, gestionar y navegar entre múltiples sesiones de terminal dentro de una sola ventana. Esto es especialmente útil para trabajar en múltiples tareas simultáneamente sin necesidad de abrir varias ventanas de terminal.

## Usage
La sintaxis básica del comando `tmux` es la siguiente:

```bash
tmux [opciones] [argumentos]
```

## Common Options
- `new`: Crea una nueva sesión de tmux.
- `attach`: Se conecta a una sesión existente.
- `detach`: Desconecta la sesión actual.
- `list-sessions`: Muestra todas las sesiones de tmux activas.
- `kill-session`: Termina una sesión específica.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `tmux`:

1. **Crear una nueva sesión de tmux:**
   ```bash
   tmux new -s mi_sesion
   ```

2. **Conectarse a una sesión existente:**
   ```bash
   tmux attach -t mi_sesion
   ```

3. **Desconectar de la sesión actual:**
   ```bash
   Ctrl + b, d
   ```

4. **Listar todas las sesiones activas:**
   ```bash
   tmux list-sessions
   ```

5. **Terminar una sesión específica:**
   ```bash
   tmux kill-session -t mi_sesion
   ```

## Tips
- Usa combinaciones de teclas como `Ctrl + b` seguido de otra tecla para ejecutar comandos dentro de tmux.
- Puedes dividir la ventana en paneles usando `Ctrl + b` seguido de `%` para dividir verticalmente o `"` para dividir horizontalmente.
- Guarda tus configuraciones de tmux en un archivo `.tmux.conf` en tu directorio home para personalizar tu experiencia.