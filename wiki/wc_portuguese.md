# [Linux] C Shell (csh) wc Uso: Conta linhas, palavras e bytes em arquivos

## Overview
O comando `wc` (word count) é utilizado para contar o número de linhas, palavras e bytes em um ou mais arquivos. Ele é uma ferramenta útil para obter informações rápidas sobre o conteúdo de arquivos de texto.

## Usage
A sintaxe básica do comando `wc` é a seguinte:

```csh
wc [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `wc`:

- `-l`: Conta apenas o número de linhas.
- `-w`: Conta apenas o número de palavras.
- `-c`: Conta apenas o número de bytes.
- `-m`: Conta o número de caracteres (incluindo caracteres multibyte).
- `-L`: Exibe o comprimento da linha mais longa.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `wc`:

1. Contar o número total de linhas, palavras e bytes em um arquivo:

   ```csh
   wc arquivo.txt
   ```

2. Contar apenas o número de linhas em um arquivo:

   ```csh
   wc -l arquivo.txt
   ```

3. Contar apenas o número de palavras em um arquivo:

   ```csh
   wc -w arquivo.txt
   ```

4. Contar apenas o número de bytes em um arquivo:

   ```csh
   wc -c arquivo.txt
   ```

5. Contar o número de caracteres em um arquivo:

   ```csh
   wc -m arquivo.txt
   ```

6. Contar o comprimento da linha mais longa em um arquivo:

   ```csh
   wc -L arquivo.txt
   ```

## Tips
- Combine opções para obter múltiplas contagens de uma só vez. Por exemplo, `wc -l -w arquivo.txt` exibirá o número de linhas e palavras.
- Use o comando em conjunto com outros comandos, como `cat` ou `grep`, para contar linhas ou palavras em saídas filtradas.
- Lembre-se de que o `wc` pode processar múltiplos arquivos ao mesmo tempo, basta listar os arquivos após o comando.