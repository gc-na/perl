# [Linux] C Shell (csh) cmp Uso: Comparar arquivos byte a byte

## Overview
O comando `cmp` é utilizado para comparar dois arquivos byte a byte. Ele é útil para verificar se dois arquivos são idênticos ou para identificar a primeira diferença entre eles.

## Usage
A sintaxe básica do comando `cmp` é a seguinte:

```csh
cmp [opções] [arquivos]
```

## Common Options
Aqui estão algumas opções comuns do comando `cmp`:

- `-l`: Exibe a lista de diferenças em formato octal.
- `-s`: Silencia a saída, apenas retorna o status de saída.
- `-i <n>`: Ignora os primeiros `n` bytes de cada arquivo.
- `-n <n>`: Compara apenas os primeiros `n` bytes dos arquivos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `cmp`:

1. Comparar dois arquivos e exibir a primeira diferença:
   ```csh
   cmp arquivo1.txt arquivo2.txt
   ```

2. Comparar dois arquivos e listar as diferenças em formato octal:
   ```csh
   cmp -l arquivo1.txt arquivo2.txt
   ```

3. Comparar dois arquivos sem exibir a saída, apenas o status:
   ```csh
   cmp -s arquivo1.txt arquivo2.txt
   ```

4. Comparar apenas os primeiros 100 bytes de dois arquivos:
   ```csh
   cmp -n 100 arquivo1.txt arquivo2.txt
   ```

## Tips
- Use a opção `-s` quando você apenas precisa saber se os arquivos são diferentes, sem se preocupar com as diferenças específicas.
- Se você estiver comparando arquivos grandes e quiser economizar tempo, considere usar a opção `-n` para limitar a comparação a uma parte dos arquivos.
- Lembre-se de que o `cmp` é sensível a maiúsculas e minúsculas, então `arquivo.txt` e `Arquivo.txt` serão considerados diferentes.