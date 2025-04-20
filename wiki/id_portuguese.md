# [Linux] C Shell (csh) id uso: exibir informações do usuário

## Overview
O comando `id` no C Shell (csh) é utilizado para exibir informações sobre o usuário atual ou sobre um usuário específico. Ele fornece detalhes como o UID (User ID), GID (Group ID) e os grupos aos quais o usuário pertence.

## Usage
A sintaxe básica do comando `id` é a seguinte:

```
id [opções] [argumentos]
```

## Common Options
- `-u`: Exibe apenas o UID do usuário.
- `-g`: Exibe apenas o GID do grupo principal do usuário.
- `-G`: Exibe todos os GIDs dos grupos aos quais o usuário pertence.
- `-n`: Exibe o nome do usuário ou do grupo em vez do ID numérico.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `id`:

1. Exibir informações do usuário atual:
   ```csh
   id
   ```

2. Exibir apenas o UID do usuário atual:
   ```csh
   id -u
   ```

3. Exibir apenas o GID do grupo principal do usuário atual:
   ```csh
   id -g
   ```

4. Exibir todos os GIDs dos grupos do usuário atual:
   ```csh
   id -G
   ```

5. Exibir informações de um usuário específico (por exemplo, "usuario1"):
   ```csh
   id usuario1
   ```

## Tips
- Utilize `id` sem opções para obter uma visão geral completa das informações do usuário.
- Combine opções para personalizar a saída conforme necessário, como `id -u -n` para obter o nome do usuário atual.
- Lembre-se de que você pode verificar as informações de outros usuários, desde que tenha permissões adequadas.