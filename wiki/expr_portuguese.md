# [Linux] C Shell (csh) expr Uso: Avaliação de expressões

## Overview
O comando `expr` é utilizado no C Shell para avaliar expressões aritméticas, lógicas e de string. Ele permite realizar operações matemáticas simples e manipulações de texto diretamente no terminal.

## Usage
A sintaxe básica do comando `expr` é a seguinte:

```csh
expr [opções] [argumentos]
```

## Common Options
- `+` : Adição.
- `-` : Subtração.
- `*` : Multiplicação (deve ser escapado com uma barra invertida `\*`).
- `/` : Divisão.
- `%` : Módulo.
- `=` : Atribuição de valor.
- `:` : Comparação de strings.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `expr`:

### Exemplo 1: Adição
```csh
expr 5 + 3
```
Saída: `8`

### Exemplo 2: Subtração
```csh
expr 10 - 4
```
Saída: `6`

### Exemplo 3: Multiplicação
```csh
expr 7 \* 6
```
Saída: `42`

### Exemplo 4: Divisão
```csh
expr 20 / 4
```
Saída: `5`

### Exemplo 5: Módulo
```csh
expr 10 % 3
```
Saída: `1`

### Exemplo 6: Comparação de Strings
```csh
expr "hello" : "h.*"
```
Saída: `5` (número de caracteres que correspondem ao padrão)

## Tips
- Sempre escape o asterisco (`*`) com uma barra invertida (`\`) para evitar que o shell o interprete como um caractere curinga.
- Use parênteses para agrupar expressões e garantir a ordem correta das operações.
- O `expr` é útil em scripts para realizar cálculos simples sem a necessidade de uma linguagem de programação mais complexa.