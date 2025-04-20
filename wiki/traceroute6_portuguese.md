# [Linux] C Shell (csh) traceroute6 Uso: Rastrear rotas de pacotes IPv6

## Overview
O comando `traceroute6` é utilizado para rastrear a rota que os pacotes IPv6 seguem até um destino específico. Ele fornece informações sobre cada salto que os pacotes fazem, permitindo que os usuários identifiquem onde podem ocorrer problemas de rede.

## Usage
A sintaxe básica do comando `traceroute6` é a seguinte:

```bash
traceroute6 [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `traceroute6`:

- `-m <n>`: Define o número máximo de saltos (hops) a serem percorridos.
- `-p <n>`: Especifica a porta de destino a ser usada.
- `-w <n>`: Define o tempo de espera (em segundos) para cada resposta.
- `-q <n>`: Especifica o número de consultas a serem enviadas por salto.

## Common Examples
Aqui estão alguns exemplos práticos de como usar o `traceroute6`:

1. Rastrear a rota para um endereço IPv6 específico:
   ```bash
   traceroute6 2001:db8::1
   ```

2. Definir um número máximo de saltos para 15:
   ```bash
   traceroute6 -m 15 2001:db8::1
   ```

3. Especificar uma porta de destino:
   ```bash
   traceroute6 -p 80 2001:db8::1
   ```

4. Aumentar o tempo de espera para 5 segundos:
   ```bash
   traceroute6 -w 5 2001:db8::1
   ```

5. Enviar 3 consultas por salto:
   ```bash
   traceroute6 -q 3 2001:db8::1
   ```

## Tips
- Sempre verifique se o endereço IPv6 que você está tentando rastrear está acessível.
- Utilize a opção `-m` para evitar que o comando fique preso em uma rota que não responde.
- Combine opções para personalizar sua consulta de acordo com suas necessidades específicas.
- Lembre-se de que o `traceroute6` pode não funcionar em redes que bloqueiam pacotes ICMP.