<!--
Meta Description: # Função `sub` em Perl: Definindo Sub-rotinas ## Sinopse A palavra-chave `sub` em Perl é utilizada para definir sub-rotinas, que são blocos de código ...
Meta Keywords: sub, rotina, perl, rotinas, que
-->

# Função `sub` em Perl: Definindo Sub-rotinas

## Sinopse
A palavra-chave `sub` em Perl é utilizada para definir sub-rotinas, que são blocos de código reutilizáveis que podem ser chamados em diferentes partes de um programa.

## Documentação
A função `sub` permite a criação de sub-rotinas em Perl, facilitando a modularização do código e a reutilização de lógicas. Uma sub-rotina é definida usando a sintaxe:

```perl
sub nome_da_sub {
    # código a ser executado
}
```

### Propósito
O propósito principal das sub-rotinas é encapsular uma sequência de instruções que podem ser executadas em diferentes momentos dentro do script. Isso ajuda a tornar o código mais organizado e compreensível.

### Uso
Para chamar uma sub-rotina, utiliza-se o nome da sub-rotina seguido por parênteses. Caso a sub-rotina receba parâmetros, eles podem ser passados dentro dos parênteses.

```perl
sub saudacao {
    my ($nome) = @_;  # Recebendo o parâmetro
    print "Olá, $nome!\n";
}

saudacao("Maria");  # Chamando a sub-rotina
```

### Detalhes
- As sub-rotinas podem retornar valores usando a palavra-chave `return`.
- As variáveis criadas dentro da sub-rotina são locais a ela, a menos que sejam declaradas como globais.
- É possível definir sub-rotinas com parâmetros opcionais, utilizando a sintaxe `my ($param1, $param2) = @_;`.

## Exemplos
### Exemplo 1: Sub-rotina Simples
```perl
sub soma {
    my ($a, $b) = @_;
    return $a + $b;
}

my $resultado = soma(5, 10);
print "A soma é: $resultado\n";  # Saída: A soma é: 15
```

### Exemplo 2: Sub-rotina com Parâmetros Opcionais
```perl
sub saudacao {
    my ($nome, $saudacao) = @_;
    $saudacao //= "Olá";  # Saudação padrão
    return "$saudacao, $nome!";
}

print saudacao("João");                # Saída: Olá, João!
print saudacao("Maria", "Bom dia");   # Saída: Bom dia, Maria!
```

## Explicação
Ao trabalhar com sub-rotinas, é importante lembrar que:

- **Escopo**: Variáveis declaradas dentro de uma sub-rotina são locais e não afetam o escopo global, a menos que sejam definidas explicitamente como globais.
- **Parâmetros**: Os parâmetros são passados através da lista especial `@_`, que contém todos os argumentos fornecidos na chamada da sub-rotina.
- **Retorno**: O valor retornado por uma sub-rotina é o último valor avaliado ou pode ser explicitamente retornado com `return`.

Erros comuns incluem esquecer de usar `my` ao declarar variáveis dentro da sub-rotina, o que pode levar a conflitos de nome com variáveis globais.

## Resumo em Uma Linha
A palavra-chave `sub` em Perl é utilizada para definir sub-rotinas, permitindo a reutilização e organização do código.