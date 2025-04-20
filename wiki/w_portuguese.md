# [Linux] C Shell (csh) w: Exibir usuários conectados e suas atividades

## Overview
O comando `w` é utilizado para exibir informações sobre os usuários que estão atualmente conectados ao sistema, bem como suas atividades. Ele fornece detalhes como o tempo de atividade do sistema, o tempo que cada usuário está logado e o que cada um está fazendo.

## Usage
A sintaxe básica do comando `w` é a seguinte:

```
w [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `w`:

- `-h`: Remove o cabeçalho da saída.
- `-s`: Exibe uma saída mais compacta, omitindo algumas informações.
- `-f`: Exibe informações adicionais sobre o terminal do usuário.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `w`:

1. **Exibir todos os usuários conectados:**
   ```csh
   w
   ```

2. **Exibir usuários conectados sem cabeçalho:**
   ```csh
   w -h
   ```

3. **Exibir uma saída compacta:**
   ```csh
   w -s
   ```

4. **Exibir informações detalhadas sobre os usuários:**
   ```csh
   w -f
   ```

## Tips
- Utilize o comando `w` regularmente para monitorar a atividade dos usuários no sistema.
- Combine o `w` com outros comandos, como `grep`, para filtrar informações específicas.
- Lembre-se de que a saída do `w` pode variar dependendo das permissões do usuário que executa o comando.