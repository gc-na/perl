<!--
Meta Description: # getpeername en Perl: Obtención de Información del Cliente en Conexiones de Red ## Sinopsis El método `getpeername` en Perl permite recuperar la dire...
Meta Keywords: socket, del, getpeername, dirección, que
-->

# getpeername en Perl: Obtención de Información del Cliente en Conexiones de Red

## Sinopsis
El método `getpeername` en Perl permite recuperar la dirección del socket remoto al que está conectado un socket local. Esta función es esencial en aplicaciones de red donde es necesario conocer la identidad del cliente que se conecta al servidor.

## Documentación
### Propósito
`getpeername` se utiliza para obtener la dirección y el número de puerto del cliente asociado con un socket. Es especialmente útil en servidores que manejan múltiples conexiones simultáneamente y necesitan identificar a cada cliente.

### Uso
El uso básico de `getpeername` se realiza sobre un objeto de socket creado con el módulo `IO::Socket`. La función devuelve una lista con la dirección y el puerto del cliente conectado.

#### Sintaxis
```perl
my $sockaddr = getpeername($socket);
```

- `$socket`: Un objeto de socket previamente creado.

El resultado es una cadena binaria que representa la dirección del cliente. Para convertirla a un formato legible, se puede usar el módulo `Socket`.

### Detalles
- Es necesario que el socket esté en estado de conexión.
- La función devuelve `undef` si no se puede obtener la información del cliente, lo que puede ocurrir si el socket ha sido cerrado o si no se ha establecido una conexión.
- Los datos devueltos pueden ser procesados con funciones adicionales del módulo `Socket` para extraer la dirección IP y el número de puerto.

## Ejemplos
### Ejemplo 1: Uso básico de `getpeername`
```perl
use IO::Socket;
use Socket;

# Crear un socket de servidor
my $server = IO::Socket::INET->new(
    LocalPort => 7890,
    Proto     => 'udp',
    Listen    => 5
) or die "No se pudo crear el socket: $!";

while (my $client = $server->accept()) {
    my $peer_address = getpeername($client);

    # Convertir la dirección binaria a formato legible
    my ($port, $iaddr) = unpack_sockaddr_in($peer_address);
    my $client_ip = inet_ntoa($iaddr);

    print "Conexión desde $client_ip:$port\n";
}
```

### Ejemplo 2: Comprobación de error
```perl
use IO::Socket;
use Socket;

my $socket = IO::Socket::INET->new(PeerAddr => '127.0.0.1', PeerPort => '7890', Proto => 'tcp');

if (defined $socket) {
    my $peer_address = getpeername($socket);
    if (defined $peer_address) {
        my ($port, $iaddr) = unpack_sockaddr_in($peer_address);
        my $client_ip = inet_ntoa($iaddr);
        print "Conectado a $client_ip:$port\n";
    } else {
        warn "Error al obtener la dirección del cliente: $!";
    }
} else {
    die "No se pudo conectar: $!";
}
```

## Explicación
Un error común al usar `getpeername` es intentar obtener la dirección de un socket que no está conectado o que ha sido cerrado. En tales casos, la función devolverá `undef`. Además, es importante recordar que la dirección devuelta está en formato binario y debe ser convertida a un formato legible utilizando las funciones adecuadas del módulo `Socket`.

## Resumen en Una Línea
La función `getpeername` en Perl permite obtener la dirección y el puerto del socket remoto al que está conectado un socket local, facilitando la identificación de clientes en aplicaciones de red.