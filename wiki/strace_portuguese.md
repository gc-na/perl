# [Linux] C Shell (csh) strace Uso: rastrear chamadas de sistema

## Overview
O comando `strace` é uma ferramenta poderosa utilizada para rastrear chamadas de sistema e sinais recebidos por um processo em execução. Ele é especialmente útil para depuração e análise de problemas em programas, permitindo que os desenvolvedores vejam como um programa interage com o sistema operacional.

## Usage
A sintaxe básica do comando `strace` é a seguinte:

```csh
strace [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `strace`:

- `-c`: Resumo das chamadas de sistema e tempo gasto em cada uma.
- `-e <expressão>`: Filtra as chamadas de sistema a serem rastreadas com base na expressão fornecida.
- `-p <PID>`: Anexa o `strace` a um processo em execução, identificado pelo seu PID.
- `-o <arquivo>`: Redireciona a saída para o arquivo especificado em vez de exibi-la no terminal.

## Common Examples
Aqui estão alguns exemplos práticos de uso do `strace`:

1. **Rastrear um comando simples:**
   ```csh
   strace ls
   ```

2. **Rastrear um processo em execução:**
   ```csh
   strace -p 1234
   ```

3. **Salvar a saída em um arquivo:**
   ```csh
   strace -o output.txt ls
   ```

4. **Resumir as chamadas de sistema:**
   ```csh
   strace -c ls
   ```

5. **Filtrar chamadas de sistema específicas:**
   ```csh
   strace -e trace=open,close ls
   ```

## Tips
- Use `strace` com cautela em programas que fazem muitas chamadas de sistema, pois a saída pode ser extensa e difícil de analisar.
- Combine `strace` com outras ferramentas de depuração para obter uma visão mais completa do comportamento do programa.
- Sempre verifique a documentação do `strace` para opções adicionais que podem ser úteis para suas necessidades específicas.