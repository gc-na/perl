# [Linux] C Shell (csh) finger uso: Exibir informações sobre usuários

## Overview
O comando `finger` é utilizado para exibir informações sobre usuários no sistema. Ele fornece detalhes como nome completo, horário de login, e o estado atual do usuário, permitindo que você veja rapidamente quem está logado e algumas informações adicionais sobre eles.

## Usage
A sintaxe básica do comando `finger` é a seguinte:

```
finger [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `finger`:

- `-l`: Exibe informações detalhadas sobre o usuário, incluindo a última vez que ele fez login.
- `-m`: Ignora a distinção entre maiúsculas e minúsculas ao buscar usuários.
- `-s`: Exibe uma lista resumida de usuários logados, mostrando apenas o nome e o estado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `finger`:

1. Para exibir informações de todos os usuários logados:
   ```bash
   finger
   ```

2. Para exibir informações detalhadas sobre um usuário específico:
   ```bash
   finger nome_do_usuario
   ```

3. Para exibir uma lista resumida de usuários logados:
   ```bash
   finger -s
   ```

4. Para buscar um usuário sem considerar maiúsculas e minúsculas:
   ```bash
   finger -m nome_do_usuario
   ```

## Tips
- Utilize `finger` em combinação com outros comandos, como `grep`, para filtrar resultados específicos.
- Verifique se o serviço `finger` está habilitado no seu sistema, pois pode não estar ativo por padrão em algumas distribuições.
- Use `man finger` para acessar o manual completo e explorar mais opções disponíveis.