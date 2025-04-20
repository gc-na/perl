# [Linux] C Shell (csh) last comando: exibir logins recentes

## Overview
O comando `last` é utilizado para exibir uma lista dos usuários que fizeram login no sistema, juntamente com informações sobre o tempo e a duração de suas sessões. Ele lê o arquivo de log `/var/log/wtmp`, que registra todos os logins e logouts.

## Usage
A sintaxe básica do comando `last` é a seguinte:

```csh
last [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `last`:

- `-n [n]`: Exibe apenas os últimos `n` logins.
- `-R`: Não exibe o nome do host.
- `-f [arquivo]`: Lê de um arquivo específico em vez do padrão `/var/log/wtmp`.
- `-x`: Exibe também as sessões de shutdown e reboot.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `last`:

1. **Exibir todos os logins recentes:**
   ```csh
   last
   ```

2. **Exibir os últimos 5 logins:**
   ```csh
   last -n 5
   ```

3. **Exibir logins sem mostrar o nome do host:**
   ```csh
   last -R
   ```

4. **Ler de um arquivo específico:**
   ```csh
   last -f /caminho/para/arquivo
   ```

5. **Incluir sessões de shutdown e reboot:**
   ```csh
   last -x
   ```

## Tips
- Utilize a opção `-n` para limitar a saída e facilitar a leitura, especialmente em sistemas com muitos logins.
- Combine opções para personalizar a saída conforme necessário, como `last -n 10 -R` para os últimos 10 logins sem o nome do host.
- Verifique regularmente os logs de login para monitorar a atividade do sistema e detectar acessos não autorizados.