<!--
Meta Description: # Renomear Arquivos e Diretórios em Perl: Um Guia Completo ## Sinopse O comando `rename` em Perl é uma ferramenta poderosa utilizada para alterar o no...
Meta Keywords: arquivos, rename, renomear, perl, arquivo
-->

# Renomear Arquivos e Diretórios em Perl: Um Guia Completo

## Sinopse
O comando `rename` em Perl é uma ferramenta poderosa utilizada para alterar o nome de arquivos e diretórios de forma eficiente, permitindo a automação de tarefas de manipulação de nomes.

## Documentação
O `rename` é uma função do Perl que facilita a alteração de nomes de arquivos usando expressões regulares ou substituições de texto. Essa funcionalidade é especialmente útil em scripts que necessitam modificar múltiplos arquivos de uma só vez.

### Propósito
O principal objetivo do `rename` é simplificar o processo de renomeação de arquivos, permitindo que os desenvolvedores apliquem alterações em massa em nomes de arquivos conforme necessário.

### Uso
O uso básico do comando `rename` em Perl pode ser realizado da seguinte maneira:

```perl
rename( 'nome_antigo', 'nome_novo' );
```

No entanto, o uso mais comum é com expressões regulares, que permite renomear múltiplos arquivos de uma só vez. A sintaxe é:

```perl
rename 'expressão_regular', 'nova_expressão', @arquivos;
```

### Detalhes
- **Expressões Regulares**: O `rename` utiliza expressões regulares para identificar e modificar nomes de arquivos, o que oferece grande flexibilidade.
- **Lista de Arquivos**: O comando pode aceitar uma lista de arquivos, permitindo renomear vários de uma vez.
- **Verificações**: Antes de executar a renomeação, é recomendado verificar se os arquivos existem e se não ocorrerão conflitos de nomes.

## Exemplos
### Exemplo 1: Renomear um único arquivo
```perl
use strict;
use warnings;

rename('arquivo_antigo.txt', 'arquivo_novo.txt') or die "Erro ao renomear: $!";
```

### Exemplo 2: Usar expressões regulares
```perl
use strict;
use warnings;

my @arquivos = glob("*.txt");
foreach my $arquivo (@arquivos) {
    rename($arquivo, $arquivo =~ s/antigo/novo/r) or warn "Erro ao renomear $arquivo: $!";
}
```

### Exemplo 3: Renomear arquivos com prefixo
```perl
use strict;
use warnings;

my @arquivos = glob("*.jpg");
foreach my $arquivo (@arquivos) {
    rename($arquivo, "nova_$arquivo") or warn "Erro ao renomear $arquivo: $!";
}
```

## Explicação
### Armadilhas Comuns
- **Permissões**: Certifique-se de que o script tenha permissões adequadas para renomear os arquivos.
- **Conflitos de Nomes**: Ao renomear arquivos, é importante garantir que não haja arquivos com nomes duplicados, pois isso pode resultar em perda de dados.
- **Erro de Execução**: Sempre verifique o retorno da função `rename` para lidar com possíveis erros, utilizando `warn` ou `die` para obter mensagens de erro úteis.

## Resumo em Uma Linha
O comando `rename` em Perl permite renomear arquivos e diretórios de forma eficiente utilizando expressões regulares, facilitando a automação de tarefas de manipulação de nomes.