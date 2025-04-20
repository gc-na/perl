# [Linux] C Shell (csh) nohup uso: Ejecutar comandos sin interrupciones

## Overview
El comando `nohup` se utiliza en el C Shell para ejecutar procesos que deben continuar funcionando incluso después de que el usuario haya cerrado la sesión. Esto es especialmente útil para tareas de larga duración que no deben ser interrumpidas.

## Usage
La sintaxis básica del comando `nohup` es la siguiente:

```csh
nohup [opciones] [argumentos]
```

## Common Options
- `&`: Ejecuta el comando en segundo plano.
- `-h`: Muestra la ayuda sobre el uso del comando.
- `-v`: Muestra información detallada sobre el comando.

## Common Examples
1. Ejecutar un script en segundo plano y asegurarse de que no se interrumpa al cerrar la sesión:
   ```csh
   nohup ./mi_script.sh &
   ```

2. Redirigir la salida a un archivo específico:
   ```csh
   nohup ./mi_programa > salida.txt &
   ```

3. Ejecutar un comando de larga duración:
   ```csh
   nohup tar -czf respaldo.tar.gz /ruta/del/directorio &
   ```

## Tips
- Siempre redirige la salida de tu comando a un archivo para evitar que se pierda información.
- Usa el símbolo `&` para ejecutar el comando en segundo plano y liberar la terminal.
- Revisa el archivo `nohup.out` si no especificaste un archivo de salida, ya que ahí se guardará la salida por defecto.