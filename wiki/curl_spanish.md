# [Linux] C Shell (csh) curl Uso: Herramienta para transferir datos con URL

## Overview
El comando `curl` es una herramienta de línea de comandos que permite transferir datos hacia o desde un servidor utilizando diversos protocolos, como HTTP, HTTPS, FTP, entre otros. Es muy útil para realizar solicitudes web y descargar archivos.

## Usage
La sintaxis básica del comando `curl` es la siguiente:

```csh
curl [opciones] [argumentos]
```

## Common Options
A continuación se presentan algunas opciones comunes de `curl` junto con breves explicaciones:

- `-O`: Descarga un archivo y lo guarda con el mismo nombre que tiene en el servidor.
- `-L`: Sigue redirecciones si el recurso solicitado ha cambiado de ubicación.
- `-u`: Proporciona credenciales de usuario y contraseña para autenticación.
- `-d`: Envía datos en una solicitud POST.
- `-I`: Muestra solo los encabezados de la respuesta.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `curl`:

1. **Descargar un archivo:**

   ```csh
   curl -O http://ejemplo.com/archivo.txt
   ```

2. **Seguir redirecciones:**

   ```csh
   curl -L http://ejemplo.com
   ```

3. **Enviar datos con una solicitud POST:**

   ```csh
   curl -d "nombre=valor" http://ejemplo.com/api
   ```

4. **Autenticación básica:**

   ```csh
   curl -u usuario:contraseña http://ejemplo.com/privado
   ```

5. **Mostrar solo los encabezados de la respuesta:**

   ```csh
   curl -I http://ejemplo.com
   ```

## Tips
- Siempre verifica la URL antes de realizar la descarga para evitar archivos no deseados.
- Usa la opción `-v` para habilitar el modo verbose y obtener más información sobre la transferencia.
- Si trabajas con APIs, considera usar la opción `-H` para agregar encabezados personalizados a tus solicitudes.