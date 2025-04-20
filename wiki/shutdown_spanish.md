# [Linux] C Shell (csh) shutdown uso: Apagar el sistema

## Overview
El comando `shutdown` en C Shell (csh) se utiliza para apagar o reiniciar el sistema de manera controlada. Permite a los administradores del sistema programar el apagado y notificar a los usuarios sobre la inminente interrupción del servicio.

## Usage
La sintaxis básica del comando es la siguiente:

```
shutdown [opciones] [argumentos]
```

## Common Options
- `-h`: Apagar el sistema.
- `-r`: Reiniciar el sistema.
- `-k`: Notificar a los usuarios sin apagar el sistema.
- `time`: Especifica el tiempo para el apagado (puede ser un número de minutos o un formato como "now" para inmediato).
- `message`: Mensaje opcional que se enviará a los usuarios antes del apagado.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `shutdown`:

1. Apagar el sistema inmediatamente:
   ```csh
   shutdown -h now
   ```

2. Reiniciar el sistema en 5 minutos:
   ```csh
   shutdown -r +5
   ```

3. Notificar a los usuarios que el sistema se apagará en 10 minutos:
   ```csh
   shutdown -h +10 "El sistema se apagará en 10 minutos. Guarde su trabajo."
   ```

4. Enviar un aviso sin apagar el sistema:
   ```csh
   shutdown -k now "Mantenimiento programado, el sistema no se apagará."
   ```

## Tips
- Siempre notifica a los usuarios antes de un apagado programado para evitar la pérdida de datos.
- Utiliza el mensaje para proporcionar información clara sobre el motivo del apagado o reinicio.
- Prueba el comando en un entorno de prueba antes de usarlo en un sistema de producción para familiarizarte con su comportamiento.