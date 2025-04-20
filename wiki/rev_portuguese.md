# [Linux] C Shell (csh) rev: Inverte linhas de texto

## Overview
O comando `rev` é utilizado para inverter as linhas de texto de um arquivo ou da entrada padrão. Ele lê cada linha e a retorna em ordem inversa, o que pode ser útil em várias situações, como manipulação de strings ou processamento de dados.

## Usage
A sintaxe básica do comando é a seguinte:

```
rev [opções] [argumentos]
```

## Common Options
- `-o, --output=ARQUIVO`: Especifica um arquivo de saída para armazenar o resultado.
- `-h, --help`: Exibe uma mensagem de ajuda com informações sobre o uso do comando.
- `-V, --version`: Mostra a versão do comando `rev`.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `rev`:

1. **Inverter uma linha de texto diretamente no terminal:**
   ```bash
   echo "Olá Mundo" | rev
   ```
   Saída:
   ```
   odnu olA
   ```

2. **Inverter o conteúdo de um arquivo:**
   ```bash
   rev arquivo.txt
   ```

3. **Salvar a saída invertida em um novo arquivo:**
   ```bash
   rev arquivo.txt > arquivo_invertido.txt
   ```

4. **Inverter várias linhas de texto:**
   ```bash
   cat arquivo.txt | rev
   ```

## Tips
- Utilize `rev` em combinação com outros comandos, como `cat` ou `echo`, para manipular strings de forma mais eficiente.
- Lembre-se de redirecionar a saída para um arquivo se precisar manter o resultado invertido para uso posterior.
- Experimente usar `rev` em scripts para automatizar tarefas que envolvem manipulação de texto.