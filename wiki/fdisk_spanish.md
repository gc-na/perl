# [Linux] C Shell (csh) fdisk Uso: Herramienta para gestionar particiones de disco

## Overview
El comando `fdisk` se utiliza para gestionar las particiones de disco en sistemas operativos basados en Unix. Permite crear, eliminar y modificar particiones en discos duros y otros dispositivos de almacenamiento.

## Usage
La sintaxis básica del comando `fdisk` es la siguiente:

```bash
fdisk [opciones] [dispositivo]
```

## Common Options
- `-l`: Lista todas las particiones en los discos disponibles.
- `-u`: Usa sectores como unidad de medida en lugar de cilindros.
- `-n`: Crea una nueva partición.
- `-d`: Elimina una partición existente.
- `-p`: Muestra la tabla de particiones del dispositivo especificado.

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso de `fdisk`:

1. **Listar particiones en todos los discos:**
   ```bash
   fdisk -l
   ```

2. **Abrir fdisk para un disco específico (por ejemplo, /dev/sda):**
   ```bash
   fdisk /dev/sda
   ```

3. **Crear una nueva partición:**
   ```bash
   fdisk /dev/sda
   # Luego, dentro de la interfaz de fdisk, usa el comando 'n' para crear una nueva partición.
   ```

4. **Eliminar una partición existente:**
   ```bash
   fdisk /dev/sda
   # Luego, dentro de la interfaz de fdisk, usa el comando 'd' para eliminar una partición.
   ```

5. **Mostrar la tabla de particiones de un dispositivo:**
   ```bash
   fdisk -p /dev/sda
   ```

## Tips
- Siempre realiza una copia de seguridad de tus datos antes de modificar particiones.
- Utiliza el comando `man fdisk` para acceder a la documentación completa y obtener más información sobre las opciones disponibles.
- Ten cuidado al seleccionar el dispositivo correcto para evitar la pérdida de datos.