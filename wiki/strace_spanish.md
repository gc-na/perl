# [Linux] C Shell (csh) strace Uso: Herramienta para rastrear llamadas al sistema

## Overview
El comando `strace` se utiliza para rastrear las llamadas al sistema y las señales que reciben los procesos en un sistema operativo. Es una herramienta útil para depurar y diagnosticar problemas en aplicaciones, ya que permite observar cómo interactúan los programas con el núcleo del sistema.

## Usage
La sintaxis básica del comando `strace` es la siguiente:

```bash
strace [opciones] [argumentos]
```

## Common Options
- `-c`: Muestra un resumen de las estadísticas de las llamadas al sistema.
- `-e`: Permite filtrar las llamadas al sistema que se desean rastrear.
- `-p`: Adjunta `strace` a un proceso existente utilizando su ID de proceso (PID).
- `-o archivo`: Redirige la salida a un archivo en lugar de la salida estándar.
- `-f`: Sigue los procesos hijos creados por el proceso rastreado.

## Common Examples
1. **Rastrear un comando simple:**
   ```bash
   strace ls
   ```
   Este comando rastrea las llamadas al sistema realizadas por el comando `ls`.

2. **Rastrear un proceso en ejecución:**
   ```bash
   strace -p 1234
   ```
   Aquí, `1234` es el ID del proceso que se desea rastrear.

3. **Filtrar las llamadas al sistema:**
   ```bash
   strace -e trace=open,close ls
   ```
   Este comando rastrea solo las llamadas `open` y `close` realizadas por `ls`.

4. **Guardar la salida en un archivo:**
   ```bash
   strace -o salida.txt ls
   ```
   Esto guarda el resultado del rastreo en el archivo `salida.txt`.

5. **Obtener estadísticas de llamadas al sistema:**
   ```bash
   strace -c ls
   ```
   Este comando proporciona un resumen de las estadísticas de las llamadas al sistema realizadas por `ls`.

## Tips
- Utiliza `strace` con `-o` para guardar la salida en un archivo, lo que facilita el análisis posterior.
- Filtra las llamadas al sistema con `-e` para enfocarte en las que son relevantes para tu diagnóstico.
- Ten en cuenta que `strace` puede afectar el rendimiento del programa que estás rastreando, así que úsalo con precaución en entornos de producción.