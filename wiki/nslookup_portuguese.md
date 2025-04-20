# [Linux] C Shell (csh) nslookup Uso: Consulta de endereços IP e nomes de domínio

## Overview
O comando `nslookup` é utilizado para consultar informações sobre servidores de nomes de domínio (DNS). Ele permite que os usuários obtenham o endereço IP associado a um nome de domínio ou vice-versa.

## Usage
A sintaxe básica do comando é a seguinte:

```csh
nslookup [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `nslookup`:

- `-type=tipo`: Especifica o tipo de consulta DNS (por exemplo, A, MX, CNAME).
- `-timeout=segundos`: Define o tempo limite para a consulta.
- `-retry=número`: Define o número de tentativas de consulta em caso de falha.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `nslookup`:

1. **Consultar o endereço IP de um domínio:**
   ```csh
   nslookup www.exemplo.com
   ```

2. **Consultar o nome de domínio associado a um endereço IP:**
   ```csh
   nslookup 192.0.2.1
   ```

3. **Consultar registros MX (Mail Exchange) de um domínio:**
   ```csh
   nslookup -type=MX exemplo.com
   ```

4. **Definir um servidor DNS específico para a consulta:**
   ```csh
   nslookup www.exemplo.com 8.8.8.8
   ```

## Tips
- Sempre verifique se você está utilizando o servidor DNS correto, especialmente em ambientes corporativos.
- Utilize a opção `-type` para obter informações específicas, como registros A ou MX.
- Se você estiver enfrentando problemas de resolução de nomes, tente usar um servidor DNS público, como o Google (8.8.8.8).