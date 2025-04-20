# [Linux] C Shell (csh) dstat Uso: Monitora recursos do sistema em tempo real

## Overview
O comando `dstat` é uma ferramenta poderosa que permite monitorar recursos do sistema em tempo real. Ele combina as funcionalidades de várias ferramentas de monitoramento, como `vmstat`, `iostat`, `netstat`, e `ifstat`, fornecendo uma visão abrangente do desempenho do sistema.

## Usage
A sintaxe básica do comando `dstat` é a seguinte:

```
dstat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `dstat`:

- `-c`: Mostra o uso da CPU.
- `-d`: Exibe estatísticas de disco.
- `-n`: Mostra estatísticas de rede.
- `-m`: Exibe informações sobre a memória.
- `--time`: Adiciona um timestamp a cada linha de saída.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `dstat`:

1. **Monitorar uso da CPU e da memória:**
   ```bash
   dstat -c -m
   ```

2. **Ver estatísticas de disco e rede:**
   ```bash
   dstat -d -n
   ```

3. **Monitorar todos os recursos com timestamps:**
   ```bash
   dstat --time -cdmn
   ```

4. **Exibir informações detalhadas de CPU, disco e rede:**
   ```bash
   dstat -t -c -d -n --full
   ```

## Tips
- Utilize o `dstat` em scripts de monitoramento para coletar dados de desempenho ao longo do tempo.
- Combine várias opções para obter uma visão mais completa do sistema.
- Considere redirecionar a saída do `dstat` para um arquivo para análise posterior, usando `dstat > output.txt`.