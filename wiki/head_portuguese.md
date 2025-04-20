# [Linux] C Shell (csh) head Uso: Exibir as primeiras linhas de um arquivo

## Overview
O comando `head` é utilizado para exibir as primeiras linhas de um ou mais arquivos. Por padrão, ele mostra as primeiras 10 linhas, mas você pode ajustar essa quantidade conforme necessário.

## Usage
A sintaxe básica do comando `head` é a seguinte:

```
head [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o comando `head`:

- `-n [número]`: Especifica o número de linhas a serem exibidas. Por exemplo, `-n 5` mostrará as primeiras 5 linhas.
- `-c [número]`: Exibe os primeiros bytes do arquivo, em vez de linhas.
- `-q`: Suprime a impressão do cabeçalho dos arquivos quando múltiplos arquivos são fornecidos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `head`:

1. Exibir as primeiras 10 linhas de um arquivo chamado `exemplo.txt`:
   ```csh
   head exemplo.txt
   ```

2. Exibir as primeiras 5 linhas de um arquivo:
   ```csh
   head -n 5 exemplo.txt
   ```

3. Exibir os primeiros 20 bytes de um arquivo:
   ```csh
   head -c 20 exemplo.txt
   ```

4. Exibir as primeiras 10 linhas de múltiplos arquivos:
   ```csh
   head arquivo1.txt arquivo2.txt
   ```

5. Suprimir a impressão do cabeçalho ao exibir múltiplos arquivos:
   ```csh
   head -q arquivo1.txt arquivo2.txt
   ```

## Tips
- Use `head` em combinação com outros comandos, como `grep`, para filtrar resultados. Por exemplo, `grep "erro" log.txt | head -n 5` mostrará os primeiros 5 erros encontrados no arquivo de log.
- Lembre-se de que o `head` é útil para visualizar rapidamente o conteúdo de arquivos grandes sem precisar abri-los completamente.
- Experimente usar `head` com arquivos de texto gerados por outros comandos, como `ls` ou `ps`, para obter uma visão rápida dos resultados.