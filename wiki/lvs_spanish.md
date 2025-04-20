# [Linux] C Shell (csh) lvs uso: listar volúmenes lógicos

## Overview
El comando `lvs` se utiliza para mostrar información sobre los volúmenes lógicos en un sistema que utiliza LVM (Logical Volume Manager). Permite a los usuarios ver detalles como el tamaño, el estado y el nombre de los volúmenes lógicos.

## Usage
La sintaxis básica del comando `lvs` es la siguiente:

```bash
lvs [opciones] [argumentos]
```

## Common Options
- `-o`: Especifica las columnas que se mostrarán en la salida.
- `-a`: Muestra todos los volúmenes, incluidos los que están inactivos.
- `-n`: Permite especificar el nombre del volumen lógico que se desea mostrar.
- `-r`: Muestra información de los volúmenes en formato de árbol.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `lvs`:

1. **Mostrar todos los volúmenes lógicos:**
   ```bash
   lvs
   ```

2. **Mostrar volúmenes lógicos con columnas específicas:**
   ```bash
   lvs -o +devices
   ```

3. **Mostrar un volumen lógico específico:**
   ```bash
   lvs -n nombre_del_volumen
   ```

4. **Mostrar todos los volúmenes, incluidos los inactivos:**
   ```bash
   lvs -a
   ```

5. **Mostrar información en formato de árbol:**
   ```bash
   lvs -r
   ```

## Tips
- Asegúrate de tener los permisos adecuados para ejecutar el comando `lvs`, ya que puede requerir privilegios de superusuario.
- Utiliza la opción `-o` para personalizar la salida y enfocarte en la información más relevante para tus necesidades.
- Combina `lvs` con otros comandos de LVM para gestionar volúmenes lógicos de manera más efectiva, como `lvcreate` o `lvremove`.