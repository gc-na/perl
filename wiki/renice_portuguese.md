# [Linux] C Shell (csh) renice: Ajustar a prioridade de processos em execução

## Overview
O comando `renice` é utilizado para alterar a prioridade de execução de processos já em funcionamento no sistema. A prioridade é um valor que determina a quantidade de tempo de CPU que um processo pode utilizar. Um valor de prioridade mais baixo indica uma prioridade mais alta.

## Usage
A sintaxe básica do comando `renice` é a seguinte:

```csh
renice [opções] [argumentos]
```

## Common Options
- `-n`: Especifica o novo valor de prioridade. Pode ser um número positivo ou negativo.
- `-p`: Permite especificar o ID do processo (PID) que terá sua prioridade alterada.
- `-g`: Altera a prioridade de todos os processos pertencentes a um grupo de processos específico.
- `-u`: Altera a prioridade de todos os processos pertencentes a um usuário específico.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `renice`:

1. Alterar a prioridade de um processo específico pelo PID:
   ```csh
   renice -n 10 -p 1234
   ```

2. Aumentar a prioridade de um processo (diminui o número):
   ```csh
   renice -n -5 -p 5678
   ```

3. Alterar a prioridade de todos os processos de um usuário:
   ```csh
   renice -n 15 -u usuario
   ```

4. Alterar a prioridade de todos os processos em um grupo específico:
   ```csh
   renice -n 5 -g grupo
   ```

## Tips
- Sempre verifique a prioridade atual dos processos antes de usar o `renice` para evitar mudanças indesejadas.
- Use valores negativos com cautela, pois eles aumentam a prioridade e podem afetar o desempenho do sistema se aplicados a muitos processos.
- Para visualizar a lista de processos e suas prioridades, você pode usar o comando `ps` em conjunto com `renice`.