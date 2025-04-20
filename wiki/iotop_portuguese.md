# [Linux] C Shell (csh) iotop Uso: Monitora o uso de I/O por processos

## Overview
O comando `iotop` é uma ferramenta útil para monitorar o uso de entrada/saída (I/O) em sistemas Linux. Ele exibe quais processos estão consumindo mais recursos de I/O, permitindo que os administradores identifiquem e resolvam problemas de desempenho relacionados a disco.

## Usage
A sintaxe básica do comando `iotop` é a seguinte:

```bash
iotop [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `iotop`:

- `-o`: Exibe apenas os processos que estão fazendo uso de I/O.
- `-b`: Executa o `iotop` em modo batch, útil para gravação em arquivos.
- `-n NUM`: Define o número de iterações a serem exibidas no modo batch.
- `-d SECONDS`: Define o intervalo de atualização em segundos.

## Common Examples
Aqui estão alguns exemplos práticos de como usar o `iotop`:

1. **Executar o iotop em tempo real:**
   ```bash
   iotop
   ```

2. **Mostrar apenas processos que estão utilizando I/O:**
   ```bash
   iotop -o
   ```

3. **Executar em modo batch com atualizações a cada 2 segundos:**
   ```bash
   iotop -b -d 2
   ```

4. **Executar em modo batch e limitar a 5 iterações:**
   ```bash
   iotop -b -n 5
   ```

## Tips
- Utilize a opção `-o` para filtrar rapidamente os processos que estão realmente utilizando I/O, o que pode ajudar na identificação de problemas.
- Considere usar o modo batch (`-b`) se você precisar registrar a saída em um arquivo para análise posterior.
- Monitore o `iotop` em intervalos regulares para ter uma visão clara do desempenho do sistema ao longo do tempo.