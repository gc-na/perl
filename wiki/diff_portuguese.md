# [Linux] C Shell (csh) diff Uso: Comparar arquivos linha a linha

## Overview
O comando `diff` é utilizado para comparar o conteúdo de dois arquivos, mostrando as diferenças entre eles linha por linha. É uma ferramenta essencial para desenvolvedores e administradores de sistemas que precisam identificar alterações em arquivos de texto.

## Usage
A sintaxe básica do comando `diff` é a seguinte:

```csh
diff [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `diff`:

- `-u`: Exibe as diferenças em um formato unificado, que é mais fácil de ler.
- `-c`: Mostra as diferenças em um formato de contexto, que inclui algumas linhas de contexto ao redor das alterações.
- `-i`: Ignora diferenças de maiúsculas e minúsculas.
- `-w`: Ignora espaços em branco ao comparar linhas.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `diff`:

1. Comparar dois arquivos simples:
   ```csh
   diff arquivo1.txt arquivo2.txt
   ```

2. Usar o formato unificado para visualizar as diferenças:
   ```csh
   diff -u arquivo1.txt arquivo2.txt
   ```

3. Ignorar diferenças de maiúsculas e minúsculas:
   ```csh
   diff -i arquivo1.txt arquivo2.txt
   ```

4. Comparar diretórios inteiros:
   ```csh
   diff -r diretorio1/ diretorio2/
   ```

5. Mostrar diferenças em formato de contexto:
   ```csh
   diff -c arquivo1.txt arquivo2.txt
   ```

## Tips
- Sempre verifique se os arquivos que você está comparando estão no mesmo formato (por exemplo, ambos como arquivos de texto).
- Utilize a opção `-u` para uma visualização mais clara das diferenças, especialmente ao revisar alterações em código.
- Para comparar diretórios, a opção `-r` é muito útil, pois permite ver todas as diferenças em arquivos dentro dos diretórios especificados.