# [Sistema Operativo] C Shell (csh) nslookup Uso: Consulta de direcciones IP y nombres de dominio

## Overview
El comando `nslookup` se utiliza para consultar el sistema de nombres de dominio (DNS) para obtener información sobre direcciones IP y nombres de dominio. Permite a los usuarios verificar la configuración de DNS y resolver nombres de dominio en direcciones IP.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
nslookup [opciones] [argumentos]
```

## Common Options
- `-type=tipo`: Especifica el tipo de consulta DNS, como `A`, `MX`, `CNAME`, etc.
- `-timeout=segundos`: Establece el tiempo de espera en segundos para la respuesta.
- `-retry=intentos`: Define el número de intentos de consulta en caso de fallo.

## Common Examples
Aquí hay algunos ejemplos prácticos de cómo usar `nslookup`:

1. **Consultar la dirección IP de un dominio:**

   ```csh
   nslookup www.ejemplo.com
   ```

2. **Consultar un registro de tipo MX (Mail Exchange):**

   ```csh
   nslookup -type=MX ejemplo.com
   ```

3. **Consultar un registro CNAME:**

   ```csh
   nslookup -type=CNAME www.ejemplo.com
   ```

4. **Cambiar el servidor DNS utilizado para la consulta:**

   ```csh
   nslookup www.ejemplo.com 8.8.8.8
   ```

## Tips
- Utiliza `nslookup` en modo interactivo simplemente escribiendo `nslookup` sin argumentos para realizar múltiples consultas sin tener que volver a escribir el comando.
- Asegúrate de que tu conexión a Internet esté activa antes de realizar consultas DNS.
- Verifica siempre la configuración de DNS si experimentas problemas de conectividad con un dominio específico.