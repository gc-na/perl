# [Linux] C Shell (csh) chkconfig uso: Gestionar servicios del sistema

## Overview
El comando `chkconfig` se utiliza para gestionar los servicios de inicio en sistemas basados en Linux. Permite habilitar o deshabilitar servicios para que se inicien automáticamente en diferentes niveles de ejecución.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
chkconfig [opciones] [argumentos]
```

## Common Options
- `--list`: Muestra todos los servicios y su estado en cada nivel de ejecución.
- `--add`: Agrega un nuevo servicio al sistema.
- `--del`: Elimina un servicio del sistema.
- `--level`: Especifica los niveles de ejecución para habilitar o deshabilitar un servicio.

## Common Examples
1. **Listar todos los servicios y su estado:**
   ```csh
   chkconfig --list
   ```

2. **Habilitar un servicio en todos los niveles de ejecución:**
   ```csh
   chkconfig nombre_del_servicio on
   ```

3. **Deshabilitar un servicio en todos los niveles de ejecución:**
   ```csh
   chkconfig nombre_del_servicio off
   ```

4. **Agregar un nuevo servicio:**
   ```csh
   chkconfig --add nombre_del_servicio
   ```

5. **Eliminar un servicio existente:**
   ```csh
   chkconfig --del nombre_del_servicio
   ```

## Tips
- Asegúrate de tener privilegios de superusuario para realizar cambios en los servicios del sistema.
- Verifica el estado de los servicios después de realizar cambios para asegurarte de que se hayan aplicado correctamente.
- Utiliza `chkconfig --level 2345 nombre_del_servicio on` para habilitar un servicio solo en niveles de ejecución específicos.