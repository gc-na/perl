# [Linux] C Shell (csh) mkfifo: criar arquivos FIFO

## Overview
O comando `mkfifo` é utilizado para criar arquivos FIFO (First In, First Out) no sistema. Esses arquivos permitem a comunicação entre processos, funcionando como canais de dados onde um processo pode escrever e outro pode ler.

## Usage
A sintaxe básica do comando `mkfifo` é a seguinte:

```csh
mkfifo [opções] [argumentos]
```

## Common Options
- `-m, --mode`: Define as permissões do arquivo FIFO a ser criado.
- `-Z, --context`: Define o contexto de segurança SELinux para o arquivo.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `mkfifo`:

1. **Criar um arquivo FIFO simples:**

   ```csh
   mkfifo meu_fifo
   ```

2. **Criar um arquivo FIFO com permissões específicas:**

   ```csh
   mkfifo -m 644 meu_fifo
   ```

3. **Criar múltiplos arquivos FIFO de uma só vez:**

   ```csh
   mkfifo fifo1 fifo2 fifo3
   ```

4. **Criar um arquivo FIFO com contexto de segurança:**

   ```csh
   mkfifo -Z meu_fifo
   ```

## Tips
- Sempre verifique as permissões do arquivo FIFO após a criação, especialmente se vários usuários ou processos irão acessá-lo.
- Utilize o comando `ls -l` para visualizar as permissões e garantir que estão configuradas corretamente.
- Lembre-se de que os arquivos FIFO são temporários e devem ser removidos quando não forem mais necessários, utilizando o comando `rm`.