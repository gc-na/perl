# [Linux] C Shell (csh) htop Uso: Visualização interativa de processos

## Overview
O comando `htop` é uma ferramenta interativa de monitoramento de processos que permite visualizar em tempo real o uso da CPU, memória e outros recursos do sistema. É uma alternativa mais amigável e visual ao comando `top`, oferecendo uma interface colorida e opções de navegação mais intuitivas.

## Usage
A sintaxe básica do comando `htop` é a seguinte:

```csh
htop [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `htop`:

- `-h`, `--help`: Exibe a ajuda e as opções disponíveis.
- `-s`, `--sort`: Permite classificar os processos por uma coluna específica, como CPU ou memória.
- `-p`, `--pid`: Monitora apenas os processos com os IDs especificados.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `htop`:

1. **Iniciar o htop**:
   ```csh
   htop
   ```

2. **Iniciar o htop e classificar por uso de memória**:
   ```csh
   htop -s MEM%
   ```

3. **Monitora processos específicos pelo PID**:
   ```csh
   htop -p 1234,5678
   ```

4. **Exibir ajuda sobre o htop**:
   ```csh
   htop -h
   ```

## Tips
- Utilize as teclas de atalho dentro do `htop` para facilitar a navegação, como `F6` para mudar a coluna de ordenação.
- Você pode usar as setas do teclado para navegar entre os processos e `F9` para enviar sinais a um processo selecionado.
- Para sair do `htop`, pressione `q`.