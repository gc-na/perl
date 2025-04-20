# [Unix] C Shell (csh) comm: Comparar líneas de archivos

## Overview
El comando `comm` se utiliza para comparar dos archivos de texto ordenados línea por línea. Este comando muestra las líneas que son únicas para cada archivo y las que son comunes entre ellos.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
comm [opciones] [archivo1] [archivo2]
```

## Common Options
- `-1`: Suprime las líneas que son únicas para el primer archivo.
- `-2`: Suprime las líneas que son únicas para el segundo archivo.
- `-3`: Suprime las líneas que son comunes a ambos archivos.
- `--nocheck-order`: Permite que los archivos no estén ordenados.

## Common Examples

### Ejemplo 1: Comparar dos archivos
Supongamos que tenemos dos archivos, `archivo1.txt` y `archivo2.txt`, y queremos ver las diferencias entre ellos.

```csh
comm archivo1.txt archivo2.txt
```

### Ejemplo 2: Mostrar solo líneas únicas del segundo archivo
Si solo queremos ver las líneas que están en `archivo2.txt` y no en `archivo1.txt`, podemos usar la opción `-2`.

```csh
comm -2 archivo1.txt archivo2.txt
```

### Ejemplo 3: Mostrar solo líneas comunes
Para mostrar solo las líneas que aparecen en ambos archivos, utilizamos la opción `-1` y `-2`.

```csh
comm -12 archivo1.txt archivo2.txt
```

### Ejemplo 4: Comparar archivos no ordenados
Si los archivos no están ordenados, podemos usar la opción `--nocheck-order`.

```csh
comm --nocheck-order archivo1.txt archivo2.txt
```

## Tips
- Asegúrate de que los archivos estén ordenados antes de usar `comm` para obtener resultados precisos.
- Puedes combinar opciones para personalizar la salida según tus necesidades.
- Utiliza `sort` para ordenar los archivos si no están en orden antes de compararlos:

```csh
sort archivo1.txt > archivo1_ordenado.txt
sort archivo2.txt > archivo2_ordenado.txt
comm archivo1_ordenado.txt archivo2_ordenado.txt
```