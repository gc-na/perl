# [Linux] C Shell (csh) bg <Uso equivalente em português>: Colocar um trabalho em segundo plano

## Overview
O comando `bg` no C Shell (csh) é utilizado para retomar a execução de um trabalho que foi interrompido, colocando-o em segundo plano. Isso permite que o usuário continue utilizando o terminal enquanto o trabalho é executado.

## Usage
A sintaxe básica do comando `bg` é a seguinte:

```csh
bg [opções] [número do trabalho]
```

## Common Options
- `número do trabalho`: Especifica qual trabalho deve ser colocado em segundo plano. Se não for fornecido, o último trabalho interrompido será utilizado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `bg`:

1. **Colocar o último trabalho interrompido em segundo plano:**
   ```csh
   bg
   ```

2. **Colocar um trabalho específico em segundo plano (por exemplo, trabalho 1):**
   ```csh
   bg %1
   ```

3. **Colocar um trabalho em segundo plano após ter sido interrompido com Ctrl+Z:**
   ```csh
   bg %2
   ```

## Tips
- Sempre verifique a lista de trabalhos em segundo plano usando o comando `jobs` antes de usar `bg`, para saber qual trabalho você deseja retomar.
- Utilize `fg` se você precisar trazer um trabalho de volta para o primeiro plano.
- Lembre-se de que, ao usar `bg`, o trabalho continuará a ser executado, mas você não verá sua saída diretamente no terminal.