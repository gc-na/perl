# [Linux] C Shell (csh) mkfifo: Crear un archivo FIFO

## Overview
El comando `mkfifo` se utiliza para crear un archivo FIFO (First In, First Out), que es un tipo especial de archivo que permite la comunicación entre procesos. Los archivos FIFO actúan como canales de comunicación donde los datos escritos en el archivo por un proceso pueden ser leídos por otro proceso en el orden en que fueron escritos.

## Usage
La sintaxis básica del comando `mkfifo` es la siguiente:

```
mkfifo [opciones] [argumentos]
```

## Common Options
- `-m, --mode`: Establece los permisos del archivo FIFO que se va a crear. Por defecto, los permisos son 0666.
- `--help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `mkfifo`:

1. **Crear un archivo FIFO simple:**
   ```csh
   mkfifo mi_fifo
   ```

2. **Crear un archivo FIFO con permisos específicos:**
   ```csh
   mkfifo -m 0644 mi_fifo_con_permisos
   ```

3. **Verificar que el archivo FIFO se ha creado:**
   ```csh
   ls -l mi_fifo
   ```

4. **Usar el archivo FIFO en un comando de lectura y escritura:**
   - En una terminal, escribe:
     ```csh
     cat < mi_fifo
     ```
   - En otra terminal, escribe:
     ```csh
     echo "Hola, FIFO!" > mi_fifo
     ```

## Tips
- Asegúrate de que el archivo FIFO esté siendo leído antes de escribir en él, de lo contrario, el proceso de escritura se bloqueará hasta que haya un lector disponible.
- Utiliza permisos adecuados al crear un archivo FIFO para garantizar que solo los procesos autorizados puedan acceder a él.
- Recuerda que los archivos FIFO son temporales y se eliminan automáticamente cuando no hay más procesos que los utilizan.