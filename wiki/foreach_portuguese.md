# [Linux] C Shell (csh) foreach uso: Executa um comando para cada item em uma lista

## Overview
O comando `foreach` no C Shell (csh) é utilizado para executar um bloco de comandos para cada item em uma lista. É uma maneira eficiente de iterar sobre elementos, permitindo que você execute operações repetitivas sem precisar escrever um loop manualmente.

## Usage
A sintaxe básica do comando `foreach` é a seguinte:

```csh
foreach variável (lista)
    comando
end
```

## Common Options
O comando `foreach` não possui muitas opções, mas aqui estão algumas considerações importantes:

- `variável`: O nome da variável que irá armazenar o valor atual da iteração.
- `lista`: A lista de itens sobre os quais você deseja iterar.
- `comando`: O comando ou bloco de comandos que será executado para cada item da lista.

## Common Examples

### Exemplo 1: Listar arquivos
Este exemplo itera sobre todos os arquivos no diretório atual e os lista.

```csh
foreach arquivo (*)
    echo $arquivo
end
```

### Exemplo 2: Renomear arquivos
Este exemplo renomeia todos os arquivos `.txt` adicionando um prefixo "old_".

```csh
foreach arquivo (*.txt)
    mv $arquivo old_$arquivo
end
```

### Exemplo 3: Executar um comando em múltiplos diretórios
Neste exemplo, o comando `ls` é executado em vários diretórios especificados.

```csh
foreach dir (dir1 dir2 dir3)
    echo "Conteúdo de $dir:"
    ls $dir
end
```

## Tips
- Sempre use `end` para fechar o bloco `foreach`.
- Utilize aspas se os nomes dos arquivos ou diretórios contiverem espaços.
- Teste seus comandos com um pequeno conjunto de dados antes de executar em um grande número de arquivos para evitar erros.