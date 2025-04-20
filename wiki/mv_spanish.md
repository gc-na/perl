# [Linux] C Shell (csh) mv Uso equivalente: Mover o renombrar archivos y directorios

## Overview
El comando `mv` se utiliza en C Shell (csh) para mover o renombrar archivos y directorios. Es una herramienta fundamental para la gestión de archivos en sistemas Unix y Linux.

## Usage
La sintaxis básica del comando `mv` es la siguiente:

```csh
mv [opciones] [orígenes] [destino]
```

## Common Options
- `-i`: Pregunta antes de sobrescribir un archivo existente.
- `-u`: Mueve solo si el archivo de origen es más nuevo que el archivo de destino o si el archivo de destino no existe.
- `-v`: Muestra información detallada sobre lo que está haciendo el comando.

## Common Examples
1. **Mover un archivo a un directorio:**
   ```csh
   mv archivo.txt /ruta/al/directorio/
   ```

2. **Renombrar un archivo:**
   ```csh
   mv viejo_nombre.txt nuevo_nombre.txt
   ```

3. **Mover varios archivos a un directorio:**
   ```csh
   mv archivo1.txt archivo2.txt /ruta/al/directorio/
   ```

4. **Mover un directorio:**
   ```csh
   mv /ruta/al/directorio1 /ruta/al/directorio2
   ```

5. **Mover un archivo y preguntar antes de sobrescribir:**
   ```csh
   mv -i archivo.txt /ruta/al/directorio/
   ```

## Tips
- Siempre verifica el destino antes de mover archivos para evitar sobrescribir datos importantes.
- Utiliza la opción `-v` para tener un registro de las acciones realizadas, especialmente útil en operaciones masivas.
- Si no estás seguro de lo que hará el comando, prueba primero con la opción `-i` para evitar sobrescrituras accidentales.