# [Linux] C Shell (csh) wget Uso: Descargar archivos de la web

## Overview
El comando `wget` es una herramienta de línea de comandos utilizada para descargar archivos de la web. Es especialmente útil para recuperar contenido de sitios web y soporta descargas recursivas, lo que permite obtener archivos de manera eficiente.

## Usage
La sintaxis básica del comando `wget` es la siguiente:

```bash
wget [opciones] [argumentos]
```

## Common Options
Aquí hay algunas opciones comunes que puedes utilizar con `wget`:

- `-O <archivo>`: Especifica el nombre del archivo de salida.
- `-c`: Continúa una descarga interrumpida.
- `-r`: Descarga recursivamente.
- `-p`: Descarga todos los elementos necesarios para mostrar la página HTML.
- `--limit-rate=<tasa>`: Limita la velocidad de descarga.

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso de `wget`:

1. **Descargar un archivo simple:**

   ```bash
   wget https://ejemplo.com/archivo.zip
   ```

2. **Descargar un archivo y guardarlo con un nombre específico:**

   ```bash
   wget -O mi_archivo.zip https://ejemplo.com/archivo.zip
   ```

3. **Continuar una descarga interrumpida:**

   ```bash
   wget -c https://ejemplo.com/archivo.zip
   ```

4. **Descargar una página web y todos sus recursos:**

   ```bash
   wget -p https://ejemplo.com/pagina
   ```

5. **Descargar un sitio web de forma recursiva:**

   ```bash
   wget -r https://ejemplo.com/sitio
   ```

## Tips
- Siempre verifica la URL antes de descargar para asegurarte de que es la correcta.
- Usa la opción `-c` para evitar perder tiempo en descargas largas que pueden interrumpirse.
- Considera limitar la velocidad de descarga con `--limit-rate` si estás en una conexión compartida para no saturar el ancho de banda.