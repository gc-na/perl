# [Linux] C Shell (csh) sed Uso: Herramienta para manipular texto

## Overview
El comando `sed` (Stream Editor) es una herramienta poderosa en Unix y Linux que permite realizar transformaciones de texto en un flujo de datos. Se utiliza comúnmente para buscar, reemplazar, insertar o eliminar texto en archivos o en la entrada estándar.

## Usage
La sintaxis básica del comando `sed` es la siguiente:

```bash
sed [opciones] [argumentos]
```

## Common Options
- `-e`: Permite especificar múltiples expresiones de edición.
- `-i`: Edita archivos en el lugar, modificando el archivo original.
- `-n`: Suprime la salida automática, permitiendo mostrar solo las líneas que coinciden con las expresiones.
- `s`: Realiza una sustitución de texto.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `sed`:

1. **Reemplazar texto en un archivo**:
   ```bash
   sed 's/hola/adiós/' archivo.txt
   ```
   Este comando reemplaza la primera aparición de "hola" por "adiós" en cada línea de `archivo.txt`.

2. **Reemplazar todas las apariciones de un texto**:
   ```bash
   sed 's/hola/adiós/g' archivo.txt
   ```
   Aquí, el modificador `g` indica que se deben reemplazar todas las apariciones de "hola" por "adiós".

3. **Eliminar líneas específicas**:
   ```bash
   sed '3d' archivo.txt
   ```
   Este comando elimina la tercera línea del archivo `archivo.txt`.

4. **Modificar un archivo en el lugar**:
   ```bash
   sed -i 's/hola/adiós/g' archivo.txt
   ```
   Con la opción `-i`, este comando reemplaza "hola" por "adiós" directamente en `archivo.txt`.

5. **Mostrar solo líneas que coinciden con un patrón**:
   ```bash
   sed -n '/hola/p' archivo.txt
   ```
   Este comando muestra solo las líneas que contienen "hola" en `archivo.txt`.

## Tips
- Siempre es recomendable hacer una copia de seguridad de los archivos antes de realizar ediciones en el lugar con `-i`.
- Utiliza comillas simples para evitar que el shell interprete caracteres especiales en las expresiones de `sed`.
- Prueba tus comandos de `sed` sin la opción `-i` primero para asegurarte de que los resultados sean los esperados.