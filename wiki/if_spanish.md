# [Unix] C Shell (csh) if: Evaluar condiciones

## Overview
El comando `if` en C Shell (csh) se utiliza para evaluar condiciones y ejecutar comandos basados en el resultado de esa evaluación. Permite tomar decisiones en los scripts de shell, facilitando la automatización de tareas.

## Usage
La sintaxis básica del comando `if` es la siguiente:

```
if ( condición ) then
    comandos
endif
```

## Common Options
Aunque el comando `if` en sí no tiene muchas opciones, se pueden utilizar diferentes operadores para evaluar condiciones. Algunos de los más comunes son:

- `-e`: Verifica si un archivo existe.
- `-d`: Verifica si un directorio existe.
- `-f`: Verifica si un archivo es un archivo regular.
- `==`: Compara dos cadenas de texto.

## Common Examples

### Ejemplo 1: Verificar la existencia de un archivo
```csh
if ( -e archivo.txt ) then
    echo "El archivo existe."
endif
```

### Ejemplo 2: Comprobar si un directorio existe
```csh
if ( -d /ruta/al/directorio ) then
    echo "El directorio existe."
endif
```

### Ejemplo 3: Comparar cadenas
```csh
set nombre = "Juan"
if ( $nombre == "Juan" ) then
    echo "Hola, Juan."
endif
```

### Ejemplo 4: Verificar si un archivo es un archivo regular
```csh
if ( -f archivo.txt ) then
    echo "Es un archivo regular."
else
    echo "No es un archivo regular."
endif
```

## Tips
- Siempre asegúrate de cerrar el bloque `if` con `endif` para evitar errores de sintaxis.
- Utiliza paréntesis alrededor de la condición para garantizar que se evalúe correctamente.
- Puedes anidar múltiples condiciones `if` para crear lógica más compleja en tus scripts.