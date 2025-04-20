# [Linux] C Shell (csh) watch uso: Monitora a execução de comandos periodicamente

## Overview
O comando `watch` é utilizado para executar periodicamente um comando e exibir sua saída na tela. Isso é útil para monitorar mudanças em tempo real, como a atualização de arquivos ou o estado de processos.

## Usage
A sintaxe básica do comando `watch` é a seguinte:

```csh
watch [opções] [comando]
```

## Common Options
Aqui estão algumas opções comuns do comando `watch`:

- `-n <segundos>`: Define o intervalo de tempo em segundos entre as execuções do comando.
- `-d`: Destaca as diferenças entre a saída anterior e a nova.
- `-t`: Remove a exibição do cabeçalho que mostra o comando sendo executado e o tempo.

## Common Examples

### Exemplo 1: Monitorar o uso de disco
Para monitorar o uso de disco a cada 5 segundos, você pode usar:

```csh
watch -n 5 df -h
```

### Exemplo 2: Monitorar processos
Para observar a lista de processos em execução e suas mudanças, execute:

```csh
watch ps aux
```

### Exemplo 3: Verificar a carga do sistema
Para verificar a carga do sistema a cada 2 segundos, utilize:

```csh
watch -n 2 uptime
```

### Exemplo 4: Monitorar um arquivo de log
Para monitorar um arquivo de log e ver as novas entradas, você pode usar:

```csh
watch tail -n 10 /var/log/syslog
```

## Tips
- Use a opção `-d` para facilitar a visualização de mudanças significativas na saída.
- Combine o `watch` com comandos que fornecem informações em tempo real, como `top` ou `netstat`, para obter uma visão dinâmica do sistema.
- Lembre-se de que o uso excessivo de `watch` pode consumir recursos do sistema, então ajuste o intervalo de tempo conforme necessário.