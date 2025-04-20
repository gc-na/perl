# [Linux] C Shell (csh) mtr Uso: Herramienta de diagnóstico de red

## Overview
El comando `mtr` combina las funcionalidades de `ping` y `traceroute` para proporcionar información sobre la ruta que toman los paquetes de datos hacia un destino específico. Es útil para diagnosticar problemas de red y analizar la calidad de la conexión.

## Usage
La sintaxis básica del comando `mtr` es la siguiente:

```csh
mtr [opciones] [destino]
```

## Common Options
- `-r`: Muestra un resumen de la ruta y los tiempos de respuesta.
- `-c [n]`: Especifica el número de pings a enviar, donde `[n]` es un número entero.
- `-i [segundos]`: Establece el intervalo entre pings en segundos.
- `-w`: Muestra la salida en formato de ancho ajustado, facilitando la lectura.

## Common Examples
- Para realizar un diagnóstico básico hacia un host, como `google.com`:

```csh
mtr google.com
```

- Para enviar 10 pings y mostrar un resumen al final:

```csh
mtr -r -c 10 google.com
```

- Para establecer un intervalo de 2 segundos entre pings:

```csh
mtr -i 2 google.com
```

- Para mostrar la salida en un formato más legible:

```csh
mtr -w google.com
```

## Tips
- Utiliza la opción `-r` para obtener un resumen rápido después de realizar múltiples pings.
- Experimenta con diferentes intervalos de tiempo usando `-i` para observar cómo varían los tiempos de respuesta.
- Revisa la documentación completa de `mtr` para descubrir más opciones avanzadas que pueden ser útiles en situaciones específicas.