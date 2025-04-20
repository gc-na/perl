# [Linux] C Shell (csh) parted Uso: Gerenciar partições de disco

## Overview
O comando `parted` é uma ferramenta utilizada para gerenciar partições de disco em sistemas operacionais baseados em Linux. Ele permite criar, redimensionar, mover e excluir partições, facilitando a organização do espaço em disco.

## Usage
A sintaxe básica do comando `parted` é a seguinte:

```bash
parted [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `parted`:

- `-l` ou `--list`: Lista todas as partições disponíveis.
- `mkpart`: Cria uma nova partição.
- `resizepart`: Redimensiona uma partição existente.
- `rm`: Remove uma partição.
- `print`: Exibe a tabela de partições atual.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `parted`:

1. **Listar todas as partições:**
   ```bash
   parted -l
   ```

2. **Criar uma nova partição:**
   ```bash
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Redimensionar uma partição existente:**
   ```bash
   parted /dev/sda resizepart 1 200MiB
   ```

4. **Remover uma partição:**
   ```bash
   parted /dev/sda rm 1
   ```

5. **Exibir a tabela de partições:**
   ```bash
   parted /dev/sda print
   ```

## Tips
- Sempre faça backup dos dados importantes antes de modificar partições para evitar perda de dados.
- Utilize o comando `print` para verificar a tabela de partições antes de realizar alterações.
- Tenha cuidado ao especificar o dispositivo correto (`/dev/sda`, `/dev/sdb`, etc.) para evitar modificar a partição errada.