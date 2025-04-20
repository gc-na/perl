# [Linux] C Shell (csh) netcat uso: Herramienta de red versátil

## Overview
El comando `netcat`, también conocido como "nc", es una herramienta de red que permite leer y escribir datos a través de conexiones de red utilizando el protocolo TCP o UDP. Es ampliamente utilizado para depuración de redes, transferencia de archivos y como un cliente/servidor simple.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
netcat [opciones] [argumentos]
```

## Common Options
- `-l`: Escucha en un puerto específico para conexiones entrantes.
- `-p [puerto]`: Especifica el puerto local para usar.
- `-u`: Utiliza el protocolo UDP en lugar de TCP.
- `-v`: Muestra información detallada sobre la conexión.
- `-z`: Realiza un escaneo de puertos sin enviar datos.

## Common Examples
1. **Escuchar en un puerto específico:**
   ```bash
   netcat -l -p 1234
   ```
   Este comando inicia `netcat` en modo escucha en el puerto 1234.

2. **Conectar a un servidor remoto:**
   ```bash
   netcat example.com 80
   ```
   Conecta a `example.com` en el puerto 80 (HTTP).

3. **Transferir un archivo:**
   En el lado del receptor:
   ```bash
   netcat -l -p 1234 > archivo_recibido.txt
   ```
   En el lado del emisor:
   ```bash
   netcat [IP_del_receptor] 1234 < archivo_a_enviar.txt
   ```

4. **Escaneo de puertos:**
   ```bash
   netcat -z -v example.com 1-100
   ```
   Escanea los puertos del 1 al 100 en `example.com` y muestra los resultados.

## Tips
- Asegúrate de tener los permisos necesarios para escuchar en puertos específicos, especialmente en puertos por debajo de 1024.
- Utiliza la opción `-v` para obtener más información sobre las conexiones, lo que puede ser útil para la depuración.
- Recuerda que `netcat` no cifra la información transmitida, así que evita enviar datos sensibles sin una capa de seguridad adicional.