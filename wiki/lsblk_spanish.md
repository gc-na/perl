# [Linux] C Shell (csh) lsblk Uso: [listar bloques de dispositivos]

## Overview
El comando `lsblk` se utiliza para listar todos los dispositivos de bloques en el sistema, como discos duros, particiones y dispositivos de almacenamiento extraíbles. Este comando proporciona una vista clara de la estructura de almacenamiento, mostrando información como el tamaño y el tipo de cada dispositivo.

## Usage
La sintaxis básica del comando `lsblk` es la siguiente:

```csh
lsblk [opciones] [argumentos]
```

## Common Options
Aquí hay algunas opciones comunes que se pueden utilizar con `lsblk`:

- `-a` o `--all`: Muestra todos los dispositivos, incluidos los que no están montados.
- `-f` o `--fs`: Muestra información sobre el sistema de archivos de cada dispositivo.
- `-l` o `--list`: Muestra la salida en formato de lista en lugar de árbol.
- `-o` o `--output`: Permite especificar qué columnas mostrar en la salida.
- `-n` o `--noheadings`: Suprime los encabezados de las columnas en la salida.

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso de `lsblk`:

1. **Listar todos los dispositivos de bloques**:
   ```csh
   lsblk
   ```

2. **Listar todos los dispositivos, incluidos los no montados**:
   ```csh
   lsblk -a
   ```

3. **Mostrar información del sistema de archivos**:
   ```csh
   lsblk -f
   ```

4. **Mostrar la salida en formato de lista**:
   ```csh
   lsblk -l
   ```

5. **Especificar columnas a mostrar**:
   ```csh
   lsblk -o NAME,SIZE,TYPE
   ```

6. **Suprimir encabezados de columnas**:
   ```csh
   lsblk -n
   ```

## Tips
- Utiliza la opción `-f` para obtener información adicional sobre los sistemas de archivos, lo que puede ser útil para la administración de discos.
- Combina `lsblk` con otros comandos como `grep` para filtrar la salida y encontrar dispositivos específicos.
- Familiarízate con la salida del comando para poder identificar rápidamente los dispositivos que necesitas gestionar.