# [Linux] C Shell (csh) dig Uso: consulta de DNS

## Overview
O comando `dig` (Domain Information Groper) é uma ferramenta de linha de comando utilizada para consultar informações sobre domínios DNS. Ele permite que os usuários obtenham detalhes sobre registros DNS, como endereços IP, registros MX, e muito mais.

## Usage
A sintaxe básica do comando `dig` é a seguinte:

```csh
dig [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `dig`:

- `@servidor`: Especifica um servidor DNS para realizar a consulta.
- `-t tipo`: Define o tipo de registro DNS a ser consultado (por exemplo, A, MX, TXT).
- `+short`: Exibe a resposta de forma mais concisa.
- `+trace`: Segue a cadeia de servidores DNS para resolver o domínio.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `dig`:

1. **Consultar o registro A de um domínio:**
   ```csh
   dig example.com
   ```

2. **Consultar um registro MX (Mail Exchange):**
   ```csh
   dig -t MX example.com
   ```

3. **Consultar um servidor DNS específico:**
   ```csh
   dig @8.8.8.8 example.com
   ```

4. **Obter uma resposta curta:**
   ```csh
   dig +short example.com
   ```

5. **Rastrear a resolução de um domínio:**
   ```csh
   dig +trace example.com
   ```

## Tips
- Utilize a opção `+short` para obter respostas mais diretas, especialmente quando você está apenas interessado nos endereços IP.
- Para resolver problemas de DNS, o uso da opção `+trace` pode ajudar a identificar onde a resolução está falhando.
- Sempre verifique se você está consultando o servidor DNS correto, especialmente em ambientes corporativos onde servidores internos podem estar em uso.