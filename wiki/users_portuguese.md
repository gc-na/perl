# [Linux] C Shell (csh) users equivalente: listar usuários do sistema

## Overview
O comando `users` no C Shell (csh) é utilizado para exibir os nomes dos usuários que estão atualmente logados no sistema. Ele fornece uma maneira rápida de verificar quem está ativo em um determinado momento.

## Usage
A sintaxe básica do comando `users` é a seguinte:

```
users [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `users`:

- `-n`: Exibe o número de usuários logados.
- `-r`: Exibe apenas os usuários que estão logados em terminais remotos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `users`:

1. **Listar todos os usuários logados:**
   ```csh
   users
   ```

2. **Contar o número de usuários logados:**
   ```csh
   users -n
   ```

3. **Listar usuários logados remotamente:**
   ```csh
   users -r
   ```

## Tips
- Utilize o comando `who` para obter informações mais detalhadas sobre os usuários logados, como o terminal e o horário de login.
- Combine o comando `users` com outros comandos, como `wc -w`, para contar quantos usuários estão logados:
  ```csh
  users | wc -w
  ```
- Para um monitoramento contínuo, você pode usar um loop em um script que chama `users` em intervalos regulares.