# [Linux] C Shell (csh) umask uso: Define permissões padrão de arquivos

## Overview
O comando `umask` no C Shell (csh) é utilizado para definir as permissões padrão para novos arquivos e diretórios criados no sistema. Ele especifica quais permissões devem ser removidas das permissões padrão, permitindo um controle mais rigoroso sobre a segurança dos arquivos.

## Usage
A sintaxe básica do comando `umask` é a seguinte:

```csh
umask [opções] [argumentos]
```

## Common Options
- `-S`: Exibe a máscara de permissão em formato simbólico.
- `-p`: Exibe a máscara de permissão atual sem alterá-la.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `umask`:

1. **Verificar a máscara atual:**
   ```csh
   umask
   ```

2. **Definir uma nova máscara:**
   Para definir a máscara para que novos arquivos tenham permissões de leitura e escrita para o proprietário, e nenhuma permissão para o grupo e outros:
   ```csh
   umask 077
   ```

3. **Exibir a máscara em formato simbólico:**
   ```csh
   umask -S
   ```

4. **Restaurar a máscara padrão:**
   Para restaurar a máscara padrão do sistema:
   ```csh
   umask 022
   ```

## Tips
- Sempre verifique a máscara atual antes de criar novos arquivos, especialmente em ambientes compartilhados, para evitar permissões indesejadas.
- Use a opção `-S` para entender melhor as permissões que estão sendo aplicadas.
- Considere definir a máscara em arquivos de inicialização, como `.cshrc`, para garantir que suas preferências sejam aplicadas sempre que você iniciar uma nova sessão do shell.