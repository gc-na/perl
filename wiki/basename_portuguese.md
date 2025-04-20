# [Linux] C Shell (csh) basename Uso: Extrair o nome do arquivo sem o caminho

## Overview
O comando `basename` é utilizado para extrair o nome de um arquivo a partir de um caminho completo, removendo qualquer diretório que o preceda. Isso é útil quando você precisa trabalhar apenas com o nome do arquivo em scripts ou comandos.

## Usage
A sintaxe básica do comando `basename` é a seguinte:

```csh
basename [opções] [argumentos]
```

## Common Options
- `-a`: Aceita múltiplos argumentos e retorna o nome base de cada um.
- `-s`: Remove uma extensão específica do nome do arquivo.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `basename`:

1. **Extrair o nome de um arquivo:**
   ```csh
   basename /caminho/para/o/arquivo.txt
   ```
   Saída:
   ```
   arquivo.txt
   ```

2. **Remover a extensão de um arquivo:**
   ```csh
   basename /caminho/para/o/arquivo.txt .txt
   ```
   Saída:
   ```
   arquivo
   ```

3. **Usar com múltiplos arquivos:**
   ```csh
   basename -a /caminho/para/arquivo1.txt /caminho/para/arquivo2.txt
   ```
   Saída:
   ```
   arquivo1.txt
   arquivo2.txt
   ```

## Tips
- Utilize o `basename` em scripts para facilitar a manipulação de nomes de arquivos.
- Combine `basename` com outros comandos, como `find`, para processar arquivos de forma mais eficiente.
- Lembre-se de que o `basename` não altera os arquivos, apenas fornece a saída do nome base.