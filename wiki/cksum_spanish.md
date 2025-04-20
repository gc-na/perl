# [Linux] C Shell (csh) cksum: Calcular y mostrar el checksum de archivos

## Overview
El comando `cksum` en C Shell (csh) se utiliza para calcular y mostrar el checksum de un archivo, así como su tamaño en bytes. Este checksum es útil para verificar la integridad de los datos.

## Usage
La sintaxis básica del comando es la siguiente:

```
cksum [opciones] [argumentos]
```

## Common Options
- `-a, --algorithm=ALGO`: Especifica el algoritmo de checksum a utilizar.
- `-h, --help`: Muestra la ayuda sobre el uso del comando.
- `-V, --version`: Muestra la versión del comando.

## Common Examples
1. Calcular el checksum de un archivo específico:
   ```csh
   cksum archivo.txt
   ```

2. Calcular el checksum de múltiples archivos:
   ```csh
   cksum archivo1.txt archivo2.txt
   ```

3. Usar el algoritmo SHA256 para calcular el checksum:
   ```csh
   cksum -a sha256 archivo.txt
   ```

4. Mostrar la ayuda del comando:
   ```csh
   cksum --help
   ```

## Tips
- Asegúrate de tener permisos de lectura en los archivos para los que deseas calcular el checksum.
- Utiliza `cksum` en combinación con otros comandos como `diff` para verificar cambios en archivos.
- Guarda el resultado del checksum en un archivo para futuras comparaciones.