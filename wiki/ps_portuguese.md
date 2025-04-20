# [Linux] C Shell (csh) ps Uso: Exibir processos em execução

## Overview
O comando `ps` é utilizado para exibir informações sobre os processos em execução no sistema. Ele fornece uma visão instantânea dos processos, permitindo que os usuários vejam quais programas estão ativos e suas respectivas informações, como PID (identificador do processo), uso de CPU e memória.

## Usage
A sintaxe básica do comando `ps` é a seguinte:

```
ps [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `ps`:

- `-e`: Exibe todos os processos em execução.
- `-f`: Mostra a saída em um formato completo, incluindo informações adicionais sobre os processos.
- `-u [usuário]`: Exibe os processos pertencentes a um usuário específico.
- `-aux`: Exibe todos os processos em execução, incluindo aqueles que não têm um terminal associado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `ps`:

1. **Exibir todos os processos em execução:**
   ```bash
   ps -e
   ```

2. **Exibir processos em formato completo:**
   ```bash
   ps -f
   ```

3. **Exibir processos de um usuário específico:**
   ```bash
   ps -u nome_do_usuario
   ```

4. **Exibir todos os processos, incluindo os que não têm terminal:**
   ```bash
   ps aux
   ```

## Tips
- Utilize `ps aux | grep [nome_do_processo]` para filtrar e encontrar um processo específico.
- Combine `ps` com outros comandos, como `sort` ou `head`, para organizar melhor a saída.
- Lembre-se de que o `ps` captura um instantâneo dos processos em um dado momento; para monitoramento contínuo, considere usar o comando `top`.