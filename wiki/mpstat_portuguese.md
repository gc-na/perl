# [Linux] C Shell (csh) mpstat Uso: Monitora estatísticas de CPU

## Overview
O comando `mpstat` é utilizado para exibir estatísticas de uso da CPU em sistemas operacionais Unix e Linux. Ele fornece informações detalhadas sobre a carga de trabalho de cada processador, permitindo que os usuários analisem o desempenho do sistema.

## Usage
A sintaxe básica do comando `mpstat` é a seguinte:

```csh
mpstat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `mpstat`:

- `-P ALL`: Exibe estatísticas para todos os processadores.
- `-u`: Mostra a utilização da CPU.
- `-r`: Exibe informações sobre a utilização da memória.
- `-h`: Mostra a ajuda com as opções disponíveis.

## Common Examples
Abaixo estão alguns exemplos práticos do uso do comando `mpstat`:

1. **Exibir estatísticas de todos os processadores:**

```csh
mpstat -P ALL
```

2. **Mostrar a utilização da CPU a cada 5 segundos:**

```csh
mpstat 5
```

3. **Exibir informações sobre a utilização da memória:**

```csh
mpstat -r
```

4. **Mostrar a utilização da CPU apenas para o processador 0:**

```csh
mpstat -P 0
```

## Tips
- Utilize a opção `-P ALL` para obter uma visão geral do desempenho de todos os processadores, especialmente em sistemas multi-core.
- Combine o `mpstat` com outras ferramentas de monitoramento, como `top` ou `vmstat`, para uma análise mais completa do sistema.
- Execute o comando em intervalos regulares para monitorar mudanças no desempenho ao longo do tempo.