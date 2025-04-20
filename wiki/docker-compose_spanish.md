# [Linux] C Shell (csh) docker-compose uso: Gestionar aplicaciones en contenedores

## Overview
El comando `docker-compose` se utiliza para definir y ejecutar aplicaciones de múltiples contenedores de Docker. Con un archivo de configuración, puedes especificar los servicios, redes y volúmenes que componen tu aplicación, facilitando su gestión y despliegue.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
docker-compose [opciones] [argumentos]
```

## Common Options
- `up`: Inicia los contenedores definidos en el archivo `docker-compose.yml`.
- `down`: Detiene y elimina los contenedores, redes y volúmenes creados por `up`.
- `build`: Construye o reconstruye los servicios definidos en el archivo.
- `logs`: Muestra los logs de los contenedores en ejecución.
- `ps`: Lista los contenedores que están siendo gestionados por `docker-compose`.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `docker-compose`:

1. **Iniciar los contenedores**:
   ```bash
   docker-compose up
   ```

2. **Iniciar los contenedores en segundo plano**:
   ```bash
   docker-compose up -d
   ```

3. **Detener y eliminar contenedores**:
   ```bash
   docker-compose down
   ```

4. **Construir los servicios**:
   ```bash
   docker-compose build
   ```

5. **Ver los logs de los contenedores**:
   ```bash
   docker-compose logs
   ```

## Tips
- Siempre revisa el archivo `docker-compose.yml` para asegurarte de que todos los servicios y configuraciones están correctamente definidos.
- Utiliza la opción `-d` para ejecutar contenedores en segundo plano y liberar la terminal.
- Mantén tus imágenes y contenedores actualizados usando `docker-compose pull` antes de iniciar tus servicios.
- Considera usar perfiles en tu archivo `docker-compose.yml` para gestionar diferentes entornos (desarrollo, producción, etc.).