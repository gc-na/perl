<!--
Meta Description: # rindex em Perl: Encontre a Última Ocorrência de uma Substring ## Sinopse O `rindex` é uma função da linguagem de programação Perl utilizada para enc...
Meta Keywords: perl, uma, rindex, substring, string
-->

# rindex em Perl: Encontre a Última Ocorrência de uma Substring

## Sinopse
O `rindex` é uma função da linguagem de programação Perl utilizada para encontrar a posição da última ocorrência de uma substring dentro de uma string. Essa função é especialmente útil em manipulações de texto, onde a localização da última instância de um padrão é necessária.

## Documentação
### Propósito
A função `rindex` tem como objetivo localizar a última ocorrência de uma substring em uma string principal. Caso a substring não seja encontrada, `rindex` retorna -1.

### Uso
A sintaxe básica da função `rindex` é:
```perl
rindex(string, substring, [offset])
```
- **string**: A string onde a busca será realizada.
- **substring**: A substring que se deseja localizar.
- **offset** (opcional): Um número que especifica a posição da string a partir da qual a busca deve começar. Se não for especificado, a busca começa do final da string.

### Detalhes
- O valor retornado por `rindex` é baseado em um índice que começa em 0, ou seja, a primeira letra da string tem índice 0.
- A função é sensível a maiúsculas e minúsculas.

## Exemplos
### Exemplo Básico
```perl
my $texto = "Perl é uma linguagem de programação. Perl é poderosa.";
my $posicao = rindex($texto, "Perl");
print "Última ocorrência de 'Perl' está na posição: $posicao\n";  # Saída: 30
```

### Exemplo com Offset
```perl
my $texto = "Perl é uma linguagem de programação. Perl é poderosa.";
my $posicao = rindex($texto, "Perl", 25);
print "Última ocorrência de 'Perl' antes da posição 25 está na posição: $posicao\n";  # Saída: 0
```

## Explicação
Uma armadilha comum ao usar `rindex` é não perceber que a função é sensível a maiúsculas e minúsculas. Portanto, "perl" e "Perl" são considerados diferentes. Além disso, ao utilizar o parâmetro de offset, é importante lembrar que a busca é feita da direita para a esquerda a partir da posição especificada.

Outra observação importante é que se a substring não for encontrada, o retorno será -1, o que pode ser um indicativo para lidar com condições em seu código.

## Resumo em Uma Linha
A função `rindex` em Perl localiza a última ocorrência de uma substring em uma string, retornando sua posição ou -1 se não encontrada.