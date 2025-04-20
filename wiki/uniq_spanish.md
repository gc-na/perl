# [Linux] C Shell (csh) uniq Uso: Eliminar líneas duplicadas en un archivo

## Overview
El comando `uniq` se utiliza para eliminar líneas duplicadas consecutivas en un archivo de texto. Es especialmente útil cuando se trabaja con listas o datos que pueden contener entradas repetidas.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
uniq [opciones] [archivo]
```

## Common Options
- `-c`: Cuenta el número de ocurrencias de cada línea.
- `-d`: Muestra solo las líneas que son duplicadas.
- `-u`: Muestra solo las líneas que son únicas.
- `-i`: Ignora la distinción entre mayúsculas y minúsculas.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `uniq`:

1. **Eliminar líneas duplicadas de un archivo:**
   ```csh
   uniq archivo.txt
   ```

2. **Contar las ocurrencias de cada línea:**
   ```csh
   uniq -c archivo.txt
   ```

3. **Mostrar solo líneas duplicadas:**
   ```csh
   uniq -d archivo.txt
   ```

4. **Mostrar solo líneas únicas:**
   ```csh
   uniq -u archivo.txt
   ```

5. **Ignorar mayúsculas y minúsculas:**
   ```csh
   uniq -i archivo.txt
   ```

## Tips
- Asegúrate de que el archivo de entrada esté ordenado antes de usar `uniq`, ya que solo elimina duplicados consecutivos.
- Puedes combinar `uniq` con otros comandos como `sort` para obtener mejores resultados. Por ejemplo:
  ```csh
  sort archivo.txt | uniq
  ```
- Utiliza la opción `-c` para obtener un resumen de cuántas veces aparece cada línea, lo que puede ser útil para análisis rápidos de datos.