# [Linux] C Shell (csh) cp Uso: Copiar archivos y directorios

## Overview
El comando `cp` se utiliza en C Shell (csh) para copiar archivos y directorios de un lugar a otro en el sistema de archivos. Es una herramienta fundamental para la gestión de archivos en sistemas Unix y Linux.

## Usage
La sintaxis básica del comando `cp` es la siguiente:

```bash
cp [opciones] [orígenes] [destino]
```

## Common Options
- `-i`: Pregunta antes de sobrescribir un archivo existente.
- `-r`: Copia directorios de forma recursiva.
- `-u`: Solo copia archivos que son más nuevos que los archivos de destino o que no existen en el destino.
- `-v`: Muestra los archivos que se están copiando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `cp`:

1. **Copiar un archivo a otro directorio:**
   ```bash
   cp archivo.txt /ruta/al/destino/
   ```

2. **Copiar un archivo y renombrarlo:**
   ```bash
   cp archivo.txt nuevo_archivo.txt
   ```

3. **Copiar un directorio de forma recursiva:**
   ```bash
   cp -r /ruta/al/directorio /ruta/al/nuevo_directorio
   ```

4. **Copiar un archivo y preguntar antes de sobrescribir:**
   ```bash
   cp -i archivo.txt /ruta/al/destino/
   ```

5. **Copiar solo archivos más nuevos:**
   ```bash
   cp -u archivo.txt /ruta/al/destino/
   ```

## Tips
- Siempre verifica la ruta de destino para evitar sobrescribir archivos importantes.
- Usa la opción `-v` para tener un registro visual de los archivos que se están copiando.
- Si trabajas con directorios, recuerda usar la opción `-r` para asegurarte de que se copien todos los archivos y subdirectorios.