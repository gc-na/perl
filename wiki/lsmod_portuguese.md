# [Linux] C Shell (csh) lsmod Uso: exibir módulos do kernel carregados

## Overview
O comando `lsmod` é utilizado para exibir uma lista dos módulos do kernel que estão atualmente carregados no sistema. Ele fornece informações sobre os módulos, incluindo dependências e uso de memória, permitindo que os usuários monitorem e gerenciem os módulos do kernel de forma eficaz.

## Usage
A sintaxe básica do comando `lsmod` é a seguinte:

```bash
lsmod [opções]
```

## Common Options
Embora o `lsmod` não tenha muitas opções, algumas das mais comuns incluem:

- `-h`, `--help`: Exibe a ajuda do comando.
- `-v`, `--version`: Mostra a versão do comando.

## Common Examples

### Exibir todos os módulos carregados
Para listar todos os módulos do kernel carregados, basta usar o comando sem opções:

```bash
lsmod
```

### Exibir ajuda do comando
Para obter informações sobre como usar o `lsmod`, você pode usar a opção de ajuda:

```bash
lsmod --help
```

### Ver versão do comando
Para verificar a versão do `lsmod` instalada no seu sistema, utilize:

```bash
lsmod --version
```

## Tips
- Utilize `lsmod` em conjunto com outros comandos, como `modinfo`, para obter informações detalhadas sobre um módulo específico.
- Verifique regularmente os módulos carregados para garantir que não haja módulos desnecessários ou potencialmente problemáticos em execução.
- Ao depurar problemas de hardware, o `lsmod` pode ajudar a identificar se os módulos corretos estão carregados para o seu dispositivo.