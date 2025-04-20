# [Linux] C Shell (csh) pwd Uso equivalente: mostrar el directorio de trabajo actual

## Overview
El comando `pwd` (print working directory) se utiliza en C Shell para mostrar la ruta del directorio de trabajo actual en el que se encuentra el usuario. Es una herramienta fundamental para la navegación en la línea de comandos, ya que permite saber en qué ubicación se está trabajando.

## Usage
La sintaxis básica del comando `pwd` es la siguiente:

```csh
pwd [opciones] [argumentos]
```

## Common Options
El comando `pwd` tiene algunas opciones comunes que pueden ser útiles:

- `-L`: Muestra la ruta del directorio de trabajo actual, siguiendo los enlaces simbólicos.
- `-P`: Muestra la ruta física del directorio de trabajo actual, resolviendo todos los enlaces simbólicos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `pwd`:

1. **Mostrar el directorio de trabajo actual:**
   ```csh
   pwd
   ```

2. **Mostrar la ruta siguiendo enlaces simbólicos:**
   ```csh
   pwd -L
   ```

3. **Mostrar la ruta física del directorio de trabajo:**
   ```csh
   pwd -P
   ```

## Tips
- Utiliza `pwd` frecuentemente para confirmar tu ubicación en el sistema de archivos, especialmente antes de ejecutar comandos que afectan archivos o directorios.
- Combina `pwd` con otros comandos, como `cd`, para asegurarte de que estás en el directorio correcto antes de realizar cambios.
- Recuerda que `pwd` es una herramienta simple pero poderosa para la navegación en la línea de comandos.