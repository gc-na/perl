# [Linux] C Shell (csh) lsblk Uso: exibir informações sobre dispositivos de bloco

## Overview
O comando `lsblk` é utilizado para listar informações sobre todos os dispositivos de bloco disponíveis no sistema, como discos rígidos, partições e dispositivos de armazenamento removíveis. Ele fornece uma visão clara da estrutura de armazenamento, facilitando a identificação de dispositivos e suas respectivas montagens.

## Usage
A sintaxe básica do comando `lsblk` é a seguinte:

```csh
lsblk [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `lsblk`:

- `-a` ou `--all`: Exibe todos os dispositivos, incluindo aqueles que não estão montados.
- `-f` ou `--fs`: Mostra informações sobre o sistema de arquivos dos dispositivos.
- `-l` ou `--list`: Exibe a saída em formato de lista, em vez de árvore.
- `-o` ou `--output`: Permite especificar quais colunas exibir na saída.
- `-n` ou `--noheadings`: Remove os cabeçalhos da saída.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `lsblk`:

1. **Listar todos os dispositivos de bloco:**
   ```csh
   lsblk
   ```

2. **Listar todos os dispositivos, incluindo não montados:**
   ```csh
   lsblk -a
   ```

3. **Mostrar informações do sistema de arquivos:**
   ```csh
   lsblk -f
   ```

4. **Exibir a saída em formato de lista:**
   ```csh
   lsblk -l
   ```

5. **Especificar colunas a serem exibidas:**
   ```csh
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

6. **Remover cabeçalhos da saída:**
   ```csh
   lsblk -n
   ```

## Tips
- Utilize a opção `-f` para verificar rapidamente o tipo de sistema de arquivos e o UUID dos dispositivos.
- Combine opções para personalizar a saída de acordo com suas necessidades, como `lsblk -a -f`.
- Para uma visualização mais clara, use a opção `-o` para selecionar apenas as colunas relevantes que você precisa.