# [Linux] C Shell (csh) write uso: Enviar mensagens para outros usuários

## Overview
O comando `write` no C Shell (csh) permite que você envie mensagens de texto para outros usuários que estão logados no mesmo sistema. É uma maneira simples e direta de se comunicar com colegas de trabalho ou amigos que estão usando o mesmo computador.

## Usage
A sintaxe básica do comando `write` é a seguinte:

```
write [opções] [usuário] [terminal]
```

## Common Options
- `-n`: Não exibe o nome do usuário que está enviando a mensagem.
- `-h`: Não envia a mensagem se o usuário estiver ocupado.

## Common Examples

### Enviar uma mensagem para um usuário específico
Para enviar uma mensagem para um usuário chamado `joao`, você pode usar o seguinte comando:

```csh
write joao
```
Após executar o comando, você pode digitar sua mensagem e pressionar `Ctrl+D` para enviar.

### Enviar uma mensagem para um usuário em um terminal específico
Se você souber que `maria` está logada em um terminal específico, como `pts/1`, você pode enviar uma mensagem diretamente para esse terminal:

```csh
write maria pts/1
```

### Enviar uma mensagem sem mostrar seu nome
Para enviar uma mensagem sem que o destinatário veja seu nome, utilize a opção `-n`:

```csh
write -n joao
```

## Tips
- Certifique-se de que o usuário que você deseja contatar está logado e disponível para receber mensagens.
- Use `who` para verificar quais usuários estão logados e em quais terminais.
- Lembre-se de que o destinatário pode estar ocupado e pode não responder imediatamente.