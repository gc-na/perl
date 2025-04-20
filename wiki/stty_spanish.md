# [Linux] C Shell (csh) stty: Configurar terminales

## Overview
El comando `stty` se utiliza para cambiar y mostrar las configuraciones de la terminal en sistemas Unix y Linux. Permite ajustar parámetros como el control de flujo, la configuración de caracteres especiales y otras propiedades que afectan la interacción del usuario con la terminal.

## Usage
La sintaxis básica del comando `stty` es la siguiente:

```csh
stty [opciones] [argumentos]
```

## Common Options
- `-a`: Muestra todas las configuraciones actuales de la terminal.
- `-g`: Muestra la configuración actual en un formato que se puede usar como argumento para `stty`.
- `erase <carácter>`: Establece el carácter de borrado.
- `kill <carácter>`: Establece el carácter de eliminación de línea.
- `intr <carácter>`: Establece el carácter de interrupción.

## Common Examples
1. **Mostrar todas las configuraciones de la terminal:**
   ```csh
   stty -a
   ```

2. **Establecer el carácter de borrado a `^H` (retroceso):**
   ```csh
   stty erase ^H
   ```

3. **Establecer el carácter de interrupción a `^C`:**
   ```csh
   stty intr ^C
   ```

4. **Guardar la configuración actual para su uso posterior:**
   ```csh
   stty -g > config.txt
   ```

5. **Restaurar la configuración desde un archivo:**
   ```csh
   stty `cat config.txt`
   ```

## Tips
- Siempre verifica la configuración actual de la terminal antes de hacer cambios para evitar problemas inesperados.
- Utiliza `stty -g` para guardar configuraciones que puedas necesitar más tarde.
- Recuerda que algunos caracteres especiales pueden requerir que los ingreses como combinaciones de teclas (por ejemplo, `^C` para Ctrl+C).