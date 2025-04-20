# [Linux] C Shell (csh) if: Avalia expressões condicionais

## Overview
O comando `if` no C Shell (csh) é utilizado para executar comandos com base na avaliação de uma condição. Se a condição for verdadeira, o bloco de comandos associado é executado; caso contrário, ele é ignorado.

## Usage
A sintaxe básica do comando `if` é a seguinte:

```csh
if ( condição ) then
    comandos
endif
```

## Common Options
O comando `if` não possui opções específicas, mas as condições podem incluir comparações numéricas, de strings e de arquivos. Aqui estão algumas formas comuns de expressões condicionais:

- `-e arquivo`: verifica se o arquivo existe.
- `-d diretório`: verifica se o diretório existe.
- `-f arquivo`: verifica se o arquivo é um arquivo regular.
- `string1 == string2`: verifica se duas strings são iguais.

## Common Examples

### Exemplo 1: Verificar se um arquivo existe
```csh
if ( -e "meuarquivo.txt" ) then
    echo "O arquivo existe."
endif
```

### Exemplo 2: Verificar se um diretório existe
```csh
if ( -d "meudiretorio" ) then
    echo "O diretório existe."
endif
```

### Exemplo 3: Comparar duas strings
```csh
set nome = "João"
if ( "$nome" == "João" ) then
    echo "Olá, João!"
endif
```

### Exemplo 4: Verificar se um arquivo é um arquivo regular
```csh
if ( -f "script.csh" ) then
    echo "É um arquivo regular."
endif
```

## Tips
- Sempre use `endif` para fechar o bloco `if`.
- Utilize parênteses ao redor da condição para garantir que a sintaxe esteja correta.
- Combine o `if` com outros comandos como `else` e `else if` para criar lógica mais complexa.
- Teste suas condições em um ambiente seguro antes de aplicá-las em scripts importantes para evitar erros.