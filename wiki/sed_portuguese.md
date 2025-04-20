# [Linux] C Shell (csh) sed Uso: Manipulação de texto

## Overview
O comando `sed` (stream editor) é uma ferramenta poderosa para manipulação e transformação de texto em arquivos ou fluxos de dados. Ele permite realizar operações como substituição, inserção e exclusão de linhas de forma não interativa.

## Usage
A sintaxe básica do comando `sed` é a seguinte:

```bash
sed [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `sed`:

- `-e`: Permite adicionar múltiplas expressões de edição.
- `-i`: Edita arquivos no local, ou seja, faz as alterações diretamente no arquivo.
- `-n`: Suprime a saída padrão, permitindo que você controle o que é exibido.
- `s/padrão/substituição/`: Realiza a substituição do padrão pela substituição.

## Common Examples

### Substituir texto em um arquivo
Para substituir a palavra "antigo" por "novo" em um arquivo chamado `exemplo.txt`:

```bash
sed 's/antigo/novo/g' exemplo.txt
```

### Editar um arquivo no local
Para substituir "erro" por "correção" diretamente no arquivo `exemplo.txt`:

```bash
sed -i 's/erro/correção/g' exemplo.txt
```

### Exibir apenas linhas que contêm um padrão
Para mostrar apenas as linhas que contêm a palavra "importante":

```bash
sed -n '/importante/p' exemplo.txt
```

### Remover linhas vazias
Para remover todas as linhas vazias de um arquivo:

```bash
sed '/^$/d' exemplo.txt
```

## Tips
- Sempre faça uma cópia de segurança do seu arquivo antes de usar a opção `-i`, pois as alterações são irreversíveis.
- Use `-n` em conjunto com expressões de impressão para ter um controle mais preciso sobre a saída.
- Teste seus comandos `sed` em um terminal antes de aplicá-los em arquivos importantes para evitar erros indesejados.