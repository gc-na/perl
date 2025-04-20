# [Linux] C Shell (csh) iconv Uso: Conversão de codificações de texto

## Overview
O comando `iconv` é utilizado para converter arquivos de texto entre diferentes codificações de caracteres. Isso é especialmente útil quando se trabalha com arquivos que podem ter sido criados em sistemas ou ambientes com diferentes padrões de codificação.

## Usage
A sintaxe básica do comando `iconv` é a seguinte:

```csh
iconv [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o comando `iconv`:

- `-f` : Especifica a codificação de origem.
- `-t` : Especifica a codificação de destino.
- `-o` : Define o arquivo de saída. Se não for especificado, a saída será enviada para o stdout.
- `-l` : Lista todas as codificações suportadas.

## Common Examples

### Exemplo 1: Converter de UTF-8 para ISO-8859-1
```csh
iconv -f UTF-8 -t ISO-8859-1 arquivo_entrada.txt -o arquivo_saida.txt
```

### Exemplo 2: Converter de Windows-1252 para UTF-8
```csh
iconv -f WINDOWS-1252 -t UTF-8 arquivo_entrada.txt -o arquivo_saida.txt
```

### Exemplo 3: Listar todas as codificações suportadas
```csh
iconv -l
```

### Exemplo 4: Converter e exibir a saída no terminal
```csh
iconv -f UTF-8 -t ASCII arquivo_entrada.txt
```

## Tips
- Sempre verifique as codificações de origem e destino para evitar perda de dados.
- Utilize a opção `-o` para salvar a saída em um novo arquivo, evitando sobrescrever o arquivo original.
- Teste a conversão com um pequeno trecho do arquivo antes de processar arquivos grandes.