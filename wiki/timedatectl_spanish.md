# [Linux] C Shell (csh) timedatectl Uso: Controlar la configuración de fecha y hora del sistema

## Overview
El comando `timedatectl` se utiliza para consultar y cambiar la configuración de fecha y hora del sistema en sistemas que utilizan systemd. Permite gestionar la sincronización de tiempo y la zona horaria, así como verificar el estado actual del reloj del sistema.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
timedatectl [opciones] [argumentos]
```

## Common Options
- `set-time`: Establece la fecha y hora del sistema.
- `set-timezone`: Cambia la zona horaria del sistema.
- `status`: Muestra el estado actual de la fecha y hora del sistema.
- `list-timezones`: Lista todas las zonas horarias disponibles.
- `set-ntp`: Habilita o deshabilita la sincronización automática del tiempo a través de NTP (Network Time Protocol).

## Common Examples
1. **Ver el estado actual de la fecha y hora:**
   ```bash
   timedatectl status
   ```

2. **Establecer una fecha y hora específicas:**
   ```bash
   timedatectl set-time '2023-10-01 12:00:00'
   ```

3. **Cambiar la zona horaria a Europa/Madrid:**
   ```bash
   timedatectl set-timezone Europe/Madrid
   ```

4. **Listar todas las zonas horarias disponibles:**
   ```bash
   timedatectl list-timezones
   ```

5. **Habilitar la sincronización automática del tiempo:**
   ```bash
   timedatectl set-ntp true
   ```

## Tips
- Asegúrate de tener privilegios de administrador para cambiar la fecha, hora o zona horaria.
- Utiliza `timedatectl list-timezones` para encontrar la zona horaria correcta antes de establecerla.
- Verifica siempre el estado después de realizar cambios con `timedatectl status` para confirmar que se aplicaron correctamente.