# [Linux] C Shell (csh) who uso: Exibe usuários conectados ao sistema

## Overview
O comando `who` é utilizado para mostrar a lista de usuários que estão atualmente conectados ao sistema. Ele fornece informações como o nome do usuário, o terminal que estão utilizando e o horário em que se conectaram.

## Usage
A sintaxe básica do comando `who` é a seguinte:

```
who [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `who`:

- `-a`: Exibe todas as informações disponíveis, incluindo usuários conectados e informações sobre o sistema.
- `-b`: Mostra a última vez que o sistema foi inicializado.
- `-q`: Exibe apenas a lista de usuários conectados e a contagem total de usuários.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `who`:

1. **Listar todos os usuários conectados:**
   ```csh
   who
   ```

2. **Mostrar todas as informações disponíveis:**
   ```csh
   who -a
   ```

3. **Ver a última inicialização do sistema:**
   ```csh
   who -b
   ```

4. **Exibir apenas a contagem de usuários conectados:**
   ```csh
   who -q
   ```

## Tips
- Utilize `who -a` para obter uma visão completa do estado do sistema e dos usuários conectados.
- Combine o comando `who` com outros comandos, como `grep`, para filtrar informações específicas.
- Verifique regularmente quem está conectado ao sistema, especialmente em ambientes multiusuário, para manter a segurança e a privacidade.