# [Linux] C Shell (csh) mkdir Uso: Criação de diretórios

## Overview
O comando `mkdir` é utilizado para criar novos diretórios no sistema de arquivos. É uma ferramenta essencial para organizar arquivos e pastas de maneira eficiente.

## Usage
A sintaxe básica do comando `mkdir` é a seguinte:

```
mkdir [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `mkdir`:

- `-p`: Cria diretórios pai conforme necessário. Se os diretórios já existirem, não gera erro.
- `-m`: Define as permissões do diretório criado, utilizando uma máscara de permissão octal.

## Common Examples
Abaixo estão alguns exemplos práticos do uso do comando `mkdir`:

1. Criar um único diretório:
   ```bash
   mkdir meu_diretorio
   ```

2. Criar múltiplos diretórios ao mesmo tempo:
   ```bash
   mkdir dir1 dir2 dir3
   ```

3. Criar um diretório com diretórios pai:
   ```bash
   mkdir -p pasta1/pasta2/pasta3
   ```

4. Criar um diretório com permissões específicas:
   ```bash
   mkdir -m 755 meu_diretorio
   ```

## Tips
- Sempre verifique se o diretório já existe antes de tentar criá-lo para evitar erros.
- Utilize a opção `-p` para criar estruturas de diretórios complexas de uma só vez.
- Considere definir permissões apropriadas ao criar diretórios, especialmente em ambientes compartilhados.