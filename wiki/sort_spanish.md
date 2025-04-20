# [Linux] C Shell (csh) sort Uso: Ordenar líneas de texto

## Overview
El comando `sort` se utiliza en C Shell (csh) para ordenar líneas de texto en un archivo o desde la entrada estándar. Es una herramienta útil para organizar datos, ya sea en orden alfabético, numérico o según otros criterios.

## Usage
La sintaxis básica del comando `sort` es la siguiente:

```csh
sort [opciones] [argumentos]
```

## Common Options
- `-r`: Ordenar en orden inverso.
- `-n`: Ordenar numéricamente en lugar de alfabéticamente.
- `-k`: Especificar la clave de ordenación (por ejemplo, la columna a ordenar).
- `-u`: Eliminar líneas duplicadas en el resultado.
- `-o`: Especificar un archivo de salida para guardar el resultado.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `sort`:

1. **Ordenar un archivo alfabéticamente**:
   ```csh
   sort archivo.txt
   ```

2. **Ordenar un archivo numéricamente**:
   ```csh
   sort -n numeros.txt
   ```

3. **Ordenar en orden inverso**:
   ```csh
   sort -r lista.txt
   ```

4. **Ordenar por una columna específica**:
   ```csh
   sort -k 2 datos.txt
   ```

5. **Eliminar líneas duplicadas y ordenar**:
   ```csh
   sort -u lista.txt
   ```

6. **Guardar el resultado en un nuevo archivo**:
   ```csh
   sort -o ordenado.txt archivo.txt
   ```

## Tips
- Siempre verifica el contenido del archivo original antes de realizar una ordenación, especialmente si usas la opción `-o`, ya que sobrescribirá el archivo de salida.
- Combina `sort` con otros comandos como `uniq` para obtener resultados más refinados.
- Utiliza `man sort` en la terminal para obtener más información sobre las opciones disponibles y ejemplos adicionales.