# [Linux] C Shell (csh) fc <Uso equivalente en español>: [editar y reejecutar comandos]

## Overview
El comando `fc` en C Shell (csh) se utiliza para editar y reejecutar comandos previamente ingresados en la sesión de la terminal. Permite al usuario modificar comandos anteriores antes de ejecutarlos nuevamente, lo que facilita la corrección de errores o la modificación de argumentos.

## Usage
La sintaxis básica del comando `fc` es la siguiente:

```csh
fc [opciones] [argumentos]
```

## Common Options
- `-l`: Lista los comandos en el historial.
- `-n`: No muestra los números de línea al listar los comandos.
- `-s`: Ejecuta el comando después de editarlo sin abrir un editor.

## Common Examples
1. **Listar los últimos 10 comandos:**
   ```csh
   fc -l -10
   ```

2. **Editar el último comando:**
   ```csh
   fc
   ```

3. **Ejecutar el último comando sin editar:**
   ```csh
   fc -s
   ```

4. **Listar los comandos sin números de línea:**
   ```csh
   fc -n -l
   ```

5. **Editar un comando específico (por número):**
   ```csh
   fc 5
   ```

## Tips
- Utiliza `fc` para corregir rápidamente errores en comandos sin tener que volver a escribirlos.
- Familiarízate con el uso de editores de texto como `vi` o `nano`, ya que `fc` abrirá el editor predeterminado para la edición.
- Recuerda que puedes especificar un rango de comandos para editar varios a la vez, lo que puede ser útil para realizar cambios en múltiples entradas.