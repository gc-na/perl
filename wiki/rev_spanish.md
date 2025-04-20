# [Linux] C Shell (csh) rev: Invertir líneas de texto

## Overview
El comando `rev` se utiliza para invertir el orden de los caracteres en cada línea de un archivo o entrada estándar. Es útil para manipular texto y puede ser empleado en diversas tareas de procesamiento de datos.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
rev [opciones] [argumentos]
```

## Common Options
- `-o, --output=FILE`: Especifica un archivo de salida donde se guardará el resultado.
- `-h, --help`: Muestra la ayuda y una lista de opciones disponibles.
- `-V, --version`: Muestra la versión del comando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `rev`:

1. Invertir el contenido de un archivo llamado `texto.txt` y mostrarlo en la terminal:

    ```csh
    rev texto.txt
    ```

2. Invertir el contenido de un archivo y guardarlo en otro archivo llamado `invertido.txt`:

    ```csh
    rev texto.txt > invertido.txt
    ```

3. Invertir una cadena de texto ingresada directamente desde la línea de comandos:

    ```csh
    echo "Hola Mundo" | rev
    ```

4. Invertir el contenido de un archivo y mostrar solo las primeras 5 líneas:

    ```csh
    rev texto.txt | head -n 5
    ```

## Tips
- Recuerda que `rev` procesa línea por línea, por lo que cada línea se invertirá de forma independiente.
- Puedes combinar `rev` con otros comandos de Unix para realizar tareas más complejas, como filtrado o redirección.
- Asegúrate de tener permisos de lectura en el archivo que deseas invertir, y de escritura en el archivo de salida si lo estás redirigiendo.