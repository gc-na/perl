# [Linux] C Shell (csh) uniq Uso: Remove linhas duplicadas de um arquivo

## Overview
O comando `uniq` é utilizado para filtrar linhas duplicadas em um arquivo ou na entrada padrão. Ele é especialmente útil quando você deseja obter uma lista de entradas únicas a partir de um conjunto de dados.

## Usage
A sintaxe básica do comando `uniq` é a seguinte:

```
uniq [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `uniq`:

- `-c`: Conta o número de ocorrências de cada linha.
- `-d`: Exibe apenas as linhas duplicadas.
- `-u`: Exibe apenas as linhas únicas.
- `-i`: Ignora diferenças entre maiúsculas e minúsculas ao comparar linhas.

## Common Examples

### Exemplo 1: Remover linhas duplicadas
Para remover linhas duplicadas de um arquivo chamado `arquivo.txt`, você pode usar:

```csh
uniq arquivo.txt
```

### Exemplo 2: Contar ocorrências de linhas
Para contar quantas vezes cada linha aparece em `arquivo.txt`, use:

```csh
uniq -c arquivo.txt
```

### Exemplo 3: Exibir apenas linhas duplicadas
Para mostrar apenas as linhas que aparecem mais de uma vez em `arquivo.txt`, execute:

```csh
uniq -d arquivo.txt
```

### Exemplo 4: Ignorar diferenças de maiúsculas e minúsculas
Para remover duplicatas ignorando a capitalização, utilize:

```csh
uniq -i arquivo.txt
```

## Tips
- Sempre ordene o arquivo antes de usar `uniq`, pois ele só remove duplicatas que estão adjacentes. Você pode usar o comando `sort` para isso.
- Combine `uniq` com outros comandos, como `sort`, para obter resultados mais eficazes. Por exemplo: 

```csh
sort arquivo.txt | uniq
```

- Use a opção `-c` para ter uma visão clara de quantas vezes cada entrada aparece, o que pode ser útil para análises de dados.