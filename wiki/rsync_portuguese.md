# [Linux] C Shell (csh) rsync Uso: Sincronização de arquivos e diretórios

## Overview
O comando `rsync` é uma ferramenta poderosa utilizada para sincronizar arquivos e diretórios entre diferentes locais, seja localmente ou através de uma rede. Ele é eficiente, pois apenas copia as partes dos arquivos que foram alteradas, economizando tempo e largura de banda.

## Usage
A sintaxe básica do comando `rsync` é a seguinte:

```bash
rsync [opções] [origem] [destino]
```

## Common Options
Aqui estão algumas opções comuns do `rsync`:

- `-a`: Modo de arquivo; preserva permissões, timestamps e links simbólicos.
- `-v`: Modo verboso; exibe informações detalhadas sobre o que está sendo transferido.
- `-z`: Comprime os dados durante a transferência, economizando largura de banda.
- `-r`: Copia diretórios recursivamente.
- `--delete`: Remove arquivos no destino que não estão mais na origem.

## Common Examples

1. Sincronizar um diretório local com outro diretório local:
   ```bash
   rsync -av /caminho/origem/ /caminho/destino/
   ```

2. Sincronizar um diretório local com um servidor remoto:
   ```bash
   rsync -av /caminho/origem/ usuario@servidor:/caminho/destino/
   ```

3. Sincronizar um diretório remoto com um diretório local:
   ```bash
   rsync -av usuario@servidor:/caminho/origem/ /caminho/destino/
   ```

4. Sincronizar e excluir arquivos no destino que não estão na origem:
   ```bash
   rsync -av --delete /caminho/origem/ /caminho/destino/
   ```

## Tips
- Sempre faça um teste com a opção `-n` (dry run) para ver o que será transferido antes de executar o comando de fato.
- Utilize a opção `-z` ao transferir arquivos grandes pela rede para acelerar o processo.
- Considere usar `rsync` com SSH para transferências seguras, como em `rsync -avz -e ssh /caminho/origem/ usuario@servidor:/caminho/destino/`.