<!--
Meta Description: # Chomp em Perl: Removendo Quebras de Linha de Strings ## Sinopse O comando `chomp` em Perl é utilizado para remover quebras de linha do final das str...
Meta Keywords: linha, chomp, perl, que, não
-->

# Chomp em Perl: Removendo Quebras de Linha de Strings

## Sinopse
O comando `chomp` em Perl é utilizado para remover quebras de linha do final das strings, facilitando o tratamento de entradas de dados.

## Documentação
O `chomp` é uma função embutida em Perl que altera a string original, removendo o caractere de nova linha (`\n`) que pode estar presente no final. O uso mais comum do `chomp` é em entradas de dados, como quando se lê uma linha de um arquivo ou da entrada padrão, onde a quebra de linha é automaticamente adicionada.

### Uso
A sintaxe básica do `chomp` é:

```perl
chomp($string);
```

É possível também usar `chomp` em arrays:

```perl
chomp(@array);
```

Neste caso, `chomp` remove a quebra de linha de cada elemento do array.

### Detalhes
- O `chomp` retorna o número de caracteres removidos.
- Se o caractere de nova linha não estiver presente, a string permanece inalterada.
- O `chomp` pode ser chamado sem argumentos, o que remove a quebra de linha da variável `$_`.

## Exemplos

### Exemplo 1: Uso Básico
```perl
my $linha = "Olá, mundo!\n";
chomp($linha);
print $linha;  # Saída: Olá, mundo!
```

### Exemplo 2: Uso em Array
```perl
my @linhas = ("Linha 1\n", "Linha 2\n", "Linha 3\n");
chomp(@linhas);
print join(", ", @linhas);  # Saída: Linha 1, Linha 2, Linha 3
```

### Exemplo 3: Uso Sem Argumentos
```perl
$_ = "Texto com quebra de linha\n";
chomp;  # Remove a quebra de linha de $_
print $_;  # Saída: Texto com quebra de linha
```

## Explicação
O `chomp` é uma ferramenta valiosa, especialmente em scripts que processam dados de entrada. No entanto, há algumas armadilhas que os programadores devem estar cientes:

- **Remoção de Outros Caracteres**: O `chomp` só remove quebras de linha. Se sua string termina com outros caracteres, eles não serão afetados.
- **Uso com Variáveis Não Inicializadas**: Se `chomp` for aplicado a uma variável não inicializada, não causará erro, mas também não terá efeito.
- **Variáveis Globais**: Ao usar `chomp` em arrays, é importante lembrar que ele modifica todos os elementos do array. Isso pode ser inesperado se você não estiver atento.

## Resumo em Uma Linha
O `chomp` em Perl é uma função que remove quebras de linha do final de strings, facilitando o tratamento de dados de entrada.