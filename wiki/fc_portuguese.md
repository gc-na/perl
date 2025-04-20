# [Linux] C Shell (csh) fc <Uso equivalente em português>: Editar e reexecutar comandos anteriores

## Overview
O comando `fc` no C Shell (csh) é utilizado para listar, editar e reexecutar comandos que foram previamente executados na sessão atual do shell. Ele é uma ferramenta útil para corrigir erros ou modificar comandos sem precisar digitá-los novamente.

## Usage
A sintaxe básica do comando `fc` é a seguinte:

```csh
fc [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `fc`:

- `-l`: Lista os comandos anteriores sem editá-los.
- `-e editor`: Especifica um editor para editar os comandos (por exemplo, `-e vi`).
- `-n`: Não exibe números de linha na lista de comandos.

## Common Examples

### Listar os últimos 10 comandos
Para listar os últimos 10 comandos executados, você pode usar:

```csh
fc -l -10
```

### Editar o último comando
Para editar o último comando executado com o editor padrão, utilize:

```csh
fc
```

### Editar um comando específico
Se você quiser editar um comando específico, por exemplo, o comando número 5, você pode fazer:

```csh
fc 5
```

### Reexecutar o último comando
Para reexecutar o último comando sem editá-lo, basta usar:

```csh
fc -s
```

### Usar um editor específico
Para editar o último comando usando o editor `nano`, você pode fazer:

```csh
fc -e nano
```

## Tips
- Utilize `fc -l` para revisar rapidamente os comandos anteriores antes de decidir editar ou reexecutar.
- Sempre verifique o comando que você está prestes a reexecutar, especialmente se ele envolve operações destrutivas.
- Configure seu editor preferido para o `fc` para facilitar a edição dos comandos.