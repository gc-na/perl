# [Linux] C Shell (csh) fmt Uso: Formatação de texto

## Overview
O comando `fmt` é utilizado para formatar texto em linhas de comprimento fixo. Ele é especialmente útil para ajustar a largura de parágrafos em arquivos de texto, tornando-os mais legíveis.

## Usage
A sintaxe básica do comando `fmt` é a seguinte:

```csh
fmt [options] [arguments]
```

## Common Options
- `-w <n>`: Define a largura máxima das linhas formatadas. O padrão é 75 caracteres.
- `-s`: Suprime a quebra de linhas em branco, mantendo a formatação do texto.
- `-u`: Remove espaços em branco extras entre palavras.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `fmt`:

1. **Formatar um arquivo de texto com largura padrão:**
   ```csh
   fmt texto.txt
   ```

2. **Formatar um arquivo de texto com largura de 50 caracteres:**
   ```csh
   fmt -w 50 texto.txt
   ```

3. **Formatar texto a partir da entrada padrão:**
   ```csh
   echo "Este é um exemplo de texto que será formatado." | fmt
   ```

4. **Suprimir quebras de linha em branco:**
   ```csh
   fmt -s texto_com_quebras.txt
   ```

5. **Remover espaços em branco extras:**
   ```csh
   fmt -u texto_com_espacos.txt
   ```

## Tips
- Sempre verifique a largura das linhas formatadas para garantir que se encaixem no layout desejado.
- Use a opção `-w` para personalizar a largura de acordo com as necessidades do seu documento.
- Combine o `fmt` com outros comandos, como `cat`, para formatar e visualizar arquivos de texto de forma eficiente.