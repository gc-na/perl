# [Linux] C Shell (csh) script uso: Grava a sessão do terminal

## Overview
O comando `script` é utilizado para gravar uma sessão do terminal em um arquivo. Isso é útil para registrar a saída de comandos e interações em um ambiente de linha de comando, permitindo que você revise ou compartilhe a sessão posteriormente.

## Usage
A sintaxe básica do comando `script` é a seguinte:

```csh
script [opções] [arquivo]
```

## Common Options
- `-a`: Anexa a saída ao arquivo existente, em vez de sobrescrevê-lo.
- `-q`: Executa o comando em modo silencioso, sem exibir mensagens de início e término.
- `-t`: Grava o tempo de execução da sessão em um arquivo separado.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `script`:

1. **Gravar uma sessão padrão:**

   ```csh
   script sessao.txt
   ```

   Este comando inicia a gravação da sessão atual e salva a saída em `sessao.txt`.

2. **Gravar uma sessão e anexar a um arquivo existente:**

   ```csh
   script -a sessao_existente.txt
   ```

   Com este comando, a nova sessão será adicionada ao final de `sessao_existente.txt`.

3. **Executar em modo silencioso:**

   ```csh
   script -q sessao_silenciosa.txt
   ```

   Este comando grava a sessão em `sessao_silenciosa.txt` sem exibir mensagens de início e término.

4. **Gravar o tempo da sessão:**

   ```csh
   script -t tempo.txt sessao_tempo.txt
   ```

   Aqui, o tempo de execução da sessão será gravado em `tempo.txt`, enquanto a saída da sessão será salva em `sessao_tempo.txt`.

## Tips
- Sempre verifique o conteúdo do arquivo gravado após a sessão para garantir que tudo foi registrado corretamente.
- Use o modo silencioso (`-q`) se você não quiser distrações visuais enquanto grava a sessão.
- Considere usar a opção de anexar (`-a`) se você estiver realizando várias sessões e quiser manter um registro contínuo.