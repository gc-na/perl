# [Linux] C Shell (csh) cmp Uso: Comparar archivos byte a byte

## Overview
El comando `cmp` se utiliza para comparar dos archivos byte a byte. Su función principal es identificar las diferencias entre los archivos, indicando la primera posición donde difieren y, si se desea, también puede mostrar las diferencias en formato hexadecimal.

## Usage
La sintaxis básica del comando `cmp` es la siguiente:

```
cmp [opciones] [archivo1] [archivo2]
```

## Common Options
- `-l`: Muestra las diferencias en formato octal.
- `-s`: Silencia la salida, solo devuelve el estado de salida.
- `-i OFFSET`: Comienza la comparación a partir de un desplazamiento específico.
- `-n NUM`: Compara solo los primeros NUM bytes de los archivos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `cmp`:

1. Comparar dos archivos y mostrar la primera diferencia:
   ```csh
   cmp archivo1.txt archivo2.txt
   ```

2. Comparar dos archivos sin mostrar la salida, solo el estado:
   ```csh
   cmp -s archivo1.txt archivo2.txt
   ```

3. Comparar solo los primeros 100 bytes de dos archivos:
   ```csh
   cmp -n 100 archivo1.txt archivo2.txt
   ```

4. Comparar dos archivos y mostrar las diferencias en formato octal:
   ```csh
   cmp -l archivo1.txt archivo2.txt
   ```

## Tips
- Utiliza la opción `-s` si solo necesitas saber si los archivos son diferentes sin necesidad de ver detalles.
- Si trabajas con archivos grandes y solo necesitas verificar una parte, la opción `-n` es muy útil.
- Recuerda que `cmp` es sensible a mayúsculas y minúsculas, así que ten cuidado al comparar archivos con nombres similares.