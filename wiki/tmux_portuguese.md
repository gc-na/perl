# [Linux] C Shell (csh) tmux uso: Gerenciar sessões de terminal

## Overview
O comando `tmux` é um multiplexador de terminal que permite a criação, gerenciamento e navegação entre várias sessões de terminal dentro de uma única janela. Ele é especialmente útil para usuários que precisam trabalhar em múltiplas tarefas simultaneamente ou que desejam manter sessões ativas mesmo após desconectar-se.

## Usage
A sintaxe básica do comando `tmux` é a seguinte:

```bash
tmux [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `tmux`:

- `new`: Cria uma nova sessão.
- `attach`: Anexa-se a uma sessão existente.
- `detach`: Desanexa a sessão atual.
- `list-sessions`: Lista todas as sessões ativas.
- `kill-session`: Encerra uma sessão específica.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `tmux`:

1. **Criar uma nova sessão:**
   ```bash
   tmux new -s minha_sessao
   ```

2. **Anexar-se a uma sessão existente:**
   ```bash
   tmux attach -t minha_sessao
   ```

3. **Desanexar a sessão atual:**
   ```bash
   Ctrl + b, d
   ```

4. **Listar todas as sessões ativas:**
   ```bash
   tmux list-sessions
   ```

5. **Encerrar uma sessão específica:**
   ```bash
   tmux kill-session -t minha_sessao
   ```

## Tips
- Utilize a combinação de teclas `Ctrl + b` seguida de `?` dentro do `tmux` para ver uma lista de comandos disponíveis.
- Nomeie suas sessões de forma descritiva para facilitar a identificação.
- Considere usar `tmux` em conjunto com `ssh` para manter sessões persistentes em servidores remotos.