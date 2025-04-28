<!--
Meta Description: # sqrt: Função de Raiz Quadrada em Perl ## Sinopse A função `sqrt` em Perl é utilizada para calcular a raiz quadrada de um número. É uma função fundam...
Meta Keywords: raiz, quadrada, número, sqrt, função
-->

# sqrt: Função de Raiz Quadrada em Perl

## Sinopse
A função `sqrt` em Perl é utilizada para calcular a raiz quadrada de um número. É uma função fundamental para operações matemáticas e é frequentemente utilizada em cálculos científicos e financeiros.

## Documentação
A função `sqrt` faz parte da biblioteca padrão do Perl e permite que os desenvolvedores obtenham a raiz quadrada de um número não negativo. A sintaxe básica é:

```perl
my $raiz_quadrada = sqrt($numero);
```

### Propósito
A função `sqrt` é usada para calcular a raiz quadrada de um valor numérico. Este valor deve ser um número não negativo, pois a raiz quadrada de números negativos não é definida no conjunto dos números reais.

### Uso
Para utilizar a função `sqrt`, basta passar um número como argumento. O resultado será a raiz quadrada desse número. Se o argumento for uma string que representa um número, Perl irá automaticamente convertê-la para um número.

### Detalhes
- **Argumentos**: Um único argumento numérico (não negativo).
- **Retorno**: A função retorna a raiz quadrada do número.
- **Comportamento com Strings**: Strings que podem ser convertidas em números são aceitas.
- **Erro**: Se o número fornecido for negativo, `sqrt` retornará `NaN` (Not a Number).

## Exemplos
Aqui estão alguns exemplos básicos de como utilizar a função `sqrt` em Perl:

```perl
# Exemplo 1: Raiz quadrada de um número inteiro
my $numero = 16;
my $resultado = sqrt($numero);
print "A raiz quadrada de $numero é $resultado.\n";  # Saída: A raiz quadrada de 16 é 4.

# Exemplo 2: Raiz quadrada de um número decimal
my $numero_decimal = 20.25;
my $resultado_decimal = sqrt($numero_decimal);
print "A raiz quadrada de $numero_decimal é $resultado_decimal.\n";  # Saída: A raiz quadrada de 20.25 é 4.5.

# Exemplo 3: Raiz quadrada de uma string numérica
my $string_numero = "25";
my $resultado_string = sqrt($string_numero);
print "A raiz quadrada de $string_numero é $resultado_string.\n";  # Saída: A raiz quadrada de 25 é 5.
```

## Explicação
Embora a função `sqrt` seja simples de usar, é importante lembrar que ela não aceita números negativos. Tentar calcular a raiz quadrada de um número negativo resultará em `NaN`, o que pode causar confusão em operações subsequentes. Além disso, é bom ter atenção ao tipo de dados que está sendo passado para a função, já que a conversão automática de strings pode levar a resultados inesperados se o conteúdo da string não for um número válido.

## Resumo em Uma Linha
A função `sqrt` em Perl calcula a raiz quadrada de um número não negativo, retornando `NaN` para números negativos.