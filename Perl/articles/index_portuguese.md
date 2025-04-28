<!--
Meta Description: # Índice em Perl: Compreendendo a Função `index` ## Sinopse A função `index` em Perl é utilizada para localizar a posição de uma substring dentro de u...
Meta Keywords: string, index, substring, uma, perl
-->

# Índice em Perl: Compreendendo a Função `index`

## Sinopse
A função `index` em Perl é utilizada para localizar a posição de uma substring dentro de uma string, retornando o índice da primeira ocorrência da substring ou -1 se não encontrada.

## Documentação
A função `index` é uma ferramenta poderosa em Perl para manipulação de strings. Seu propósito principal é buscar a posição de uma substring específica em uma string maior.

### Uso
A sintaxe básica da função `index` é a seguinte:

```perl
index STRING, SUBSTRING, [POSIÇÃO_INICIAL]
```

- **STRING**: A string em que a busca será realizada.
- **SUBSTRING**: A substring que você deseja localizar.
- **POSIÇÃO_INICIAL** (opcional): Um índice a partir do qual a busca deve começar. O padrão é 0, ou seja, o início da string.

### Retorno
- Retorna o índice da primeira ocorrência de `SUBSTRING` em `STRING`.
- Retorna -1 se a `SUBSTRING` não for encontrada.

## Exemplos
Aqui estão alguns exemplos básicos de uso da função `index`:

```perl
# Exemplo 1: Busca simples
my $string = "Perl é uma linguagem de programação";
my $pos = index($string, "linguagem");
print "A substring 'linguagem' começa na posição: $pos\n"; # Saída: 10

# Exemplo 2: Substring não encontrada
my $pos2 = index($string, "Python");
print "A substring 'Python' começa na posição: $pos2\n"; # Saída: -1

# Exemplo 3: Busca a partir de uma posição inicial
my $pos3 = index($string, "a", 5);
print "A próxima ocorrência de 'a' a partir da posição 5 está em: $pos3\n"; # Saída: 14
```

## Explicação
Embora a função `index` seja simples de usar, existem alguns pontos a serem considerados:

- **Case Sensitive**: A função `index` é sensível a maiúsculas e minúsculas. Por exemplo, `index("Perl", "perl")` retornará -1.
- **Substrings Vazias**: Se a substring for uma string vazia, `index` retornará a posição 0, pois uma string vazia é considerada presente em qualquer lugar.
- **Início da Busca**: Se a posição inicial for maior que o comprimento da string, o retorno será -1.

## Resumo em Uma Linha
A função `index` em Perl localiza a posição da primeira ocorrência de uma substring em uma string, retornando -1 se não encontrada.