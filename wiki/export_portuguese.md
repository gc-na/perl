# [Linux] C Shell (csh) export uso: Define variáveis de ambiente

## Overview
O comando `export` no C Shell (csh) é utilizado para definir variáveis de ambiente que podem ser acessadas por processos filhos. Isso é útil para configurar o ambiente de execução de programas e scripts.

## Usage
A sintaxe básica do comando `export` é a seguinte:

```csh
export [opções] [argumentos]
```

## Common Options
- `-n`: Remove a variável do ambiente exportado.
- `-p`: Exibe todas as variáveis de ambiente exportadas.

## Common Examples

### Exemplo 1: Exportar uma variável simples
Para exportar uma variável chamada `MY_VAR` com o valor `hello`, você pode usar:

```csh
set MY_VAR = "hello"
export MY_VAR
```

### Exemplo 2: Exportar múltiplas variáveis
Você pode exportar várias variáveis de uma só vez:

```csh
set VAR1 = "value1"
set VAR2 = "value2"
export VAR1 VAR2
```

### Exemplo 3: Verificar variáveis exportadas
Para listar todas as variáveis de ambiente que foram exportadas, utilize:

```csh
export -p
```

### Exemplo 4: Remover uma variável do ambiente
Para remover uma variável exportada, como `MY_VAR`, você pode fazer:

```csh
export -n MY_VAR
```

## Tips
- Sempre verifique se a variável foi exportada corretamente usando `export -p`.
- Lembre-se de que as variáveis exportadas só estão disponíveis para processos filhos, não para o shell pai.
- Use nomes de variáveis que sejam descritivos para facilitar a manutenção do seu ambiente.