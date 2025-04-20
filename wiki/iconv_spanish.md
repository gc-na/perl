# [Linux] C Shell (csh) iconv uso: Conversión de codificación de caracteres

## Overview
El comando `iconv` se utiliza para convertir la codificación de caracteres de archivos de texto. Permite transformar el contenido de un archivo de una codificación a otra, lo que es especialmente útil al trabajar con diferentes sistemas y aplicaciones que pueden requerir formatos específicos.

## Usage
La sintaxis básica del comando `iconv` es la siguiente:

```csh
iconv [opciones] [argumentos]
```

## Common Options
- `-f, --from-code=CODIFICACIÓN`: Especifica la codificación de entrada.
- `-t, --to-code=CODIFICACIÓN`: Especifica la codificación de salida.
- `-o, --output=ARCHIVO`: Redirige la salida a un archivo en lugar de la salida estándar.
- `-c`: Omite caracteres que no se pueden convertir.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `iconv`:

1. **Convertir de UTF-8 a ISO-8859-1**:
   ```csh
   iconv -f UTF-8 -t ISO-8859-1 archivo_entrada.txt -o archivo_salida.txt
   ```

2. **Convertir de Windows-1252 a UTF-8**:
   ```csh
   iconv -f WINDOWS-1252 -t UTF-8 archivo_entrada.txt -o archivo_salida.txt
   ```

3. **Convertir y omitir caracteres no convertibles**:
   ```csh
   iconv -f UTF-8 -t ASCII//TRANSLIT -c archivo_entrada.txt -o archivo_salida.txt
   ```

4. **Convertir un archivo y mostrar la salida en la consola**:
   ```csh
   iconv -f UTF-8 -t UTF-16 archivo_entrada.txt
   ```

## Tips
- Siempre verifica las codificaciones de entrada y salida para evitar pérdida de datos.
- Usa la opción `-o` para guardar la salida en un archivo y evitar sobrescribir el archivo original.
- Realiza pruebas con archivos pequeños antes de convertir archivos grandes para asegurarte de que el resultado sea el esperado.