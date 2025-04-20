# [Linux] C Shell (csh) rsync uso: Sincronización de archivos y directorios

## Overview
El comando `rsync` se utiliza para sincronizar archivos y directorios entre diferentes ubicaciones, ya sea en la misma máquina o entre máquinas remotas. Es eficiente porque solo copia los cambios realizados en los archivos, lo que ahorra tiempo y ancho de banda.

## Usage
La sintaxis básica del comando `rsync` es la siguiente:

```bash
rsync [opciones] [origen] [destino]
```

## Common Options
- `-a`: Modo archivo; copia archivos de manera recursiva y preserva atributos como permisos y tiempos de modificación.
- `-v`: Modo verbose; muestra información detallada sobre el proceso de sincronización.
- `-z`: Comprime los datos durante la transferencia para ahorrar ancho de banda.
- `-r`: Copia directorios de manera recursiva.
- `--delete`: Elimina archivos en el destino que no están presentes en el origen.

## Common Examples
- Sincronizar un directorio local a otro directorio local:

```bash
rsync -av /ruta/origen/ /ruta/destino/
```

- Sincronizar un directorio local a un servidor remoto:

```bash
rsync -av /ruta/origen/ usuario@servidor:/ruta/destino/
```

- Sincronizar un directorio remoto a un directorio local:

```bash
rsync -av usuario@servidor:/ruta/origen/ /ruta/destino/
```

- Sincronizar y eliminar archivos en el destino que no están en el origen:

```bash
rsync -av --delete /ruta/origen/ /ruta/destino/
```

## Tips
- Siempre verifica el comando con la opción `-n` (modo de prueba) antes de ejecutar una sincronización para asegurarte de que los cambios son los esperados.
- Utiliza la opción `-z` si estás sincronizando archivos grandes a través de una conexión lenta para mejorar la velocidad de transferencia.
- Considera usar `--progress` para ver el progreso de la transferencia de archivos, especialmente útil para archivos grandes.