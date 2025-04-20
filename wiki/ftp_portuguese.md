# [Linux] C Shell (csh) ftp Uso: Transferir arquivos pela rede

## Overview
O comando `ftp` (File Transfer Protocol) é utilizado para transferir arquivos entre um computador local e um servidor remoto através da rede. Ele permite que os usuários se conectem a servidores FTP, façam upload e download de arquivos, e gerenciem diretórios.

## Usage
A sintaxe básica do comando `ftp` é a seguinte:

```csh
ftp [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `ftp`:

- `-v`: Modo verbose. Exibe informações detalhadas sobre a transferência.
- `-n`: Não tenta automaticamente se conectar ao servidor FTP ao iniciar.
- `-g`: Desativa a expansão de caracteres curinga para nomes de arquivos.
- `-i`: Desativa o modo interativo, permitindo transferências de arquivos sem confirmação.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `ftp`:

1. Conectar-se a um servidor FTP:
   ```csh
   ftp ftp.exemplo.com
   ```

2. Fazer upload de um arquivo para o servidor:
   ```csh
   put arquivo.txt
   ```

3. Fazer download de um arquivo do servidor:
   ```csh
   get arquivo.txt
   ```

4. Listar arquivos no diretório atual do servidor:
   ```csh
   ls
   ```

5. Mudar para um diretório específico no servidor:
   ```csh
   cd /diretorio/exemplo
   ```

## Tips
- Sempre use o modo `-v` para obter informações detalhadas sobre as transferências, especialmente ao solucionar problemas.
- Lembre-se de usar `bye` ou `quit` para sair do cliente FTP corretamente.
- Verifique as permissões de arquivo e diretório no servidor para evitar erros durante as transferências.