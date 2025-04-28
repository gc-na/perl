<!--
Meta Description: # Comando `stat` em Perl: Análise de Arquivos e Diretórios ## Sinopse O comando `stat` em Perl permite obter informações detalhadas sobre um arquivo o...
Meta Keywords: arquivo, stat, tamanho, permissões, info
-->

# Comando `stat` em Perl: Análise de Arquivos e Diretórios

## Sinopse
O comando `stat` em Perl permite obter informações detalhadas sobre um arquivo ou diretório, como tamanho, permissões, timestamps de acesso e modificação, entre outros.

## Documentação
O `stat` é uma função incorporada em Perl que retorna uma lista com informações sobre um arquivo especificado. Os dados retornados incluem:

- **Inode**: O número do inode do arquivo.
- **Tamanho**: O tamanho do arquivo em bytes.
- **Tipo de arquivo**: Indica se o arquivo é um regular, diretório, link simbólico, etc.
- **Permissões**: As permissões do arquivo, que indicam quem pode ler, escrever ou executar o arquivo.
- **Timestamps**: Informações sobre o último acesso, modificação e mudança de status do arquivo.

### Uso
A sintaxe básica da função `stat` é:

```perl
@info = stat($arquivo);
```

Onde `$arquivo` é o caminho para o arquivo ou diretório que você deseja analisar. A função retorna uma lista com 13 elementos, que pode ser acessada diretamente ou através de um array.

### Detalhes
Os elementos retornados pela função `stat` são:

1. Inode
2. Tamanho do arquivo (em bytes)
3. Modo de arquivo (permissões e tipo)
4. Número de links
5. ID do usuário (UID) do proprietário
6. ID do grupo (GID) do proprietário
7. Hora da última modificação
8. Hora do último acesso
9. Hora da última mudança de status
10. Tamanho da alocação
11. ID do dispositivo
12. ID do dispositivo de bloco
13. Tamanho do arquivo (em bytes, novamente)

## Exemplos
### Exemplo 1: Obtendo informações de um arquivo
```perl
use strict;
use warnings;

my $arquivo = 'exemplo.txt';
my @info = stat($arquivo);

if (@info) {
    print "Tamanho do arquivo: $info[7] bytes\n"; # Elemento 7 é o tamanho
    print "Última modificação: ", scalar(localtime($info[9])), "\n"; # Elemento 9 é o timestamp da última modificação
} else {
    warn "Não foi possível obter informações do arquivo: $!\n";
}
```

### Exemplo 2: Verificando permissões de um diretório
```perl
use strict;
use warnings;

my $diretorio = 'meu_diretorio';
my @info = stat($diretorio);

if (@info) {
    my $permissoes = sprintf "%04o", $info[2] & 07777; # Elemento 2 contém as permissões
    print "Permissões do diretório: $permissoes\n";
} else {
    warn "Não foi possível obter informações do diretório: $!\n";
}
```

## Explicação
Uma armadilha comum ao usar `stat` é não verificar se o arquivo ou diretório realmente existe antes de chamar a função. Isso pode resultar em erros ou avisos, como "Arquivo não encontrado". É sempre uma boa prática validar a existência do arquivo com uma verificação simples, como `-e $arquivo`, antes de usar `stat`. Além disso, os elementos retornados de `stat` podem ser diferentes em sistemas de arquivos diversos, então é importante estar ciente do ambiente em que seu script está sendo executado.

## Resumo em uma linha
O comando `stat` em Perl fornece informações detalhadas sobre arquivos e diretórios, incluindo tamanhos, permissões e timestamps.