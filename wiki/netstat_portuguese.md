# [Linux] C Shell (csh) netstat Uso: Exibir conexões de rede e estatísticas

## Overview
O comando `netstat` é uma ferramenta poderosa utilizada para exibir informações sobre conexões de rede, tabelas de roteamento, estatísticas de interface e muito mais. Ele é útil para diagnosticar problemas de rede e monitorar a atividade da rede em um sistema.

## Usage
A sintaxe básica do comando `netstat` é a seguinte:

```csh
netstat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `netstat`:

- `-a`: Exibe todas as conexões e escuta portas.
- `-t`: Mostra apenas conexões TCP.
- `-u`: Mostra apenas conexões UDP.
- `-n`: Exibe endereços e números de porta em formato numérico, em vez de tentar resolver nomes.
- `-r`: Exibe a tabela de roteamento.
- `-i`: Mostra as estatísticas de interface de rede.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `netstat`:

1. Exibir todas as conexões e portas em escuta:
   ```csh
   netstat -a
   ```

2. Mostrar apenas conexões TCP:
   ```csh
   netstat -t
   ```

3. Exibir conexões UDP:
   ```csh
   netstat -u
   ```

4. Mostrar a tabela de roteamento:
   ```csh
   netstat -r
   ```

5. Exibir estatísticas de interface de rede:
   ```csh
   netstat -i
   ```

6. Exibir endereços e portas em formato numérico:
   ```csh
   netstat -n
   ```

## Tips
- Utilize a opção `-n` para acelerar a exibição de informações, especialmente em redes grandes, onde a resolução de nomes pode demorar.
- Combine opções para obter informações mais específicas, como `netstat -at` para listar apenas conexões TCP em escuta.
- Use `netstat` em conjunto com outros comandos, como `grep`, para filtrar resultados. Por exemplo:
  ```csh
  netstat -an | grep LISTEN
  ```
- Lembre-se de que o `netstat` pode não estar disponível em algumas distribuições mais recentes, onde pode ser substituído por `ss`.