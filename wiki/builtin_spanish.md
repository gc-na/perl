# [Linux] C Shell (csh) builtin `echo`: Muestra texto en la salida estándar

## Overview
El comando `echo` en C Shell (csh) se utiliza para mostrar texto o variables en la salida estándar, que generalmente es la pantalla del terminal. Es una herramienta fundamental para la visualización de mensajes y la depuración de scripts.

## Usage
La sintaxis básica del comando `echo` es la siguiente:

```csh
echo [opciones] [texto]
```

## Common Options
- `-n`: No imprime una nueva línea al final del texto.
- `-e`: Activa la interpretación de secuencias de escape (como `\n` para nueva línea).
- `-E`: Desactiva la interpretación de secuencias de escape.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `echo`:

1. **Mostrar un mensaje simple:**
   ```csh
   echo "Hola, mundo!"
   ```

2. **Mostrar el valor de una variable:**
   ```csh
   set nombre = "Juan"
   echo "Hola, $nombre!"
   ```

3. **Mostrar texto sin nueva línea:**
   ```csh
   echo -n "Este texto no tiene nueva línea al final."
   ```

4. **Usar secuencias de escape:**
   ```csh
   echo -e "Línea 1\nLínea 2"
   ```

5. **Desactivar la interpretación de secuencias de escape:**
   ```csh
   echo -E "Texto con \n sin interpretación."
   ```

## Tips
- Utiliza `echo -n` cuando necesites que el texto se imprima en la misma línea que el siguiente comando.
- Para depuración, imprimir el valor de variables puede ayudarte a entender el flujo de tu script.
- Recuerda que el uso de comillas es importante; las comillas dobles permiten la expansión de variables, mientras que las comillas simples no.