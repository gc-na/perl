<!--
Meta Description: # Redo no Perl: Comando e Utilização ## Sinopse O comando `redo` em Perl é uma palavra-chave que permite reexecutar a iteração atual de um loop, sem a...
Meta Keywords: redo, loop, iteração, que, perl
-->

# Redo no Perl: Comando e Utilização

## Sinopse
O comando `redo` em Perl é uma palavra-chave que permite reexecutar a iteração atual de um loop, sem avançar para a próxima iteração. É uma ferramenta útil para manipulação de fluxos de controle em loops.

## Documentação
O `redo` é frequentemente utilizado dentro de estruturas de repetição, como `while`, `for` e `foreach`. Quando `redo` é chamado, a execução do loop reinicia a partir do início do bloco, ignorando qualquer código que esteja abaixo dele na iteração atual. Isso pode ser útil em situações onde você deseja repetir um passo específico sem perder o estado atual do loop.

### Sintaxe
```perl
redo;
```

### Uso
O `redo` deve ser utilizado dentro de um loop. Aqui está um exemplo básico:

```perl
while (my $i = <STDIN>) {
    chomp $i;
    if ($i eq 'retry') {
        print "Tentando novamente...\n";
        redo;  # Reexecuta o loop sem avançar
    }
    print "Você digitou: $i\n";
}
```

## Exemplos
### Exemplo 1: Redo em um loop `while`
```perl
my $count = 0;

while ($count < 5) {
    print "Digite um número (ou 'redo' para repetir): ";
    my $input = <STDIN>;
    chomp $input;

    if ($input eq 'redo') {
        print "Repetindo a iteração...\n";
        redo;  # Reexecuta a iteração atual
    }

    print "Número recebido: $input\n";
    $count++;
}
```

### Exemplo 2: Redo em um loop `for`
```perl
for my $i (1..5) {
    print "Contagem: $i\n";
    if ($i == 3) {
        print "Repetindo a contagem...\n";
        redo;  # Reexecuta a iteração quando i é igual a 3
    }
}
```

## Explicação
Uma armadilha comum ao usar `redo` é não perceber que ele reinicia apenas a iteração atual, não o loop inteiro. Isso significa que qualquer modificação no estado do loop (como variáveis de controle) não será revertida. Além disso, é importante lembrar que `redo` não pode ser usado fora de um loop, o que resultará em um erro de compilação.

O `redo` é muitas vezes confundido com `next` e `last`, que controlam a iteração e a saída do loop, respectivamente. Enquanto `next` pula para a próxima iteração e `last` termina o loop, `redo` simplesmente reinicia a iteração atual.

## Resumo em Uma Linha
O comando `redo` em Perl permite reexecutar a iteração atual de um loop, ignorando qualquer código que segue a palavra-chave dentro do bloco do loop.