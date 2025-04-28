<!--
Meta Description: # getsockname: Função para Obter o Endereço Local de um Socket em Perl ## Sinopse A função `getsockname` em Perl é utilizada para recuperar o endereço...
Meta Keywords: socket, endereço, getsockname, local, perl
-->

# getsockname: Função para Obter o Endereço Local de um Socket em Perl

## Sinopse
A função `getsockname` em Perl é utilizada para recuperar o endereço local associado a um socket, permitindo que desenvolvedores obtenham informações sobre a conexão estabelecida.

## Documentação
A função `getsockname` pertence à biblioteca `Socket` do Perl e é utilizada para determinar o endereço local de um socket que já foi criado e possivelmente ligado a uma porta. Isso é especialmente útil em aplicações de rede que necessitam saber qual endereço IP e porta estão sendo utilizados após a configuração do socket.

### Uso
Para usar `getsockname`, você deve primeiro criar um socket utilizando `socket()` e, em seguida, ligar o socket a um endereço com `bind()`. Após isso, você pode chamar `getsockname()` para obter o endereço local.

```perl
use Socket;

# Criação do socket
socket(my $socket, PF_INET, SOCK_STREAM, 0) or die "Não foi possível criar o socket: $!";

# Ligar o socket a um endereço
my $port = 8080;
my $ip = inet_aton('127.0.0.1');
bind($socket, sockaddr_in($port, $ip)) or die "Não foi possível ligar o socket: $!";

# Obter o endereço local
my $local_address = getsockname($socket);
my ($local_port, $local_ip) = sockaddr_in($local_address);
print "Endereço local: " . inet_ntoa($local_ip) . ":" . ntohs($local_port) . "\n";
```

## Exemplos
### Exemplo Básico
```perl
use Socket;

# Cria um socket e o liga
socket(my $sock, PF_INET, SOCK_STREAM, 0) or die "Erro ao criar o socket: $!";
my $port = 8080;
my $ip = inet_aton('127.0.0.1');
bind($sock, sockaddr_in($port, $ip)) or die "Erro ao ligar o socket: $!";

# Obtém o endereço local
my $local_addr = getsockname($sock);
my ($local_port, $local_ip) = sockaddr_in($local_addr);
print "IP local: " . inet_ntoa($local_ip) . ", Porta local: " . ntohs($local_port) . "\n";
```

### Exemplo com Múltiplas Conexões
```perl
use Socket;

# Criação de um socket
socket(my $sock, PF_INET, SOCK_STREAM, 0) or die "Não foi possível criar o socket: $!";
bind($sock, sockaddr_in(0, INADDR_ANY)) or die "Não foi possível ligar o socket: $!";
listen($sock, SOMAXCONN) or die "Não foi possível escutar: $!";

# Obter o endereço após o listen
my $local_addr = getsockname($sock);
my ($local_port, $local_ip) = sockaddr_in($local_addr);
print "Servidor escutando em " . inet_ntoa($local_ip) . ":" . ntohs($local_port) . "\n";
```

## Explicação
### Armadilhas Comuns
- **Socket não ligado**: Tentar chamar `getsockname` em um socket que não foi ligado com `bind()` resultará em erro. Certifique-se de que o socket está corretamente configurado antes de fazer a chamada.
- **Endereço IPv6**: A função `getsockname` funciona com IPv4 e IPv6, mas atenção deve ser dada ao formato dos endereços retornados.
- **Uso em ambientes restritos**: Em alguns ambientes de execução, pode haver restrições de segurança que impeçam o uso de sockets, resultando em falhas.

## Resumo em Uma Linha
A função `getsockname` em Perl permite recuperar o endereço local de um socket, essencial para aplicações de rede que precisam saber qual IP e porta estão sendo utilizados.