# [Linux] C Shell (csh) switch uso: Cambiar entre opciones de un comando

## Overview
El comando `switch` en C Shell (csh) se utiliza para realizar selecciones condicionales en scripts. Permite evaluar una expresión y ejecutar diferentes bloques de código según el valor de esa expresión.

## Usage
La sintaxis básica del comando `switch` es la siguiente:

```csh
switch (expresión)
    case patrón1:
        # comandos a ejecutar si la expresión coincide con patrón1
        breaksw
    case patrón2:
        # comandos a ejecutar si la expresión coincide con patrón2
        breaksw
    default:
        # comandos a ejecutar si no hay coincidencias
        breaksw
endsw
```

## Common Options
El comando `switch` no tiene opciones específicas, pero se utilizan patrones en las cláusulas `case` para determinar las coincidencias. Aquí hay algunas consideraciones sobre los patrones:

- `*`: Coincide con cualquier cadena.
- `?`: Coincide con un solo carácter.
- `[abc]`: Coincide con cualquier carácter dentro de los corchetes.

## Common Examples

### Ejemplo 1: Selección simple
```csh
set variable = "manzana"
switch ($variable)
    case "manzana":
        echo "Es una manzana."
        breaksw
    case "naranja":
        echo "Es una naranja."
        breaksw
    default:
        echo "No es ni una manzana ni una naranja."
        breaksw
endsw
```

### Ejemplo 2: Uso de patrones
```csh
set archivo = "documento.txt"
switch ($archivo)
    case "*.txt":
        echo "Es un archivo de texto."
        breaksw
    case "*.jpg":
        echo "Es una imagen JPG."
        breaksw
    default:
        echo "Tipo de archivo desconocido."
        breaksw
endsw
```

### Ejemplo 3: Múltiples coincidencias
```csh
set dia = "lunes"
switch ($dia)
    case "lunes":
    case "martes":
        echo "Es un día de la semana laboral."
        breaksw
    case "sábado":
    case "domingo":
        echo "Es un día del fin de semana."
        breaksw
    default:
        echo "Día no reconocido."
        breaksw
endsw
```

## Tips
- Asegúrate de usar `breaksw` al final de cada caso para evitar que se ejecuten las instrucciones de los siguientes casos.
- Utiliza patrones adecuados para hacer coincidir múltiples valores de manera efectiva.
- Mantén el código dentro de cada caso claro y conciso para mejorar la legibilidad.