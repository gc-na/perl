# [Linux] C Shell (csh) cp Uso: Copiar arquivos e diretórios

## Overview
O comando `cp` é utilizado para copiar arquivos e diretórios no sistema operacional. Ele permite que você crie uma cópia de um arquivo ou diretório em um novo local, mantendo o arquivo original intacto.

## Usage
A sintaxe básica do comando `cp` é a seguinte:

```csh
cp [opções] [origem] [destino]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `cp`:

- `-r`: Copia diretórios de forma recursiva.
- `-i`: Pergunta antes de sobrescrever arquivos existentes.
- `-u`: Copia apenas arquivos que são mais novos que os arquivos de destino ou que não existem no destino.
- `-v`: Exibe os arquivos sendo copiados, útil para depuração.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `cp`:

1. **Copiar um arquivo para outro local:**
   ```csh
   cp arquivo.txt /caminho/para/destino/
   ```

2. **Copiar um diretório e seu conteúdo:**
   ```csh
   cp -r /caminho/para/diretorio/ /caminho/para/destino/
   ```

3. **Copiar um arquivo e perguntar antes de sobrescrever:**
   ```csh
   cp -i arquivo.txt /caminho/para/destino/
   ```

4. **Copiar apenas arquivos mais novos:**
   ```csh
   cp -u arquivo.txt /caminho/para/destino/
   ```

5. **Copiar um arquivo e mostrar o progresso:**
   ```csh
   cp -v arquivo.txt /caminho/para/destino/
   ```

## Tips
- Sempre verifique o caminho de destino para evitar sobrescrever arquivos importantes.
- Use a opção `-i` se você não tiver certeza se deseja sobrescrever arquivos existentes.
- Para copiar arquivos de forma segura, considere usar a opção `-u` para evitar cópias desnecessárias.