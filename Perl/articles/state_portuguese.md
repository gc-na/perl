<!--
Meta Description: # Estado em Perl: Compreendendo o Comando "state" ## Sinopse O comando `state` em Perl é utilizado para declarar variáveis que mantém seu valor entre ...
Meta Keywords: state, sub, uma, que, chamada
-->

# Estado em Perl: Compreendendo o Comando "state"

## Sinopse
O comando `state` em Perl é utilizado para declarar variáveis que mantém seu valor entre chamadas de uma sub-rotina, permitindo que a variável seja inicializada apenas uma vez e preserve seu estado entre as invocações.

## Documentação
O `state` foi introduzido na versão 5.10 do Perl e é uma maneira eficiente de preservar o estado sem a necessidade de variáveis globais. Diferente das variáveis lexicais normais, que são reinicializadas toda vez que uma sub-rotina é chamada, as variáveis declaradas com `state` retêm seus valores entre as chamadas, tornando-as ideais para contadores, caches ou qualquer situação onde o estado deve ser mantido.

### Propósito
O objetivo do `state` é proporcionar uma forma fácil e segura de gerenciar o estado interno de uma sub-rotina, sem recorrer a variáveis globais que podem causar problemas de escopo e manutenção.

### Uso
Para utilizar o `state`, é necessário declarar uma variável dentro de uma sub-rotina precedida pela palavra-chave `state`. Veja o exemplo abaixo:

```perl
sub contador {
    state $cont = 0;  # Inicializa $cont apenas na primeira chamada
    $cont++;
    return $cont;
}
```

Neste exemplo, `$cont` será inicializado em 0 apenas na primeira chamada da sub-rotina `contador` e incrementará seu valor a cada chamada subsequente.

## Exemplos

### Exemplo Básico
```perl
sub minha_funcao {
    state $chamadas = 0;  # Inicializa apenas na primeira chamada
    $chamadas++;
    print "Esta função foi chamada $chamadas vezes.\n";
}

minha_funcao();  # Saída: Esta função foi chamada 1 vezes.
minha_funcao();  # Saída: Esta função foi chamada 2 vezes.
```

### Uso com Caching
```perl
sub fatorial {
    my ($n) = @_;
    state %cache;  # Cache para armazenar resultados já calculados

    return $cache{$n} if exists $cache{$n};  # Retorna resultado do cache se existir

    my $resultado = 1;
    $resultado *= $_ for 1 .. $n;
    $cache{$n} = $resultado;  # Armazena resultado no cache
    return $resultado;
}

print fatorial(5);  # Saída: 120
print fatorial(5);  # Saída: 120 (usando cache)
```

## Explicação
Um erro comum ao usar `state` é esquecer que a variável mantém seu valor apenas dentro do escopo da sub-rotina. Além disso, não é possível usar `state` fora de uma sub-rotina, o que pode confundir desenvolvedores acostumados com variáveis globais. Outra atenção deve ser dada ao uso de `state` em ambientes multi-thread, pois o estado é particular a cada thread.

## Resumo em Uma Linha
O comando `state` em Perl permite a manutenção de variáveis que retêm seu valor entre chamadas de sub-rotinas, facilitando a gestão de estado interno.