# [Linux] C Shell (csh) trap uso: Captura señales y maneja la terminación de procesos

## Overview
El comando `trap` en C Shell (csh) se utiliza para capturar señales y manejar la terminación de procesos. Permite ejecutar comandos específicos cuando el script recibe ciertas señales, lo que es útil para limpiar recursos o realizar acciones antes de que el script termine.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
trap [options] [arguments]
```

## Common Options
- `signal`: Especifica la señal que se desea capturar (por ejemplo, `INT` para interrupciones).
- `command`: El comando que se ejecutará cuando se reciba la señal especificada.
- `-`: Elimina el manejo de la señal especificada.

## Common Examples

### Ejemplo 1: Capturar la señal de interrupción
Este ejemplo muestra cómo capturar la señal de interrupción (Ctrl+C) y ejecutar un comando específico.

```csh
trap 'echo "Interrupción capturada. Saliendo..."' INT
```

### Ejemplo 2: Limpiar archivos temporales
En este caso, se utiliza `trap` para eliminar archivos temporales cuando el script se termina.

```csh
trap 'rm -f /tmp/tempfile' EXIT
```

### Ejemplo 3: Manejo de múltiples señales
Aquí se captura tanto la señal de interrupción como la de terminación y se ejecutan diferentes comandos.

```csh
trap 'echo "Interrupción capturada. Saliendo..."' INT
trap 'echo "Terminación capturada. Limpiando..."' TERM
```

## Tips
- Siempre es una buena práctica limpiar los recursos al finalizar un script, utilizando `trap` para manejar señales como `EXIT`.
- Puedes usar `trap` para depurar scripts, mostrando mensajes cuando se reciben señales inesperadas.
- Recuerda que algunas señales no pueden ser capturadas, como `KILL`, así que asegúrate de manejar solo aquellas que son relevantes para tu script.