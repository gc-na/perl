# [Linux] C Shell (csh) sftp Uso: Transferência segura de arquivos

## Overview
O comando `sftp` (SSH File Transfer Protocol) é utilizado para transferir arquivos de forma segura entre um cliente e um servidor através de uma conexão SSH. Ele permite a transferência de arquivos de maneira interativa ou não interativa, garantindo a segurança dos dados durante o processo.

## Usage
A sintaxe básica do comando `sftp` é a seguinte:

```csh
sftp [opções] [usuário@]host
```

## Common Options
Aqui estão algumas opções comuns do comando `sftp`:

- `-b arquivo`: Executa um lote de comandos a partir do arquivo especificado.
- `-C`: Ativa a compressão durante a transferência de arquivos.
- `-o opção`: Passa uma opção específica para o cliente SSH.
- `-P porta`: Especifica a porta a ser usada para a conexão (por padrão, a porta 22 é utilizada).

## Common Examples
Aqui estão alguns exemplos práticos de uso do `sftp`:

1. Conectar a um servidor SFTP:
   ```csh
   sftp usuario@exemplo.com
   ```

2. Transferir um arquivo do cliente para o servidor:
   ```csh
   put arquivo.txt
   ```

3. Transferir um arquivo do servidor para o cliente:
   ```csh
   get arquivo.txt
   ```

4. Listar arquivos no diretório remoto:
   ```csh
   ls
   ```

5. Executar um lote de comandos a partir de um arquivo:
   ```csh
   sftp -b comandos.txt usuario@exemplo.com
   ```

## Tips
- Sempre use `sftp` em vez de `ftp` para garantir a segurança das suas transferências de arquivos.
- Verifique as permissões dos arquivos e diretórios antes de transferir para evitar erros.
- Utilize a opção `-C` para acelerar a transferência de arquivos grandes, especialmente em conexões lentas.