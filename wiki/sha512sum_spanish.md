# [Linux] C Shell (csh) sha512sum Uso: Calcular el hash SHA-512 de archivos

## Overview
El comando `sha512sum` se utiliza para calcular y verificar el hash SHA-512 de archivos. Este hash es una representación única del contenido del archivo, lo que permite comprobar su integridad y autenticidad.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
sha512sum [options] [arguments]
```

## Common Options
- `-b`: Lee el archivo en modo binario.
- `-c`: Verifica los hashes de los archivos listados en un archivo de suma.
- `-h`: Muestra la ayuda y la información sobre el uso del comando.
- `--tag`: Produce una salida en formato de etiqueta.

## Common Examples

1. **Calcular el hash SHA-512 de un archivo:**
   ```csh
   sha512sum archivo.txt
   ```

2. **Calcular el hash de varios archivos:**
   ```csh
   sha512sum archivo1.txt archivo2.txt
   ```

3. **Verificar un archivo usando un archivo de suma:**
   Primero, crea un archivo de suma:
   ```csh
   sha512sum archivo.txt > archivo.sha512
   ```
   Luego, verifica el archivo:
   ```csh
   sha512sum -c archivo.sha512
   ```

4. **Leer un archivo en modo binario:**
   ```csh
   sha512sum -b archivo.bin
   ```

## Tips
- Siempre verifica los hashes después de transferir archivos importantes para asegurarte de que no se hayan corrompido.
- Utiliza el modo binario para archivos no de texto para evitar problemas de codificación.
- Guarda los hashes en un archivo para facilitar la verificación futura.