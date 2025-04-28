<!--
Meta Description: # socketpair: Criação de Conexões de Socket em Perl ## Sinopse O `socketpair` é uma função em Perl que permite criar um par de sockets conectados, ide...
Meta Keywords: socketpair, socket, socket1, socket2, sockets
-->

# socketpair: Criação de Conexões de Socket em Perl

## Sinopse
O `socketpair` é uma função em Perl que permite criar um par de sockets conectados, ideal para comunicação entre processos. Essa funcionalidade é útil em situações onde os processos precisam trocar mensagens de forma bidirecional.

## Documentação

### Propósito
A função `socketpair` cria um par de sockets que estão diretamente conectados entre si, o que facilita a comunicação entre processos em um ambiente de execução. Esses sockets podem ser utilizados para enviar e receber dados de forma simples e eficiente.

### Uso
A sintaxe básica da função `socketpair` é a seguinte:

```perl
socketpair(SOCKET1, SOCKET2, DOMÍNIO, TIPO, PROTOCOLO);
```

- **SOCKET1** e **SOCKET2**: Referências para as variáveis que receberão os sockets criados.
- **DOMÍNIO**: O domínio do socket (por exemplo, `AF_UNIX` para comunicação local).
- **TIPO**: O tipo de socket (geralmente `SOCK_STREAM` ou `SOCK_DGRAM`).
- **PROTOCOLO**: O protocolo a ser usado (normalmente 0, que seleciona o protocolo padrão).

### Detalhes
O `socketpair` é uma maneira eficiente de implementar comunicação entre processos (IPC) em sistemas Unix-like. Os sockets criados operam de maneira semelhante a tubos (`pipes`), mas com a vantagem de serem independentes de um sistema de arquivos.

## Exemplos

### Exemplo Básico

```perl
use strict;
use warnings;
use IO::Socket;

my ($socket1, $socket2);
socketpair($socket1, $socket2, AF_UNIX, SOCK_STREAM, 0) or die "Não foi possível criar socket pair: $!";

# Enviando uma mensagem pelo socket1
print $socket1 "Olá do socket1!\n";

# Recebendo a mensagem no socket2
my $message = <$socket2>;
print "Mensagem recebida: $message";
```

### Exemplo com Processos Fork

```perl
use strict;
use warnings;
use IO::Socket;
use POSIX ":sys_wait_h";

my ($socket1, $socket2);
socketpair($socket1, $socket2, AF_UNIX, SOCK_STREAM, 0) or die "Não foi possível criar socket pair: $!";

if (my $pid = fork()) {
    # Processo pai
    close $socket2; # Fecha o socket do filho
    print $socket1 "Mensagem do pai\n";
    waitpid($pid, 0);
} else {
    # Processo filho
    close $socket1; # Fecha o socket do pai
    my $msg = <$socket2>;
    print "Recebido no filho: $msg";
}
```

## Explicação

### Armadilhas Comuns
- **Domínios e Tipos**: Certifique-se de especificar corretamente o domínio e o tipo do socket, pois valores incorretos podem resultar em falhas na criação do socket.
- **Erro na Criação**: Sempre verifique se a função `socketpair` retorna um valor verdadeiro. Caso contrário, utilize `$!` para diagnosticar o erro.
- **Fechamento de Sockets**: Não se esqueça de fechar os sockets que não estão sendo utilizados para evitar vazamentos de recursos.

### Notas Adicionais
O `socketpair` é mais comum em sistemas Unix e pode não estar disponível em todos os sistemas operacionais. Além disso, a comunicação através de sockets requer um gerenciamento adequado de erros e controle de fluxo.

## Resumo em Uma Linha
O `socketpair` em Perl cria um par de sockets conectados para facilitar a comunicação entre processos.