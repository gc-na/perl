# [Linux] C Shell (csh) diff uso: Comparar archivos línea por línea

## Overview
El comando `diff` se utiliza para comparar el contenido de dos archivos línea por línea. Su principal función es mostrar las diferencias entre ellos, lo que resulta útil para identificar cambios en archivos de texto, como código fuente o documentos.

## Usage
La sintaxis básica del comando `diff` es la siguiente:

```csh
diff [opciones] [archivo1] [archivo2]
```

## Common Options
- `-u`: Muestra las diferencias en un formato unificado, que es más fácil de leer.
- `-c`: Muestra las diferencias en un formato de contexto, que incluye líneas de contexto alrededor de las diferencias.
- `-i`: Ignora las diferencias entre mayúsculas y minúsculas.
- `-w`: Ignora los espacios en blanco al comparar las líneas.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `diff`:

1. Comparar dos archivos de texto y mostrar las diferencias:
   ```csh
   diff archivo1.txt archivo2.txt
   ```

2. Usar el formato unificado para ver las diferencias:
   ```csh
   diff -u archivo1.txt archivo2.txt
   ```

3. Ignorar diferencias de mayúsculas y minúsculas:
   ```csh
   diff -i archivo1.txt archivo2.txt
   ```

4. Comparar dos archivos y mostrar el contexto de las diferencias:
   ```csh
   diff -c archivo1.txt archivo2.txt
   ```

## Tips
- Siempre es útil hacer una copia de seguridad de los archivos antes de realizar cambios basados en las diferencias.
- Utiliza la opción `-u` para obtener un formato más legible, especialmente cuando trabajas con cambios en código.
- Si estás trabajando con archivos grandes, considera usar `diff` junto con `less` para facilitar la navegación por las diferencias:
  ```csh
  diff archivo1.txt archivo2.txt | less
  ```