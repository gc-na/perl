# [Linux] C Shell (csh) parted Uso: Herramienta para gestionar particiones de disco

## Overview
El comando `parted` se utiliza para gestionar particiones en discos duros. Permite crear, eliminar, redimensionar y modificar particiones de manera eficiente, facilitando la administración del espacio en disco.

## Usage
La sintaxis básica del comando `parted` es la siguiente:

```bash
parted [options] [arguments]
```

## Common Options
- `-l`: Lista todas las particiones en todos los dispositivos.
- `-s`: Ejecuta `parted` en modo silencioso, sin mostrar mensajes adicionales.
- `mkpart`: Crea una nueva partición.
- `rm`: Elimina una partición existente.
- `resizepart`: Redimensiona una partición existente.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `parted`:

1. **Listar todas las particiones:**
   ```bash
   parted -l
   ```

2. **Crear una nueva partición:**
   ```bash
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Eliminar una partición:**
   ```bash
   parted /dev/sda rm 1
   ```

4. **Redimensionar una partición:**
   ```bash
   parted /dev/sda resizepart 1 200MiB
   ```

## Tips
- Siempre realiza una copia de seguridad de tus datos antes de modificar particiones.
- Utiliza el modo interactivo de `parted` para obtener ayuda sobre los comandos disponibles.
- Asegúrate de desmontar cualquier partición que planees modificar para evitar problemas de datos.