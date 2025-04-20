# [Linux] C Shell (csh) vmstat Uso: Monitorar estatísticas de sistema

## Overview
O comando `vmstat` é utilizado para relatar informações sobre a memória virtual, processos, entradas e saídas, e o uso da CPU em sistemas operacionais Unix e Linux. Ele fornece uma visão geral do desempenho do sistema, ajudando na identificação de problemas de desempenho.

## Usage
A sintaxe básica do comando `vmstat` é a seguinte:

```csh
vmstat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `vmstat`:

- `-a`: Exibe informações sobre a memória ativa e inativa.
- `-m`: Mostra estatísticas sobre a memória.
- `-s`: Exibe um resumo das estatísticas do sistema.
- `interval`: Define um intervalo em segundos para a atualização das informações.
- `count`: Especifica o número de vezes que as informações devem ser exibidas.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `vmstat`:

1. **Exibir estatísticas do sistema a cada 2 segundos:**

   ```csh
   vmstat 2
   ```

2. **Mostrar informações detalhadas sobre a memória:**

   ```csh
   vmstat -m
   ```

3. **Exibir um resumo das estatísticas do sistema:**

   ```csh
   vmstat -s
   ```

4. **Monitorar o sistema a cada 5 segundos por 10 vezes:**

   ```csh
   vmstat 5 10
   ```

## Tips
- Utilize `vmstat` em conjunto com outros comandos como `top` ou `htop` para uma análise mais abrangente do desempenho do sistema.
- Monitore o uso da memória e da CPU durante períodos de alta carga para identificar gargalos.
- Salve a saída do `vmstat` em um arquivo para análise posterior usando redirecionamento, como em `vmstat 2 > vmstat_output.txt`.