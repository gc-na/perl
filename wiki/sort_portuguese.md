# [Linux] C Shell (csh) sort Uso: Ordenar linhas de texto

## Overview
O comando `sort` é utilizado para ordenar linhas de texto em um arquivo ou na entrada padrão. Ele pode ser usado para organizar dados de forma alfabética ou numérica, facilitando a análise e a visualização das informações.

## Usage
A sintaxe básica do comando `sort` é a seguinte:

```
sort [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `sort`:

- `-r`: Ordena as linhas em ordem reversa.
- `-n`: Realiza a ordenação numérica.
- `-k`: Especifica a coluna a ser usada como chave para a ordenação.
- `-u`: Remove linhas duplicadas da saída.
- `-o`: Escreve a saída em um arquivo específico.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `sort`:

1. **Ordenar um arquivo de texto em ordem alfabética:**
   ```csh
   sort arquivo.txt
   ```

2. **Ordenar um arquivo em ordem reversa:**
   ```csh
   sort -r arquivo.txt
   ```

3. **Ordenar números em um arquivo:**
   ```csh
   sort -n numeros.txt
   ```

4. **Ordenar um arquivo e remover duplicatas:**
   ```csh
   sort -u arquivo.txt
   ```

5. **Ordenar um arquivo com base na segunda coluna:**
   ```csh
   sort -k 2 arquivo.txt
   ```

6. **Salvar a saída ordenada em um novo arquivo:**
   ```csh
   sort arquivo.txt -o arquivo_ordenado.txt
   ```

## Tips
- Sempre verifique o conteúdo do arquivo original antes de usar a opção `-o`, pois ela sobrescreve o arquivo de saída.
- Use a opção `-n` ao ordenar números para garantir que a ordenação seja feita corretamente, em vez de alfabética.
- Combine opções para obter resultados mais específicos, como `sort -r -n` para ordenar números em ordem reversa.