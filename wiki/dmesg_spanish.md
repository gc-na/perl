# [Linux] C Shell (csh) dmesg Uso: Muestra mensajes del núcleo del sistema

## Overview
El comando `dmesg` se utiliza para mostrar los mensajes del núcleo del sistema, que incluyen información sobre el hardware, controladores y otros eventos del sistema. Es especialmente útil para diagnosticar problemas relacionados con el arranque y la configuración del hardware.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
dmesg [opciones] [argumentos]
```

## Common Options
- `-c`: Borra el búfer de mensajes después de mostrarlos.
- `-n nivel`: Establece el nivel de prioridad de los mensajes que se mostrarán.
- `-T`: Convierte las marcas de tiempo en un formato legible por humanos.
- `-s tamaño`: Establece el tamaño del búfer en bytes.

## Common Examples
- Para mostrar todos los mensajes del núcleo:
  ```csh
  dmesg
  ```

- Para mostrar los mensajes del núcleo con marcas de tiempo legibles:
  ```csh
  dmesg -T
  ```

- Para borrar el búfer de mensajes después de mostrarlos:
  ```csh
  dmesg -c
  ```

- Para establecer el nivel de prioridad a 3 (solo mensajes de advertencia y errores):
  ```csh
  dmesg -n 3
  ```

## Tips
- Utiliza `dmesg -T` para facilitar la lectura de los mensajes, especialmente si estás revisando registros antiguos.
- Revisa los mensajes de `dmesg` después de un arranque para identificar problemas de hardware o controladores.
- Puedes redirigir la salida de `dmesg` a un archivo para un análisis posterior:
  ```csh
  dmesg > dmesg_output.txt
  ```