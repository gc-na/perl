# [Linux] C Shell (csh) nice uso: Cambiar la prioridad de ejecución de procesos

## Overview
El comando `nice` en C Shell (csh) se utiliza para iniciar un proceso con una prioridad ajustada. Esto permite que los usuarios controlen la cantidad de recursos del sistema que un proceso puede utilizar, lo que es útil para evitar que un proceso consuma todos los recursos y afecte a otros procesos en ejecución.

## Usage
La sintaxis básica del comando `nice` es la siguiente:

```
nice [opciones] [comando] [argumentos]
```

## Common Options
- `-n` o `--adjustment`: Especifica el valor de ajuste de la prioridad. Puede ser un número entre -20 (máxima prioridad) y 19 (mínima prioridad).
- `-h` o `--help`: Muestra la ayuda sobre el uso del comando.
- `-v` o `--version`: Muestra la versión del comando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `nice`:

1. **Ejecutar un comando con prioridad normal:**
   ```csh
   nice ls -l
   ```

2. **Ejecutar un proceso con menor prioridad:**
   ```csh
   nice -n 10 ./mi_programa
   ```

3. **Ejecutar un proceso con mayor prioridad:**
   ```csh
   nice -n -5 ./mi_programa
   ```

4. **Verificar la prioridad de un proceso en ejecución:**
   ```csh
   ps -o pid,ni,cmd
   ```

## Tips
- Utiliza `nice` para ejecutar procesos que no son críticos en segundo plano, permitiendo que otros procesos más importantes tengan prioridad.
- Recuerda que solo los usuarios con privilegios adecuados pueden aumentar la prioridad de un proceso (valores negativos).
- Puedes combinar `nice` con otros comandos como `nohup` para ejecutar procesos en segundo plano sin que se interrumpan al cerrar la sesión.