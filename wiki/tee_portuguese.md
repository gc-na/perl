# [Linux] C Shell (csh) tee uso: redireciona a saída para um ou mais arquivos

## Overview
O comando `tee` é utilizado no C Shell para ler a entrada padrão e gravar tanto na saída padrão quanto em um ou mais arquivos. Isso permite que você visualize a saída de um comando enquanto também a salva em um arquivo.

## Usage
A sintaxe básica do comando `tee` é a seguinte:

```csh
tee [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `tee`:

- `-a`: Anexa a saída ao arquivo em vez de sobrescrevê-lo.
- `-i`: Ignora sinais de interrupção.

## Common Examples

### Exemplo 1: Gravar a saída de um comando em um arquivo
```csh
ls -l | tee lista.txt
```
Neste exemplo, a saída do comando `ls -l` é exibida na tela e também gravada no arquivo `lista.txt`.

### Exemplo 2: Anexar a saída a um arquivo existente
```csh
echo "Nova linha" | tee -a lista.txt
```
Aqui, a string "Nova linha" é adicionada ao final do arquivo `lista.txt`, mantendo o conteúdo anterior.

### Exemplo 3: Usar com múltiplos arquivos
```csh
echo "Dados importantes" | tee arquivo1.txt arquivo2.txt
```
Este comando grava "Dados importantes" em `arquivo1.txt` e `arquivo2.txt` simultaneamente.

## Tips
- Utilize a opção `-a` quando quiser adicionar informações a um arquivo existente sem perder os dados já gravados.
- Combine `tee` com outros comandos para monitorar processos enquanto salva a saída, como em `dmesg | tee log.txt`.
- Lembre-se de que o `tee` pode ser útil em scripts para registrar a saída de comandos para análise posterior.