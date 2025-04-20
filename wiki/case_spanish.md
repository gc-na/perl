# [Linux] C Shell (csh) case <Uso equivalente en español>: Evaluar patrones de cadena

## Overview
El comando `case` en C Shell (csh) se utiliza para evaluar patrones de cadena y ejecutar diferentes bloques de código según el patrón que coincida. Es similar a una estructura de control de flujo que permite manejar múltiples condiciones de manera más organizada.

## Usage
La sintaxis básica del comando `case` es la siguiente:

```csh
case expresión in
    patrón1) comandos1 ;;
    patrón2) comandos2 ;;
    ...
    *) comandos_por_defecto ;;
esac
```

## Common Options
El comando `case` no tiene opciones específicas, pero se basa en patrones que puedes definir. Los patrones pueden incluir caracteres comodín como `*` y `?`.

## Common Examples

### Ejemplo 1: Evaluar un número
```csh
set num = 2
switch ($num)
    case 1:
        echo "El número es uno."
        breaksw
    case 2:
        echo "El número es dos."
        breaksw
    default:
        echo "Número no reconocido."
endsw
```

### Ejemplo 2: Evaluar una cadena
```csh
set color = "rojo"
switch ($color)
    case "rojo":
        echo "El color es rojo."
        breaksw
    case "verde":
        echo "El color es verde."
        breaksw
    default:
        echo "Color no reconocido."
endsw
```

### Ejemplo 3: Usar comodines
```csh
set archivo = "documento.txt"
switch ($archivo)
    case "*.txt":
        echo "Es un archivo de texto."
        breaksw
    case "*.jpg":
        echo "Es una imagen JPEG."
        breaksw
    default:
        echo "Tipo de archivo no reconocido."
endsw
```

## Tips
- Utiliza `breaksw` para salir de la estructura `switch` una vez que se haya ejecutado un bloque de comandos.
- Recuerda que los patrones son evaluados en orden, por lo que el orden de los casos puede afectar el resultado.
- Los comodines como `*` y `?` pueden ser muy útiles para hacer coincidir varios patrones con una sola línea de código.