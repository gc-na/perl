# [Linux] C Shell (csh) htop uso: Monitoreo interactivo de procesos

## Overview
El comando `htop` es una herramienta de monitoreo interactivo que permite visualizar y gestionar los procesos que se están ejecutando en un sistema. A diferencia del comando `top`, `htop` ofrece una interfaz más amigable y colorida, permitiendo a los usuarios realizar acciones como matar procesos, cambiar la prioridad y más, todo desde una sola pantalla.

## Usage
La sintaxis básica del comando `htop` es la siguiente:

```bash
htop [opciones] [argumentos]
```

## Common Options
- `-h`, `--help`: Muestra la ayuda y la información sobre el uso de `htop`.
- `-s`, `--sort`: Permite especificar el criterio de ordenación de los procesos (por ejemplo, CPU, memoria).
- `-p`, `--pid`: Muestra solo los procesos con los identificadores de proceso (PID) especificados.
- `-u`, `--user`: Muestra solo los procesos del usuario especificado.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `htop`:

1. **Iniciar htop**:
   ```bash
   htop
   ```

2. **Ordenar por uso de CPU**:
   ```bash
   htop -s PERCENT_CPU
   ```

3. **Mostrar procesos de un usuario específico**:
   ```bash
   htop -u nombre_usuario
   ```

4. **Mostrar solo un proceso específico**:
   ```bash
   htop -p 1234
   ```

5. **Mostrar ayuda**:
   ```bash
   htop -h
   ```

## Tips
- Utiliza las teclas de función (F1 a F10) para acceder a diferentes opciones y configuraciones dentro de `htop`.
- Puedes usar las teclas de flecha para navegar entre los procesos y la tecla `F9` para matar un proceso seleccionado.
- Personaliza la visualización de `htop` presionando `F2` para acceder a la configuración y ajustar las columnas mostradas según tus necesidades.