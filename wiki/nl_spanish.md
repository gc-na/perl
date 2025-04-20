# [Linux] C Shell (csh) nl <Uso equivalente en español>: numerar líneas en archivos de texto

## Overview
El comando `nl` se utiliza para numerar las líneas de un archivo de texto. Este comando es útil para agregar números de línea a la salida, lo que facilita la referencia a líneas específicas en documentos largos.

## Usage
La sintaxis básica del comando `nl` es la siguiente:

```bash
nl [opciones] [argumentos]
```

## Common Options
- `-b`: Especifica el tipo de numeración de líneas. Puede ser `a` para numerar todas las líneas, `t` para numerar solo las líneas que no están en blanco, o `n` para no numerar.
- `-f`: Indica que se debe numerar cada archivo de forma independiente.
- `-h`: Permite especificar un encabezado que se mostrará antes de los números de línea.
- `-v`: Establece el número inicial para la numeración de líneas.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `nl`:

1. Numerar todas las líneas de un archivo:
   ```bash
   nl archivo.txt
   ```

2. Numerar solo las líneas no vacías:
   ```bash
   nl -b t archivo.txt
   ```

3. Comenzar la numeración desde un número específico:
   ```bash
   nl -v 100 archivo.txt
   ```

4. Numerar líneas y agregar un encabezado:
   ```bash
   nl -h "Encabezado:" archivo.txt
   ```

5. Numerar líneas de múltiples archivos:
   ```bash
   nl archivo1.txt archivo2.txt
   ```

## Tips
- Utiliza la opción `-b t` si solo deseas numerar líneas que contienen texto, lo que puede ser útil para mejorar la legibilidad.
- Combina `nl` con otros comandos como `grep` o `less` para filtrar y visualizar líneas numeradas de manera más efectiva.
- Recuerda que `nl` no modifica el archivo original; simplemente muestra la salida numerada en la terminal. Si deseas guardar la salida, redirige el resultado a un nuevo archivo.