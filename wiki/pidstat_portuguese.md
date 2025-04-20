# [Linux] C Shell (csh) pidstat: [monitorar estatísticas de processos]

## Overview
O comando `pidstat` é utilizado para monitorar as estatísticas de utilização de recursos de processos em execução no sistema. Ele fornece informações detalhadas sobre o uso de CPU, memória e outros recursos, permitindo que os usuários identifiquem processos que podem estar consumindo muitos recursos.

## Usage
A sintaxe básica do comando `pidstat` é a seguinte:

```bash
pidstat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `pidstat`:

- `-p <pid>`: Especifica o ID do processo a ser monitorado.
- `-r`: Exibe informações sobre o uso de memória.
- `-u`: Mostra informações sobre o uso de CPU.
- `-h`: Exibe a ajuda com informações sobre as opções disponíveis.
- `-t`: Mostra informações sobre threads.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `pidstat`:

1. Monitorar todos os processos e suas estatísticas de CPU:
   ```bash
   pidstat
   ```

2. Monitorar um processo específico com ID 1234:
   ```bash
   pidstat -p 1234
   ```

3. Exibir estatísticas de uso de memória:
   ```bash
   pidstat -r
   ```

4. Monitorar o uso de CPU a cada 5 segundos:
   ```bash
   pidstat 5
   ```

5. Mostrar informações sobre threads:
   ```bash
   pidstat -t
   ```

## Tips
- Utilize a opção `-r` em conjunto com `-p` para obter uma visão mais completa do uso de recursos de um processo específico.
- Combine `pidstat` com outros comandos como `grep` para filtrar resultados e encontrar processos específicos rapidamente.
- Considere usar `pidstat` em scripts de monitoramento para automatizar a coleta de dados sobre o desempenho do sistema.