# [Linux] C Shell (csh) pr: Formatar e paginar arquivos de texto

## Overview
O comando `pr` é utilizado para formatar e paginar arquivos de texto, facilitando a leitura e a impressão. Ele organiza o conteúdo em colunas e adiciona cabeçalhos e numeração de páginas, tornando os documentos mais apresentáveis.

## Usage
A sintaxe básica do comando `pr` é a seguinte:

```csh
pr [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `pr`:

- `-2`: Formata a saída em duas colunas.
- `-h "Cabeçalho"`: Adiciona um cabeçalho personalizado ao documento.
- `-n`: Não numera as páginas.
- `-s`: Especifica um caractere de separação entre colunas.
- `-t`: Remove a formatação de tabulação.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `pr`:

1. **Formatar um arquivo de texto em duas colunas:**
   ```csh
   pr -2 arquivo.txt
   ```

2. **Adicionar um cabeçalho ao arquivo:**
   ```csh
   pr -h "Relatório Mensal" arquivo.txt
   ```

3. **Remover a numeração de páginas:**
   ```csh
   pr -n arquivo.txt
   ```

4. **Formatar um arquivo com um caractere de separação:**
   ```csh
   pr -s '|' arquivo.txt
   ```

5. **Formatar um arquivo e enviar para impressão:**
   ```csh
   pr arquivo.txt | lpr
   ```

## Tips
- Use a opção `-h` para adicionar um cabeçalho que descreva o conteúdo do arquivo, tornando-o mais informativo.
- Experimente diferentes opções de colunas para ver qual formatação se adapta melhor às suas necessidades.
- Lembre-se de que a saída formatada pode ser redirecionada para um arquivo ou impressora, facilitando a distribuição do conteúdo.