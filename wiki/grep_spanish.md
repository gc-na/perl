# [Linux] C Shell (csh) grep uso: Buscar texto en archivos

## Overview
El comando `grep` se utiliza para buscar patrones de texto dentro de archivos. Es una herramienta poderosa que permite filtrar líneas que coinciden con una expresión regular, facilitando la búsqueda de información específica en grandes volúmenes de datos.

## Usage
La sintaxis básica del comando `grep` es la siguiente:

```csh
grep [opciones] [argumentos]
```

## Common Options
- `-i`: Ignorar mayúsculas y minúsculas durante la búsqueda.
- `-v`: Invertir la búsqueda, mostrando líneas que no coinciden con el patrón.
- `-r`: Buscar recursivamente en directorios.
- `-n`: Mostrar el número de línea junto con las líneas coincidentes.
- `-l`: Listar solo los nombres de los archivos que contienen el patrón.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `grep`:

1. Buscar una palabra específica en un archivo:
   ```csh
   grep "palabra" archivo.txt
   ```

2. Buscar sin distinguir entre mayúsculas y minúsculas:
   ```csh
   grep -i "palabra" archivo.txt
   ```

3. Buscar en todos los archivos de un directorio:
   ```csh
   grep "palabra" *
   ```

4. Buscar recursivamente en un directorio:
   ```csh
   grep -r "palabra" /ruta/del/directorio
   ```

5. Mostrar el número de línea de las coincidencias:
   ```csh
   grep -n "palabra" archivo.txt
   ```

## Tips
- Usa `grep -v` para excluir líneas que contienen un patrón específico, lo que puede ser útil para filtrar resultados.
- Combina `grep` con otros comandos utilizando tuberías (`|`) para realizar búsquedas más complejas.
- Si buscas múltiples patrones, puedes usar `-e` para especificar cada patrón:
  ```csh
  grep -e "patrón1" -e "patrón2" archivo.txt
  ```