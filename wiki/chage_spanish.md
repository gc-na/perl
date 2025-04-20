# [Linux] C Shell (csh) chage: Cambiar la información de expiración de la contraseña

## Overview
El comando `chage` se utiliza para modificar la información de expiración de las contraseñas de los usuarios en sistemas basados en Linux. Permite establecer cuándo una contraseña debe ser cambiada y gestionar la política de contraseñas de los usuarios.

## Usage
La sintaxis básica del comando `chage` es la siguiente:

```bash
chage [opciones] [argumentos]
```

## Common Options
- `-l`: Muestra la información de expiración de la contraseña del usuario.
- `-m <días>`: Establece el número mínimo de días entre cambios de contraseña.
- `-M <días>`: Establece el número máximo de días antes de que la contraseña deba ser cambiada.
- `-I <días>`: Establece el número de días de inactividad antes de que la cuenta sea desactivada.
- `-E <fecha>`: Establece la fecha de expiración de la cuenta.

## Common Examples
1. **Mostrar la información de expiración de la contraseña de un usuario:**
   ```bash
   chage -l nombre_usuario
   ```

2. **Establecer un mínimo de 7 días entre cambios de contraseña:**
   ```bash
   chage -m 7 nombre_usuario
   ```

3. **Establecer un máximo de 90 días antes de que la contraseña deba ser cambiada:**
   ```bash
   chage -M 90 nombre_usuario
   ```

4. **Establecer 30 días de inactividad antes de desactivar la cuenta:**
   ```bash
   chage -I 30 nombre_usuario
   ```

5. **Establecer una fecha de expiración para la cuenta:**
   ```bash
   chage -E 2024-12-31 nombre_usuario
   ```

## Tips
- Siempre verifica la información de expiración después de realizar cambios usando `chage -l nombre_usuario`.
- Considera establecer políticas de contraseñas que equilibren la seguridad y la usabilidad para los usuarios.
- Utiliza el comando con privilegios de superusuario para modificar la información de otros usuarios.