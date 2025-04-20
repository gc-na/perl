# [Linux] C Shell (csh) umask uso: Establecer permisos predeterminados para archivos y directorios

## Overview
El comando `umask` en C Shell (csh) se utiliza para establecer los permisos predeterminados de los archivos y directorios que se crean en el sistema. Este comando define una máscara que restringe los permisos que se asignan automáticamente a los nuevos archivos y directorios.

## Usage
La sintaxis básica del comando `umask` es la siguiente:

```csh
umask [opciones] [argumentos]
```

## Common Options
- `-S`: Muestra la máscara de permisos en formato simbólico.
- `-p`: Muestra la máscara de permisos actual en formato octal.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `umask`:

1. **Ver la máscara de permisos actual:**
   ```csh
   umask
   ```

2. **Establecer una nueva máscara de permisos:**
   ```csh
   umask 027
   ```

3. **Mostrar la máscara de permisos en formato simbólico:**
   ```csh
   umask -S
   ```

4. **Restablecer la máscara de permisos a un valor específico:**
   ```csh
   umask 002
   ```

5. **Ver la máscara de permisos en formato octal:**
   ```csh
   umask -p
   ```

## Tips
- Recuerda que la máscara de permisos se aplica a los archivos y directorios creados después de que se establece, por lo que es importante configurarla antes de crear nuevos archivos.
- Un valor común para `umask` es `022`, que permite que el propietario tenga permisos de lectura y escritura, mientras que el grupo y otros solo tienen permisos de lectura.
- Puedes agregar el comando `umask` a tu archivo de inicio (como `.cshrc`) para establecer una configuración predeterminada cada vez que inicies una nueva sesión de shell.