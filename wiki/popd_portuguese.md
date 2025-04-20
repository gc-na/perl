# [Linux] C Shell (csh) popd Uso: Remove diretórios da pilha

## Overview
O comando `popd` é utilizado no C Shell para remover o diretório mais recente da pilha de diretórios. Ele permite que você retorne rapidamente ao diretório anterior que foi salvo, facilitando a navegação entre diretórios.

## Usage
A sintaxe básica do comando `popd` é a seguinte:

```csh
popd [opções]
```

## Common Options
O comando `popd` possui algumas opções comuns que podem ser utilizadas:

- `+n`: Remove o diretório na posição `n` da pilha.
- `-n`: Remove o diretório na posição `n` da pilha, contando de trás para frente.

## Common Examples

### Exemplo 1: Remover o diretório mais recente
```csh
popd
```
Este comando remove o diretório mais recente da pilha e muda para o diretório anterior.

### Exemplo 2: Remover um diretório específico da pilha
```csh
popd +1
```
Este comando remove o diretório na segunda posição da pilha (contando a partir de zero) e muda para o diretório que estava antes dele.

### Exemplo 3: Remover o último diretório da pilha
```csh
popd -1
```
Este comando remove o último diretório da pilha e retorna ao diretório que estava antes dele.

## Tips
- Utilize `dirs` para visualizar a pilha de diretórios antes de usar `popd`, assim você pode ter certeza de qual diretório será removido.
- Combine `pushd` e `popd` para alternar rapidamente entre diretórios sem perder o histórico de navegação.
- Lembre-se de que o `popd` só funcionará se houver diretórios na pilha; caso contrário, você receberá uma mensagem de erro.