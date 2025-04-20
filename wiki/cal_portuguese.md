# [Linux] C Shell (csh) cal <Uso equivalente em português>: exibir um calendário

## Overview
O comando `cal` é utilizado para exibir um calendário no terminal. Ele pode mostrar o calendário de um mês específico ou de um ano inteiro, facilitando a visualização de datas e dias da semana.

## Usage
A sintaxe básica do comando `cal` é a seguinte:

```
cal [opções] [argumentos]
```

## Common Options
- `-m`: Exibe o calendário começando pela segunda-feira.
- `-y`: Mostra o calendário do ano atual.
- `-3`: Exibe o mês atual, o mês anterior e o próximo mês.
- `-j`: Mostra o calendário com os dias do ano (número do dia).
- `-A [n]`: Mostra n meses após o mês atual.
- `-B [n]`: Mostra n meses antes do mês atual.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `cal`:

1. **Exibir o calendário do mês atual:**
   ```csh
   cal
   ```

2. **Exibir o calendário de um mês específico (por exemplo, março de 2023):**
   ```csh
   cal 03 2023
   ```

3. **Exibir o calendário do ano atual:**
   ```csh
   cal -y
   ```

4. **Mostrar o mês atual, o mês anterior e o próximo mês:**
   ```csh
   cal -3
   ```

5. **Exibir o calendário com os dias do ano:**
   ```csh
   cal -j
   ```

## Tips
- Utilize a opção `-m` se preferir que a semana comece na segunda-feira, especialmente se você estiver acostumado com essa convenção.
- Para planejar eventos, o comando `cal -A 3` pode ser útil para visualizar rapidamente os próximos meses.
- Combine o `cal` com outros comandos, como `grep`, para encontrar datas específicas ou eventos em um calendário mais extenso.