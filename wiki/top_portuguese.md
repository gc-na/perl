# [Linux] C Shell (csh) top uso: Exibir processos em tempo real

## Overview
O comando `top` é uma ferramenta poderosa que exibe em tempo real os processos em execução no sistema. Ele fornece uma visão dinâmica do uso de recursos do sistema, como CPU e memória, permitindo que os usuários monitorem o desempenho e identifiquem processos que consomem muitos recursos.

## Usage
A sintaxe básica do comando `top` é a seguinte:

```
top [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `top`:

- `-d <tempo>`: Define o intervalo de atualização em segundos.
- `-n <número>`: Especifica o número de iterações a serem exibidas antes de sair.
- `-u <usuário>`: Filtra a exibição para mostrar apenas os processos de um usuário específico.
- `-p <PID>`: Monitora apenas o processo com o ID especificado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `top`:

1. **Executar o comando top padrão:**
   ```bash
   top
   ```

2. **Atualizar a exibição a cada 2 segundos:**
   ```bash
   top -d 2
   ```

3. **Mostrar apenas os processos de um usuário específico:**
   ```bash
   top -u nome_do_usuario
   ```

4. **Monitorar um processo específico pelo PID:**
   ```bash
   top -p 1234
   ```

5. **Executar o top por um número específico de iterações:**
   ```bash
   top -n 5
   ```

## Tips
- Utilize a tecla `h` enquanto o `top` está em execução para acessar a ajuda e ver os comandos de atalho disponíveis.
- Para sair do `top`, pressione a tecla `q`.
- Você pode ordenar os processos por diferentes colunas, como CPU ou memória, clicando nas respectivas cabeçalhos durante a execução do `top`.