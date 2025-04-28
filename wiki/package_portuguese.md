<!--
Meta Description: # Package em Perl: Estrutura e Organização de Código ## Sinopse O `package` em Perl é uma declaração que permite a criação de namespaces, facilitando ...
Meta Keywords: package, que, perl, sub, para
-->

# Package em Perl: Estrutura e Organização de Código

## Sinopse
O `package` em Perl é uma declaração que permite a criação de namespaces, facilitando a organização e a modularização do código, além de possibilitar a definição de classes em programação orientada a objetos.

## Documentação
O comando `package` é utilizado para definir um novo namespace em Perl. Isso é essencial para evitar conflitos entre nomes de variáveis, sub-rotinas e funções em projetos maiores ou ao usar módulos de terceiros. Quando você declara um `package`, todas as sub-rotinas e variáveis que você criar a seguir pertencem a esse namespace.

### Uso
A sintaxe básica para declarar um novo package é:
```perl
package NomeDoPacote;
```
Após a declaração, você pode definir sub-rotinas e variáveis que serão acessíveis dentro desse namespace.

### Detalhes
- **Namespaces**: Cada package cria um namespace separado. Quando você chama uma sub-rotina, você pode precisar especificar o namespace, a menos que ela esteja no package atual.
- **Importação**: É comum usar o `use` para importar sub-rotinas de um package para outro.
- **Herança**: Em programação orientada a objetos, o `package` permite a definição de classes e a herança entre elas.

## Exemplos

### Exemplo 1: Criando um Package Simples
```perl
package MeuPacote;

sub ola {
    return "Olá, mundo!";
}

1; # Indica que o package foi carregado com sucesso
```

### Exemplo 2: Usando um Package
```perl
use MeuPacote;

print MeuPacote::ola(); # Saída: Olá, mundo!
```

### Exemplo 3: Herança com Packages
```perl
package Animal;
sub falar {
    return "Som do animal";
}

package Cachorro;
our @ISA = qw(Animal); # Herança de Animal

sub falar {
    return "Au Au";
}

package main;
my $dog = Cachorro->new();
print $dog->falar(); # Saída: Au Au
```

## Explicação
Um dos principais problemas que os desenvolvedores enfrentam ao usar packages é a confusão sobre o escopo das variáveis. Variáveis definidas dentro de um package não são acessíveis diretamente fora dele, a menos que sejam exportadas ou chamadas com o nome do package. Além disso, ao utilizar herança, é importante garantir que a lista de superclasses `@ISA` esteja corretamente definida para que a herança funcione como esperado.

Outro ponto a se considerar é o uso de `my`, `our`, e `local`, que afetam a visibilidade das variáveis dentro do namespace do package.

## Resumo em Uma Linha
O `package` em Perl é uma declaração que organiza o código em namespaces distintos, essencial para a modularização e a programação orientada a objetos.