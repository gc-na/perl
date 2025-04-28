<!--
Meta Description: # sprintf em Perl: Formatação de Strings com Estilo ## Sinopse O `sprintf` é uma função em Perl que permite formatar strings de maneira controlada, ut...
Meta Keywords: formato, sprintf, para, que, perl
-->

# sprintf em Perl: Formatação de Strings com Estilo

## Sinopse
O `sprintf` é uma função em Perl que permite formatar strings de maneira controlada, utilizando especificadores de formato para criar saídas personalizadas e bem-estruturadas.

## Documentação
### Propósito
O `sprintf` é utilizado para formatar strings de acordo com um formato especificado. Ele é frequentemente empregado para produzir saídas que requerem um controle fino sobre a apresentação, como números com casas decimais, alinhamento de texto e inclusão de caracteres especiais.

### Uso
A sintaxe básica do `sprintf` é:

```perl
sprintf(FORMATO, LISTA_DE_VALORES);
```

- **FORMATO**: Uma string que contém especificadores de formato.
- **LISTA_DE_VALORES**: Os valores que serão formatados de acordo com o formato especificado.

### Especificadores de Formato
Os especificadores de formato comuns incluem:

- `%d`: Para inteiros.
- `%f`: Para números de ponto flutuante.
- `%s`: Para strings.
- `%x`: Para números em formato hexadecimal.
- `%o`: Para números em formato octal.

## Exemplos
### Exemplo 1: Formatação de Inteiros
```perl
my $numero = 42;
my $string_formatada = sprintf("O número é: %d", $numero);
print $string_formatada; # Saída: O número é: 42
```

### Exemplo 2: Formatação de Números de Ponto Flutuante
```perl
my $preco = 9.99;
my $string_formatada = sprintf("O preço é: R$ %.2f", $preco);
print $string_formatada; # Saída: O preço é: R$ 9.99
```

### Exemplo 3: Formatação de Strings
```perl
my $nome = "João";
my $idade = 30;
my $string_formatada = sprintf("%s tem %d anos.", $nome, $idade);
print $string_formatada; # Saída: João tem 30 anos.
```

## Explicação
Embora o `sprintf` seja uma ferramenta poderosa, existem alguns cuidados que devem ser tomados:

- **Tipos de Dados**: Certifique-se de que os dados passados correspondem aos especificadores de formato. Um número passado para um `%s` pode causar comportamento inesperado.
- **Alinhamento**: Para alinhar texto, você pode usar modificadores como `%10s`, que alinha à direita em um campo de 10 caracteres.
- **Limites de Precisão**: Ao formatar números de ponto flutuante, o número de casas decimais pode ser controlado. Por exemplo, `%.3f` apresentará três casas decimais.

## Resumo em Uma Linha
O `sprintf` em Perl é uma função que formata strings de forma controlada, permitindo personalizar a apresentação de dados com precisão e flexibilidade.