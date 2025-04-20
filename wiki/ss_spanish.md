# [Linux] C Shell (csh) ss uso equivalente: [visualizar sockets de red]

## Overview
El comando `ss` se utiliza para investigar sockets de red en sistemas operativos basados en Linux. Proporciona información detallada sobre las conexiones de red, incluyendo el estado de los sockets, direcciones y puertos.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
ss [opciones] [argumentos]
```

## Common Options
- `-t`: Muestra solo conexiones TCP.
- `-u`: Muestra solo conexiones UDP.
- `-l`: Muestra solo sockets que están escuchando.
- `-p`: Muestra el proceso que está utilizando el socket.
- `-n`: Muestra direcciones y puertos en formato numérico, evitando la resolución de nombres.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `ss`:

1. **Mostrar todas las conexiones TCP:**
   ```bash
   ss -t
   ```

2. **Mostrar todas las conexiones UDP:**
   ```bash
   ss -u
   ```

3. **Mostrar sockets que están escuchando:**
   ```bash
   ss -l
   ```

4. **Mostrar conexiones con información del proceso:**
   ```bash
   ss -p
   ```

5. **Mostrar conexiones en formato numérico:**
   ```bash
   ss -n
   ```

## Tips
- Utiliza `ss -t -l` para ver qué servicios están escuchando en tu máquina.
- Combina opciones, como `ss -tunlp`, para obtener una vista más completa de las conexiones activas y sus procesos.
- Recuerda que necesitarás permisos de superusuario para ver información de algunos procesos.