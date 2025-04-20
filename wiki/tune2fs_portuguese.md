# [Linux] C Shell (csh) tune2fs Uso: Ajustar parâmetros do sistema de arquivos ext2/ext3/ext4

## Overview
O comando `tune2fs` é utilizado para ajustar parâmetros de sistemas de arquivos ext2, ext3 e ext4 no Linux. Ele permite modificar características do sistema de arquivos, como opções de montagem, limites de inodes e muito mais, sem a necessidade de desmontar o sistema de arquivos.

## Usage
A sintaxe básica do comando `tune2fs` é a seguinte:

```bash
tune2fs [opções] [argumentos]
```

## Common Options
- `-c <n>`: Define o número máximo de montagens antes de uma verificação forçada.
- `-i <intervalo>`: Define o intervalo de tempo entre verificações automáticas.
- `-m <porcentagem>`: Define a porcentagem de espaço reservado para o superusuário.
- `-O <opções>`: Ativa as opções especificadas para o sistema de arquivos.
- `-L <rótulo>`: Define um novo rótulo para o sistema de arquivos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `tune2fs`:

1. **Definir o número máximo de montagens antes da verificação:**
   ```bash
   tune2fs -c 20 /dev/sda1
   ```

2. **Definir o intervalo de tempo entre verificações automáticas para 30 dias:**
   ```bash
   tune2fs -i 30d /dev/sda1
   ```

3. **Reservar 5% do espaço do sistema de arquivos para o superusuário:**
   ```bash
   tune2fs -m 5 /dev/sda1
   ```

4. **Ativar a opção de verificação de integridade:**
   ```bash
   tune2fs -O journal_data /dev/sda1
   ```

5. **Definir um novo rótulo para o sistema de arquivos:**
   ```bash
   tune2fs -L "MeuSistema" /dev/sda1
   ```

## Tips
- Sempre faça um backup dos dados importantes antes de modificar as configurações do sistema de arquivos.
- Utilize o comando `tune2fs -l /dev/sda1` para listar as configurações atuais do sistema de arquivos antes de fazer alterações.
- Cuidado ao usar opções que podem afetar a integridade do sistema de arquivos, como a ativação ou desativação de recursos.