# [Linux] C Shell (csh) stat Uso: Exibir informações sobre arquivos

## Overview
O comando `stat` é utilizado para exibir informações detalhadas sobre arquivos e diretórios no sistema. Ele fornece dados como tamanho, permissões, data de modificação e muito mais.

## Usage
A sintaxe básica do comando `stat` é a seguinte:

```csh
stat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `stat`:

- `-c` : Formato de saída personalizado.
- `-f` : Exibe informações de arquivos em um formato específico.
- `--format` : Permite especificar um formato de saída.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `stat`:

1. Exibir informações básicas sobre um arquivo:
   ```csh
   stat arquivo.txt
   ```

2. Usar um formato personalizado para exibir apenas o tamanho do arquivo:
   ```csh
   stat -c %s arquivo.txt
   ```

3. Exibir informações de um diretório:
   ```csh
   stat /caminho/para/diretorio
   ```

4. Exibir informações de múltiplos arquivos:
   ```csh
   stat arquivo1.txt arquivo2.txt
   ```

## Tips
- Utilize a opção `-c` para personalizar a saída e obter apenas as informações que você precisa.
- Combine o comando `stat` com outros comandos, como `grep`, para filtrar informações específicas.
- Lembre-se de que o `stat` pode ser usado em diretórios, não apenas em arquivos, para obter informações sobre a estrutura do sistema de arquivos.