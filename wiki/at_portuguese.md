# [Linux] C Shell (csh) at: Agendar comandos para execução futura

## Overview
O comando `at` permite que os usuários agendem a execução de comandos em um momento específico no futuro. É uma ferramenta útil para automatizar tarefas que precisam ser realizadas em horários determinados.

## Usage
A sintaxe básica do comando `at` é a seguinte:

```
at [opções] [hora]
```

## Common Options
- `-f <arquivo>`: Especifica um arquivo que contém os comandos a serem executados.
- `-m`: Envia um e-mail ao usuário após a execução do comando.
- `-q <fila>`: Define a fila de execução do comando.
- `-l`: Lista os trabalhos agendados.
- `-d <id>`: Remove um trabalho agendado com o ID especificado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `at`:

1. **Agendar um comando para ser executado agora**:
   ```bash
   echo "echo 'Olá, mundo!'" | at now
   ```

2. **Agendar um comando para ser executado em uma hora**:
   ```bash
   echo "backup.sh" | at now + 1 hour
   ```

3. **Agendar um comando para ser executado em um horário específico**:
   ```bash
   echo "shutdown -h now" | at 22:00
   ```

4. **Agendar um script a partir de um arquivo**:
   ```bash
   at -f script.sh 10:00
   ```

5. **Listar trabalhos agendados**:
   ```bash
   at -l
   ```

6. **Remover um trabalho agendado**:
   ```bash
   at -d 5
   ```

## Tips
- Sempre verifique a lista de trabalhos agendados com `at -l` para evitar duplicações.
- Use a opção `-m` se precisar de confirmação por e-mail após a execução do comando.
- Para agendamentos recorrentes, considere usar o `cron`, que é mais adequado para tarefas repetitivas.