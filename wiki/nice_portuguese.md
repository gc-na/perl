# [Linux] C Shell (csh) nice Uso: Ajusta a prioridade de execução de processos

## Overview
O comando `nice` é utilizado para executar um programa com uma prioridade de CPU ajustada. Isso permite que você controle a quantidade de recursos do sistema que um processo pode usar, ajudando a evitar que processos intensivos em CPU afetem o desempenho de outros processos.

## Usage
A sintaxe básica do comando `nice` é a seguinte:

```csh
nice [opções] [comando]
```

## Common Options
Aqui estão algumas opções comuns do comando `nice`:

- `-n [nível]`: Especifica o nível de "nice" a ser aplicado. O nível pode variar de -20 (máxima prioridade) a 19 (mínima prioridade). O padrão é 10.
- `-h`: Exibe uma mensagem de ajuda sobre o uso do comando.

## Common Examples

1. Executar um comando com prioridade padrão:
   ```csh
   nice comando
   ```

2. Executar um comando com prioridade aumentada (menos "nice"):
   ```csh
   nice -n 5 comando
   ```

3. Executar um comando com prioridade reduzida (mais "nice"):
   ```csh
   nice -n 15 comando
   ```

4. Verificar a prioridade de um processo em execução:
   ```csh
   ps -o pid,nice,cmd
   ```

## Tips
- Use `nice` para processos que não são críticos, permitindo que outros processos mais importantes tenham mais recursos.
- Lembre-se de que apenas usuários com permissões adequadas podem diminuir a prioridade de um processo (usar valores negativos).
- Combine `nice` com outros comandos, como `nohup`, para executar processos em segundo plano sem interrupções.