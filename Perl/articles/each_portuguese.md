<!--
Meta Description: # A função "each" no Perl: Iterando sobre Hashes e Arrays ## Sinopse A função `each` em Perl é uma ferramenta poderosa para iterar sobre hashes e arra...
Meta Keywords: each, que, para, elementos, array
-->

# A função "each" no Perl: Iterando sobre Hashes e Arrays

## Sinopse
A função `each` em Perl é uma ferramenta poderosa para iterar sobre hashes e arrays, permitindo acessar os elementos de forma sequencial e conveniente.

## Documentação
A função `each` é utilizada para percorrer os elementos de um hash ou array de forma iterativa. Quando aplicada a um hash, `each` retorna uma lista com uma chave e seu respectivo valor a cada chamada. Ao ser utilizada em um array, `each` fornece os elementos sequencialmente.

### Uso
```perl
while (my ($chave, $valor) = each %hash) {
    print "$chave => $valor\n";
}

while (my $elemento = each @array) {
    print "$elemento\n";
}
```

### Detalhes
- **Para Hashes**: Ao usar `each` em um hash, a função retorna uma lista de dois elementos: a chave e o valor correspondente. Após a última chamada, ela retorna um valor vazio, o que pode ser utilizado para terminar o loop.
  
- **Para Arrays**: Quando aplicada a um array, `each` retorna os elementos do array em ordem, até que não haja mais elementos. Vale ressaltar que `each` em arrays não retorna índices, apenas os valores.

## Exemplos
### Exemplo 1: Iterando sobre um Hash
```perl
my %frutas = (
    'maçã' => 3,
    'banana' => 5,
    'laranja' => 2,
);

while (my ($fruta, $quantidade) = each %frutas) {
    print "Fruta: $fruta, Quantidade: $quantidade\n";
}
```

### Exemplo 2: Iterando sobre um Array
```perl
my @numeros = (10, 20, 30, 40);

while (my $numero = each @numeros) {
    print "Número: $numero\n";
}
```

## Explicação
Um dos principais desafios ao usar `each` é lembrar que, ao final da iteração, a função não retorna `undef` como em outras iterações. Em vez disso, ela retorna um valor vazio, o que pode causar confusão. Além disso, `each` modifica a posição do iterador interno, o que significa que, se você usar `each` em um hash ou array várias vezes, pode não obter os mesmos resultados se não reinicializar a iteração.

Outro ponto importante é que `each` não deve ser utilizado em listas diretamente, pois seu comportamento é definido para hashes e arrays. Para listas, é melhor usar `foreach`.

## Resumo em Uma Linha
A função `each` em Perl permite iterar sobre hashes e arrays, retornando chaves e valores ou elementos sequencialmente, facilitando a manipulação de dados.