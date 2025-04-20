# [Unix] C Shell (csh) while: Ejecutar comandos repetidamente

## Overview
El comando `while` en C Shell (csh) se utiliza para ejecutar un bloque de comandos de manera repetitiva mientras se cumpla una condición específica. Es útil para realizar tareas que requieren repetición hasta que se alcance un estado deseado.

## Usage
La sintaxis básica del comando `while` es la siguiente:

```
while ( condición )
    comando1
    comando2
    ...
end
```

## Common Options
El comando `while` no tiene opciones específicas, pero se puede utilizar con condiciones que evalúan expresiones o comandos. Las condiciones pueden incluir comparaciones numéricas, verificaciones de archivos, etc.

## Common Examples

### Ejemplo 1: Contador simple
Este ejemplo muestra cómo usar `while` para contar hasta 5.

```csh
set i = 1
while ( $i <= 5 )
    echo "Contador: $i"
    @ i++
end
```

### Ejemplo 2: Leer archivos hasta el final
Este ejemplo ilustra cómo leer líneas de un archivo hasta que se alcance el final.

```csh
set file = "mi_archivo.txt"
set line = ""
while ( "$line" != "" )
    set line = `head -n 1 $file`
    echo $line
    set file = `tail -n +2 $file`
end
```

### Ejemplo 3: Esperar hasta que un archivo exista
Este ejemplo espera hasta que un archivo específico sea creado.

```csh
set archivo = "archivo.txt"
while ( ! -e $archivo )
    echo "Esperando a que el archivo $archivo exista..."
    sleep 2
end
echo "El archivo $archivo ha sido creado."
```

## Tips
- Asegúrate de que la condición en el `while` se pueda evaluar correctamente para evitar bucles infinitos.
- Utiliza `sleep` dentro del bucle si estás esperando un evento externo, para no sobrecargar la CPU.
- Recuerda que el bloque de comandos debe estar correctamente indentado para mejorar la legibilidad.