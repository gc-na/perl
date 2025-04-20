# [Sistema Operativo] C Shell (csh) jobs Uso: Gestionar trabajos en segundo plano

## Overview
El comando `jobs` en C Shell (csh) se utiliza para mostrar una lista de los trabajos que se están ejecutando en segundo plano en la sesión actual del shell. Esto es útil para monitorear y gestionar tareas que no están en primer plano.

## Usage
La sintaxis básica del comando es la siguiente:

```
jobs [options] [arguments]
```

## Common Options
- `-l`: Muestra el número de proceso (PID) junto con el estado del trabajo.
- `-n`: Muestra solo los trabajos que han cambiado de estado desde la última vez que se ejecutó el comando.
- `-p`: Muestra solo los números de proceso de los trabajos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `jobs`:

1. **Listar trabajos en segundo plano:**
   ```csh
   jobs
   ```

2. **Listar trabajos con PID:**
   ```csh
   jobs -l
   ```

3. **Mostrar trabajos que han cambiado de estado:**
   ```csh
   jobs -n
   ```

4. **Mostrar solo los números de proceso:**
   ```csh
   jobs -p
   ```

## Tips
- Utiliza `bg` para reanudar un trabajo detenido en segundo plano.
- Usa `fg` para llevar un trabajo en segundo plano al primer plano.
- Recuerda que puedes usar `kill` seguido del PID para terminar un trabajo si es necesario.