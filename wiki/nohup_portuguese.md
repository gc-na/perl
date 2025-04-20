# [Linux] C Shell (csh) nohup uso: Executar comandos sem interrupção ao sair da sessão

## Overview
O comando `nohup` (no hang up) é utilizado para executar processos que continuam em execução mesmo após o usuário sair da sessão. Isso é especialmente útil para tarefas longas que você deseja que continuem rodando em segundo plano.

## Usage
A sintaxe básica do comando `nohup` é a seguinte:

```csh
nohup [opções] [argumentos]
```

## Common Options
- `&`: Coloca o comando em segundo plano.
- `-h`: Exibe a ajuda sobre o comando.
- `-v`: Exibe informações detalhadas sobre a execução do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `nohup`:

1. Executar um script em segundo plano:
   ```csh
   nohup ./meu_script.sh &
   ```

2. Rodar um comando que gera saída em um arquivo:
   ```csh
   nohup ls -l > lista.txt &
   ```

3. Executar um comando que não deve ser interrompido ao sair da sessão:
   ```csh
   nohup python meu_programa.py &
   ```

4. Executar um comando com saída padrão e de erro redirecionadas para um arquivo:
   ```csh
   nohup comando_qualquer > saida.txt 2>&1 &
   ```

## Tips
- Sempre redirecione a saída de comandos longos para um arquivo para evitar a perda de informações.
- Utilize `jobs` para verificar os processos em segundo plano.
- Combine `nohup` com `&` para garantir que o comando seja executado sem bloquear o terminal.