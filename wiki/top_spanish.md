# [Linux] C Shell (csh) top uso: Monitoreo de procesos en tiempo real

## Overview
El comando `top` es una herramienta de monitoreo en tiempo real que muestra los procesos en ejecución en un sistema. Proporciona información sobre el uso de la CPU, la memoria y otros recursos del sistema, permitiendo a los usuarios identificar procesos que consumen muchos recursos.

## Usage
La sintaxis básica del comando `top` es la siguiente:

```csh
top [opciones] [argumentos]
```

## Common Options
A continuación se presentan algunas opciones comunes que se pueden utilizar con el comando `top`:

- `-d <segundos>`: Establece el intervalo de actualización en segundos.
- `-p <pid>`: Muestra solo el proceso con el identificador de proceso especificado.
- `-n <número>`: Especifica el número de actualizaciones que se deben mostrar antes de salir.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `top`:

1. **Ejecutar top con actualización cada 2 segundos**:
   ```csh
   top -d 2
   ```

2. **Mostrar solo un proceso específico**:
   ```csh
   top -p 1234
   ```

3. **Mostrar 5 actualizaciones y luego salir**:
   ```csh
   top -n 5
   ```

## Tips
- Para salir de la interfaz de `top`, simplemente presiona `q`.
- Puedes ordenar los procesos por diferentes columnas presionando las teclas correspondientes mientras `top` está en ejecución (por ejemplo, `M` para ordenar por uso de memoria).
- Usa la tecla `h` dentro de `top` para acceder a la ayuda y ver más opciones disponibles.