# [Linux] C Shell (csh) sha256sum uso: Calcula e verifica somas de verificação SHA-256

## Overview
O comando `sha256sum` é utilizado para calcular e verificar somas de verificação SHA-256 de arquivos. Essa função é essencial para garantir a integridade dos dados, permitindo que os usuários verifiquem se um arquivo foi alterado ou corrompido.

## Usage
A sintaxe básica do comando `sha256sum` é a seguinte:

```
sha256sum [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `sha256sum`:

- `-b`: Calcula a soma de verificação em modo binário.
- `-c`: Verifica as somas de verificação a partir de um arquivo.
- `-h`: Exibe a ajuda e as opções disponíveis.
- `--quiet`: Não exibe mensagens de erro.

## Common Examples

### Calcular a soma de verificação de um arquivo
Para calcular a soma de verificação SHA-256 de um arquivo chamado `exemplo.txt`, você pode usar o seguinte comando:

```bash
sha256sum exemplo.txt
```

### Verificar a soma de verificação a partir de um arquivo
Se você tiver um arquivo chamado `checksums.txt` que contém somas de verificação e nomes de arquivos, você pode verificar os arquivos com o seguinte comando:

```bash
sha256sum -c checksums.txt
```

### Calcular a soma de verificação de vários arquivos
Para calcular as somas de verificação de vários arquivos ao mesmo tempo, você pode listar os arquivos:

```bash
sha256sum arquivo1.txt arquivo2.txt arquivo3.txt
```

### Usar modo binário
Para calcular a soma de verificação em modo binário, utilize a opção `-b`:

```bash
sha256sum -b exemplo.bin
```

## Tips
- Sempre verifique as somas de verificação após o download de arquivos importantes para garantir que não houve corrupção.
- Mantenha um registro das somas de verificação em um arquivo separado para facilitar a verificação futura.
- Use a opção `--quiet` se você deseja suprimir mensagens de erro durante a verificação de arquivos.