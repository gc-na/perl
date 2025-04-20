# [Linux] C Shell (csh) comm: Compara linhas de dois arquivos

## Overview
O comando `comm` é utilizado para comparar duas arquivos de texto ordenados linha por linha. Ele exibe as linhas que são exclusivas a cada arquivo e as linhas que são comuns a ambos.

## Usage
A sintaxe básica do comando é a seguinte:

```csh
comm [opções] [arquivos]
```

## Common Options
- `-1`: Suprime a saída das linhas que estão apenas no primeiro arquivo.
- `-2`: Suprime a saída das linhas que estão apenas no segundo arquivo.
- `-3`: Suprime a saída das linhas que estão em ambos os arquivos.
- `-i`: Ignora diferenças entre maiúsculas e minúsculas.

## Common Examples

1. **Comparar dois arquivos e mostrar todas as linhas**:
   ```csh
   comm arquivo1.txt arquivo2.txt
   ```

2. **Mostrar apenas as linhas que estão no primeiro arquivo**:
   ```csh
   comm -13 arquivo1.txt arquivo2.txt
   ```

3. **Mostrar apenas as linhas que estão no segundo arquivo**:
   ```csh
   comm -12 arquivo1.txt arquivo2.txt
   ```

4. **Comparar arquivos ignorando diferenças de maiúsculas e minúsculas**:
   ```csh
   comm -i arquivo1.txt arquivo2.txt
   ```

## Tips
- Certifique-se de que os arquivos estejam ordenados antes de usar o comando `comm`, pois ele requer que as entradas estejam em ordem alfabética.
- Use a opção `-1`, `-2` ou `-3` conforme necessário para filtrar a saída e focar nas informações que você realmente precisa.
- Para uma comparação mais visual, considere redirecionar a saída para um arquivo ou usar um pager como `less`.