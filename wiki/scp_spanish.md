# [Linux] C Shell (csh) scp Uso: Copiar archivos de forma segura

## Overview
El comando `scp` (secure copy) se utiliza para copiar archivos y directorios de manera segura entre sistemas a través de una red. Utiliza el protocolo SSH para garantizar que la transferencia de datos sea segura.

## Usage
La sintaxis básica del comando `scp` es la siguiente:

```bash
scp [opciones] [origen] [destino]
```

## Common Options
- `-r`: Copia directorios de forma recursiva.
- `-P`: Especifica el puerto a utilizar en el servidor remoto.
- `-i`: Permite especificar un archivo de clave privada para la autenticación.
- `-v`: Muestra información detallada sobre el proceso de copia (modo verbose).

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `scp`:

1. **Copiar un archivo local a un servidor remoto:**
   ```bash
   scp archivo.txt usuario@servidor:/ruta/destino/
   ```

2. **Copiar un archivo de un servidor remoto a la máquina local:**
   ```bash
   scp usuario@servidor:/ruta/origen/archivo.txt /ruta/local/
   ```

3. **Copiar un directorio completo a un servidor remoto:**
   ```bash
   scp -r /ruta/local/directorio usuario@servidor:/ruta/destino/
   ```

4. **Copiar un archivo especificando un puerto diferente:**
   ```bash
   scp -P 2222 archivo.txt usuario@servidor:/ruta/destino/
   ```

## Tips
- Asegúrate de tener acceso SSH al servidor remoto antes de usar `scp`.
- Utiliza la opción `-v` para depurar problemas de conexión si no puedes transferir archivos.
- Considera usar claves SSH para una autenticación más segura y evitar tener que ingresar la contraseña cada vez.