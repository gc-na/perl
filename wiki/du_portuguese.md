# [Linux] C Shell (csh) du <Uso equivalente em português>: Exibir o uso de disco

## Overview
O comando `du` (Disk Usage) é utilizado para estimar e relatar o espaço em disco utilizado por arquivos e diretórios. Ele é uma ferramenta útil para monitorar o uso de espaço em sistemas de arquivos.

## Usage
A sintaxe básica do comando `du` é a seguinte:

```csh
du [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `du`:

- `-h`: Exibe os tamanhos em um formato legível por humanos (por exemplo, KB, MB).
- `-s`: Mostra apenas o total para cada argumento, sem listar os subdiretórios.
- `-a`: Inclui arquivos além de diretórios na listagem.
- `-c`: Fornece um total cumulativo no final da saída.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `du`:

1. Exibir o uso de disco de um diretório específico em um formato legível:
   ```csh
   du -h /caminho/do/diretorio
   ```

2. Mostrar apenas o total de espaço usado por um diretório:
   ```csh
   du -sh /caminho/do/diretorio
   ```

3. Listar o uso de disco de todos os arquivos e diretórios no diretório atual:
   ```csh
   du -ah .
   ```

4. Exibir o uso de disco de um diretório e incluir um total cumulativo:
   ```csh
   du -ch /caminho/do/diretorio
   ```

## Tips
- Utilize a opção `-h` para facilitar a leitura dos tamanhos, especialmente em diretórios grandes.
- Combine `du` com o comando `sort` para ordenar a saída por tamanho:
  ```csh
  du -h | sort -h
  ```
- Use `du -s` para obter um resumo rápido do uso de espaço sem detalhes desnecessários.