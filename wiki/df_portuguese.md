# [Linux] C Shell (csh) df Uso: Exibir informações sobre o uso do sistema de arquivos

## Overview
O comando `df` é utilizado para exibir informações sobre o espaço em disco disponível e utilizado em sistemas de arquivos montados. Ele fornece uma visão geral do uso do espaço em disco, permitindo que os usuários monitorem a capacidade de armazenamento de suas partições.

## Usage
A sintaxe básica do comando `df` é a seguinte:

```csh
df [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `df`:

- `-h`: Exibe os tamanhos em um formato legível por humanos (por exemplo, KB, MB, GB).
- `-T`: Mostra o tipo de sistema de arquivos.
- `-i`: Exibe informações sobre inodes em vez de espaço em disco.
- `-a`: Inclui sistemas de arquivos que têm 0 blocos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `df`:

1. Exibir informações básicas sobre o uso do disco:
   ```csh
   df
   ```

2. Exibir informações em um formato legível por humanos:
   ```csh
   df -h
   ```

3. Mostrar o tipo de sistema de arquivos:
   ```csh
   df -T
   ```

4. Exibir informações sobre inodes:
   ```csh
   df -i
   ```

5. Incluir sistemas de arquivos com 0 blocos:
   ```csh
   df -a
   ```

## Tips
- Utilize a opção `-h` para facilitar a leitura dos resultados, especialmente em sistemas com grandes quantidades de dados.
- Combine opções para obter informações mais detalhadas, como `df -hT` para ver tamanhos e tipos de sistema de arquivos.
- Verifique regularmente o uso do disco para evitar problemas de espaço, especialmente em servidores e sistemas críticos.