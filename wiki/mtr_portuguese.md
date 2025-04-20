# [Linux] C Shell (csh) mtr Uso: Ferramenta de diagnóstico de rede

## Overview
O comando `mtr` combina as funcionalidades do `ping` e do `traceroute`, permitindo que você monitore a rota de pacotes de dados até um determinado host. Ele fornece informações em tempo real sobre a latência e a perda de pacotes em cada salto da rota.

## Usage
A sintaxe básica do comando `mtr` é a seguinte:

```
mtr [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `mtr`:

- `-r`: Executa o `mtr` em modo relatório, exibindo os resultados uma única vez.
- `-c <n>`: Define o número de pacotes a serem enviados, onde `<n>` é um número inteiro.
- `-i <s>`: Define o intervalo entre os pacotes enviados, onde `<s>` é o número de segundos.
- `--report`: Gera um relatório ao final da execução, útil para capturar resultados em um formato legível.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `mtr`:

1. **Executar um teste básico de conectividade:**
   ```bash
   mtr google.com
   ```

2. **Executar um teste com um número específico de pacotes:**
   ```bash
   mtr -c 10 google.com
   ```

3. **Executar em modo relatório:**
   ```bash
   mtr -r google.com
   ```

4. **Definir um intervalo entre pacotes:**
   ```bash
   mtr -i 2 google.com
   ```

5. **Gerar um relatório detalhado:**
   ```bash
   mtr --report google.com
   ```

## Tips
- Utilize o modo relatório (`-r`) para capturar resultados de forma mais organizada, especialmente em scripts.
- Experimente ajustar o intervalo entre pacotes (`-i`) para evitar sobrecarregar a rede durante testes.
- Combine o `mtr` com outras ferramentas de rede para uma análise mais abrangente, como `ping` e `traceroute`.