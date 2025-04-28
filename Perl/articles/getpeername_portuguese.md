<!--
Meta Description: # getpeername: Função Perl para Obter Informações de Conexão de Socket ## Sinopse A função `getpeername` em Perl é utilizada para recuperar o endereço...
Meta Keywords: socket, getpeername, perl, que, use
-->

# getpeername: Função Perl para Obter Informações de Conexão de Socket

## Sinopse
A função `getpeername` em Perl é utilizada para recuperar o endereço remoto de uma conexão de socket, permitindo que um programa obtenha informações sobre o cliente conectado.

## Documentação
A função `getpeername` faz parte do módulo de socket do Perl e é utilizada em operações de rede. O objetivo principal dessa função é fornecer detalhes sobre a conexão estabelecida, como o endereço IP e a porta do cliente que está se comunicando com o servidor.

### Uso
A função é chamada na forma:

```perl
my $address = getpeername($socket);
```

Onde `$socket` é um socket previamente criado e conectado. O retorno de `getpeername` é uma string binária que representa o endereço remoto. Para obter informações mais utilizáveis, essa string deve ser convertida usando funções como `unpack`.

### Detalhes Adicionais
- **Módulo Necessário**: Para utilizar `getpeername`, é necessário o módulo `Socket`, que deve ser incluído no seu script Perl com `use Socket;`.
- **Formato do Retorno**: O retorno é um endereço em formato binário. Para convertê-lo em um formato legível, pode-se usar `unpack` junto com a constante `AF_INET` para endereços IPv4.

## Exemplos

### Exemplo Básico
```perl
use strict;
use warnings;
use Socket;

my $socket = ...;  # Assume que o socket já está criado e conectado
my $address = getpeername($socket);

my ($port, $iaddr) = unpack_sockaddr_in($address);
my $ip_address = inet_ntoa($iaddr);

print "Endereço IP do cliente: $ip_address, Porta: $port\n";
```

### Exemplo com Servidor
```perl
use strict;
use warnings;
use IO::Socket;
use Socket;

my $server = IO::Socket::INET->new(
    Port => 7890,
    Listen => 5,
    Reuse => 1
) or die "Não foi possível criar o socket: $!";

while (my $client = $server->accept()) {
    my $address = getpeername($client);
    my ($port, $iaddr) = unpack_sockaddr_in($address);
    my $ip_address = inet_ntoa($iaddr);
    
    print "Conexão recebida de: $ip_address na porta: $port\n";
    close $client;
}
```

## Explicação
Um erro comum ao utilizar `getpeername` é esquecer de verificar se o socket está realmente conectado. Se o socket não estiver conectado, a função retornará `undef`, e você deve sempre tratar esse caso em seu código. Além disso, a conversão do endereço retornado para um formato legível deve ser feita corretamente utilizando `unpack`, pois o formato binário não é diretamente utilizável.

É importante também lembrar que `getpeername` só funcionará com sockets que estejam em estado de conexão. Se você tentar chamá-la em um socket que não está conectado, receberá um erro.

## Resumo em Uma Linha
A função `getpeername` em Perl permite obter o endereço remoto de um socket conectado, facilitando a identificação de clientes em aplicações de rede.