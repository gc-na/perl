# [Linux] C Shell (csh) wget Uso: Ferramenta para download de arquivos da web

## Overview
O comando `wget` é uma ferramenta de linha de comando utilizada para baixar arquivos da web. Ele suporta protocolos como HTTP, HTTPS e FTP, permitindo que os usuários façam downloads de forma simples e eficiente.

## Usage
A sintaxe básica do comando `wget` é a seguinte:

```bash
wget [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `wget`:

- `-O <arquivo>`: Especifica o nome do arquivo de saída.
- `-c`: Continua um download interrompido.
- `-q`: Executa o comando em modo silencioso, sem exibir mensagens.
- `--limit-rate=<taxa>`: Limita a taxa de download a um valor específico.
- `-r`: Ativa o download recursivo, permitindo baixar diretórios inteiros.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `wget`:

1. **Baixar um único arquivo:**
   ```bash
   wget http://exemplo.com/arquivo.zip
   ```

2. **Baixar um arquivo e renomeá-lo:**
   ```bash
   wget -O novo_nome.zip http://exemplo.com/arquivo.zip
   ```

3. **Continuar um download interrompido:**
   ```bash
   wget -c http://exemplo.com/arquivo.zip
   ```

4. **Baixar um site inteiro de forma recursiva:**
   ```bash
   wget -r http://exemplo.com
   ```

5. **Limitar a taxa de download:**
   ```bash
   wget --limit-rate=200k http://exemplo.com/arquivo.zip
   ```

## Tips
- Sempre verifique a URL antes de iniciar o download para evitar arquivos indesejados.
- Utilize a opção `-q` para downloads em scripts, onde você não precisa de mensagens de status.
- Para downloads de sites grandes, considere usar a opção `-r` com cautela, pois pode consumir muito espaço em disco e largura de banda.