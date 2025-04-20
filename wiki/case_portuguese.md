# [Linux] C Shell (csh) case: Avaliação de padrões de string

## Overview
O comando `case` no C Shell (csh) é utilizado para realizar a avaliação de padrões de string. Ele permite que você execute diferentes comandos com base em correspondências de padrões, facilitando a execução de lógica condicional em scripts.

## Usage
A sintaxe básica do comando `case` é a seguinte:

```csh
case [variável] in
    [padrão1]) comando1 ;;
    [padrão2]) comando2 ;;
    ...
    *) comando_default ;;
esac
```

## Common Options
O comando `case` não possui opções específicas, mas é importante seguir a estrutura correta para garantir que funcione como esperado. Os padrões podem incluir caracteres curinga como `*` e `?`.

## Common Examples

### Exemplo 1: Avaliação de um número
```csh
set num = 2
case $num in
    1) echo "Um" ;;
    2) echo "Dois" ;;
    3) echo "Três" ;;
    *) echo "Número desconhecido" ;;
esac
```

### Exemplo 2: Avaliação de uma string
```csh
set cor = "vermelho"
case $cor in
    "vermelho") echo "A cor é vermelho" ;;
    "verde") echo "A cor é verde" ;;
    "azul") echo "A cor é azul" ;;
    *) echo "Cor não reconhecida" ;;
esac
```

### Exemplo 3: Uso de caracteres curinga
```csh
set arquivo = "documento.txt"
case $arquivo in
    *.txt) echo "É um arquivo de texto" ;;
    *.jpg) echo "É uma imagem JPG" ;;
    *) echo "Tipo de arquivo desconhecido" ;;
esac
```

## Tips
- Sempre termine cada bloco de comando com `;;` para evitar erros de sintaxe.
- Utilize caracteres curinga para simplificar a correspondência de padrões.
- Mantenha a lógica clara e organizada para facilitar a leitura e manutenção do script.