<!--
Meta Description: # Atan2: A Função Matemática em Perl para Cálculo de Ângulos ## Sinopse A função `atan2` em Perl é utilizada para calcular o arco tangente de dois val...
Meta Keywords: atan2, função, ângulo, radianos, perl
-->

# Atan2: A Função Matemática em Perl para Cálculo de Ângulos

## Sinopse
A função `atan2` em Perl é utilizada para calcular o arco tangente de dois valores, retornando o ângulo correspondente em radianos. Essa função é especialmente útil em aplicações que requerem o cálculo de ângulos a partir de coordenadas cartesianas.

## Documentação
A função `atan2` é definida na biblioteca padrão do Perl e é utilizada para obter o ângulo em radianos entre o eixo X positivo e o ponto definido por um par de coordenadas `(y, x)`. Sua assinatura é:

```perl
atan2($y, $x)
```

### Propósito
O propósito principal da função `atan2` é calcular o ângulo que representa a direção do vetor `(x, y)` em relação à origem. Isso é valioso em diversas aplicações, como gráficos, jogos, física e matemática.

### Uso
A função aceita dois argumentos:
- `$y`: a coordenada vertical (eixo Y).
- `$x`: a coordenada horizontal (eixo X).

O resultado é um valor em radianos que varia de `-π` a `π`. Se `$x` for zero, o resultado dependerá do valor de `$y`: se `$y` for positivo, o resultado será `π/2`; se `$y` for negativo, o resultado será `-π/2`.

## Exemplos

### Exemplo Básico
```perl
use strict;
use warnings;

my $y = 1;
my $x = 1;
my $angulo = atan2($y, $x);
print "O ângulo em radianos é: $angulo\n";  # Saída: O ângulo em radianos é: 0.785398163397448
```

### Exemplo com Coordenadas Negativas
```perl
use strict;
use warnings;

my $y = -1;
my $x = -1;
my $angulo = atan2($y, $x);
print "O ângulo em radianos é: $angulo\n";  # Saída: O ângulo em radianos é: -2.35619449019234
```

### Exemplo com Eixo Y Zero
```perl
use strict;
use warnings;

my $y = 0;
my $x = 1;
my $angulo = atan2($y, $x);
print "O ângulo em radianos é: $angulo\n";  # Saída: 0
```

## Explicação
É importante ter em mente algumas considerações ao utilizar a função `atan2`:

- **Intervalos de Resultados**: O resultado de `atan2` sempre estará no intervalo de `-π` a `π`. Isso facilita a conversão para graus ou outras unidades angulares.
- **Divisão por Zero**: A função evita problemas de divisão por zero que podem ocorrer ao usar a função `atan` padrão, pois não realiza divisão entre os valores de entrada.
- **Ambiguidade na Quadrante**: `atan2` resolve a ambiguidade que pode surgir ao calcular ângulos apenas com `atan`, pois considera o sinal de ambos os argumentos, permitindo identificar corretamente em qual quadrante o ângulo se encontra.

## Resumo em Uma Linha
A função `atan2` em Perl calcula o ângulo em radianos entre o eixo X e um ponto definido por coordenadas cartesianas, resolvendo problemas de ambiguidade e divisão por zero.