<!--
Meta Description: # getsockname en Perl: Obtención de la dirección local de un socket ## Sinopsis El comando `getsockname` en Perl se utiliza para obtener la dirección ...
Meta Keywords: socket, dirección, getsockname, local, puerto
-->

# getsockname en Perl: Obtención de la dirección local de un socket

## Sinopsis
El comando `getsockname` en Perl se utiliza para obtener la dirección local y el puerto asignado a un socket. Este comando es parte del módulo `IO::Socket`, que proporciona una interfaz para la comunicación de red.

## Documentación
`getsockname` es un método que permite a los programadores acceder a la información de la dirección local asociada a un socket previamente creado. Este método es fundamental para aplicaciones de red que necesitan conocer su dirección y puerto de escucha. Su uso es común en servidores que aceptan conexiones entrantes.

### Uso
Para utilizar `getsockname`, primero debes crear un socket utilizando el módulo `IO::Socket`. Posteriormente, puedes llamar a `getsockname` en el objeto socket. El método devolverá la dirección y el puerto en forma de un array.

### Detalles
- **Módulo Requerido:** `IO::Socket`
- **Método:** `getsockname`
- **Retorno:** Devuelve una lista que contiene la dirección y el puerto del socket.
  
Ejemplo de uso básico:
```perl
use IO::Socket;

# Crear un socket de tipo INET
my $socket = IO::Socket::INET->new(
    LocalAddr => '127.0.0.1',
    LocalPort => '8080',
    Proto     => 'tcp',
    Listen    => SOMAXCONN
) or die "No se pudo crear el socket: $!";

# Obtener la dirección local y el puerto
my $local_address = $socket->getsockname();
```

## Ejemplos
### Ejemplo 1: Uso básico de getsockname
```perl
use IO::Socket;

# Crear un socket
my $socket = IO::Socket::INET->new(
    LocalPort => 0,
    Proto     => 'udp',
) or die "No se pudo crear el socket: $!";

# Obtener la dirección y puerto
my $local_address = $socket->getsockname();
print "Dirección local y puerto: $local_address\n";
```

### Ejemplo 2: Mostrar dirección y puerto por separado
```perl
use IO::Socket;
use Socket;

# Crear un socket
my $socket = IO::Socket::INET->new(
    LocalAddr => '0.0.0.0',
    LocalPort => 9090,
    Proto     => 'tcp',
    Listen    => SOMAXCONN,
) or die "No se pudo crear el socket: $!";

# Obtener la dirección local
my $local_address = $socket->getsockname();
my ($port, $ip) = unpack_sockaddr_in($local_address);
print "IP local: " . inet_ntoa($ip) . "\n";
print "Puerto local: $port\n";
```

## Explicación
Al usar `getsockname`, es importante recordar que este método solo funcionará en sockets que ya han sido vinculados a una dirección local. Si intentas llamar a `getsockname` en un socket que no está en un estado válido, es posible que obtengas un error o un resultado inesperado. Además, ten en cuenta que el formato de salida de la dirección puede variar según el tipo de socket (INET, UNIX, etc.).

## Resumen en una línea
`getsockname` en Perl permite obtener la dirección y el puerto local asociados a un socket, facilitando la gestión de conexiones de red.