# [Linux] C Shell (csh) nl Uso: Numera linhas em arquivos de texto

## Overview
O comando `nl` é utilizado para numerar as linhas de um arquivo de texto. Ele é especialmente útil para facilitar a leitura e a referência a partes específicas de um documento.

## Usage
A sintaxe básica do comando `nl` é a seguinte:

```csh
nl [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `nl`:

- `-b`: Define o método de numeração das linhas. Pode ser `a` (numera todas as linhas), `t` (numera apenas linhas não vazias) ou `n` (não numera).
- `-f`: Especifica o número de linhas a serem ignoradas no início do arquivo.
- `-h`: Adiciona um cabeçalho antes da numeração das linhas.
- `-v`: Define o número inicial para a numeração das linhas.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `nl`:

1. **Numerar todas as linhas de um arquivo:**
   ```csh
   nl arquivo.txt
   ```

2. **Numerar apenas linhas não vazias:**
   ```csh
   nl -b t arquivo.txt
   ```

3. **Ignorar as primeiras 2 linhas de um arquivo:**
   ```csh
   nl -f 2 arquivo.txt
   ```

4. **Adicionar um cabeçalho antes da numeração:**
   ```csh
   nl -h "Cabeçalho" arquivo.txt
   ```

5. **Começar a numeração a partir de 10:**
   ```csh
   nl -v 10 arquivo.txt
   ```

## Tips
- Utilize a opção `-b t` se você deseja uma numeração mais limpa, focando apenas nas linhas que contêm texto.
- Combine várias opções para personalizar a saída de acordo com suas necessidades.
- Experimente redirecionar a saída para um novo arquivo usando `>` para salvar a numeração em um novo documento. Por exemplo:
  ```csh
  nl arquivo.txt > numerado.txt
  ```