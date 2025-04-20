# [Linux] C Shell (csh) awk Uso: Procesamiento de texto y análisis de datos

## Overview
El comando `awk` es una poderosa herramienta de procesamiento de texto y análisis de datos en sistemas Unix y Linux. Permite manipular y extraer información de archivos de texto, facilitando tareas como la búsqueda, el filtrado y la generación de informes.

## Usage
La sintaxis básica del comando `awk` es la siguiente:

```bash
awk [opciones] [argumentos]
```

## Common Options
- `-F`: Especifica el delimitador de campo. Por defecto, `awk` utiliza espacios en blanco.
- `-v`: Permite definir variables antes de ejecutar el script `awk`.
- `-f`: Indica que se va a utilizar un archivo que contiene el script `awk`.
- `-W`: Activa opciones específicas de `awk`, como compatibilidad con versiones anteriores.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `awk`:

1. **Imprimir la primera columna de un archivo**:
   ```bash
   awk '{print $1}' archivo.txt
   ```

2. **Contar el número de líneas en un archivo**:
   ```bash
   awk 'END {print NR}' archivo.txt
   ```

3. **Filtrar líneas que contienen una palabra específica**:
   ```bash
   awk '/palabra/' archivo.txt
   ```

4. **Sumar valores de la segunda columna**:
   ```bash
   awk '{suma += $2} END {print suma}' archivo.txt
   ```

5. **Imprimir líneas donde el valor de la tercera columna es mayor que 100**:
   ```bash
   awk '$3 > 100' archivo.txt
   ```

## Tips
- Utiliza el delimitador adecuado con `-F` para trabajar con archivos CSV o con otros formatos.
- Aprovecha las variables definidas con `-v` para hacer tus scripts más dinámicos.
- Siempre prueba tus comandos en un archivo de muestra antes de aplicarlos a datos importantes para evitar pérdidas de información.