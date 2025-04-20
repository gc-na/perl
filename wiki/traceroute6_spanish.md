# [Linux] C Shell (csh) traceroute6 Uso: Muestra la ruta de paquetes IPv6

## Overview
El comando `traceroute6` se utiliza para rastrear la ruta que siguen los paquetes de datos a través de una red IPv6. Permite a los usuarios identificar los diferentes nodos por los que pasan los paquetes hasta llegar a su destino, lo que puede ser útil para diagnosticar problemas de conectividad.

## Usage
La sintaxis básica del comando `traceroute6` es la siguiente:

```csh
traceroute6 [options] [arguments]
```

## Common Options
- `-m <hops>`: Establece el número máximo de saltos (hops) que se intentarán.
- `-w <seconds>`: Define el tiempo de espera para cada respuesta en segundos.
- `-q <nqueries>`: Especifica el número de consultas por salto.
- `-p <port>`: Establece el puerto de destino para las consultas.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `traceroute6`:

1. Rastrear la ruta a un sitio web específico:
   ```csh
   traceroute6 www.ejemplo.com
   ```

2. Establecer un número máximo de saltos a 15:
   ```csh
   traceroute6 -m 15 www.ejemplo.com
   ```

3. Definir un tiempo de espera de 2 segundos:
   ```csh
   traceroute6 -w 2 www.ejemplo.com
   ```

4. Rastrear un destino utilizando un puerto específico:
   ```csh
   traceroute6 -p 80 www.ejemplo.com
   ```

## Tips
- Asegúrate de tener privilegios adecuados para ejecutar `traceroute6`, ya que puede requerir permisos de superusuario en algunos sistemas.
- Utiliza opciones como `-m` y `-w` para ajustar el comportamiento del comando según tus necesidades específicas.
- Si estás teniendo problemas de conectividad, compara los resultados de `traceroute6` con los de `ping` para obtener una visión más completa de la situación de la red.