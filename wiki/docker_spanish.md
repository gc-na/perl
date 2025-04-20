# [Linux] C Shell (csh) docker uso: Comando para gestionar contenedores

## Overview
El comando `docker` se utiliza para gestionar contenedores en un entorno de virtualización. Permite crear, ejecutar y administrar aplicaciones en contenedores, facilitando la implementación y escalabilidad de aplicaciones.

## Usage
La sintaxis básica del comando `docker` es la siguiente:

```
docker [opciones] [argumentos]
```

## Common Options
- `run`: Crea y ejecuta un contenedor a partir de una imagen.
- `ps`: Muestra los contenedores en ejecución.
- `images`: Lista las imágenes disponibles en el sistema.
- `rm`: Elimina uno o más contenedores.
- `rmi`: Elimina una o más imágenes.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `docker`:

1. **Ejecutar un contenedor**:
   ```bash
   docker run hello-world
   ```

2. **Listar contenedores en ejecución**:
   ```bash
   docker ps
   ```

3. **Listar todas las imágenes**:
   ```bash
   docker images
   ```

4. **Eliminar un contenedor**:
   ```bash
   docker rm nombre_del_contenedor
   ```

5. **Eliminar una imagen**:
   ```bash
   docker rmi nombre_de_la_imagen
   ```

## Tips
- Asegúrate de tener Docker instalado y en ejecución antes de usar los comandos.
- Utiliza `docker --help` para obtener más información sobre las opciones disponibles.
- Mantén tus imágenes y contenedores organizados para facilitar la gestión y evitar confusiones.