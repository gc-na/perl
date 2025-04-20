# [Linux] C Shell (csh) trap Uso: Captura de sinais e execução de comandos

## Overview
O comando `trap` no C Shell (csh) é utilizado para capturar sinais e executar comandos específicos quando esses sinais são recebidos. Isso é útil para gerenciar a forma como um script ou processo responde a eventos como interrupções ou encerramentos.

## Usage
A sintaxe básica do comando `trap` é a seguinte:

```csh
trap [options] [arguments]
```

## Common Options
- `signal`: Especifica o sinal que deve ser capturado (por exemplo, `INT` para interrupção).
- `command`: O comando que será executado quando o sinal especificado for recebido.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `trap`:

1. **Capturando uma interrupção (Ctrl+C)**:
   ```csh
   trap 'echo "Interrupção recebida!"' INT
   ```

2. **Limpeza antes de sair**:
   ```csh
   trap 'rm -f /tmp/tempfile; exit' EXIT
   ```

3. **Capturando o sinal de término (SIGTERM)**:
   ```csh
   trap 'echo "Processo terminado!"' TERM
   ```

4. **Executando um comando ao receber um sinal**:
   ```csh
   trap 'echo "Sinal recebido, executando tarefa de limpeza."' HUP
   ```

## Tips
- Sempre teste seus scripts para garantir que o `trap` está funcionando como esperado, especialmente em situações críticas.
- Use `trap` para garantir que recursos temporários sejam limpos adequadamente, evitando vazamentos de recursos.
- Considere a ordem dos sinais e comandos, pois múltiplos `trap` podem ser definidos para diferentes sinais.