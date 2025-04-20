# [Linux] C Shell (csh) sqlite3 Uso: Interagir com bancos de dados SQLite

## Overview
O comando `sqlite3` é uma interface de linha de comando para o banco de dados SQLite. Ele permite que os usuários criem, modifiquem e consultem bancos de dados SQLite de forma interativa ou através de scripts.

## Usage
A sintaxe básica do comando `sqlite3` é a seguinte:

```bash
sqlite3 [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `sqlite3`:

- `-init <arquivo>`: Executa comandos SQL a partir do arquivo especificado ao iniciar.
- `-batch`: Executa em modo batch, sem interação com o usuário.
- `-header`: Exibe os nomes das colunas no resultado das consultas.
- `-version`: Mostra a versão do SQLite.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `sqlite3`:

1. **Criar um novo banco de dados:**

```bash
sqlite3 meu_banco.db
```

2. **Executar um script SQL a partir de um arquivo:**

```bash
sqlite3 meu_banco.db -init script.sql
```

3. **Consultar dados de uma tabela:**

```bash
sqlite3 meu_banco.db "SELECT * FROM minha_tabela;"
```

4. **Exportar dados para um arquivo CSV:**

```bash
sqlite3 -header -csv meu_banco.db "SELECT * FROM minha_tabela;" > dados.csv
```

5. **Mostrar a versão do SQLite:**

```bash
sqlite3 -version
```

## Tips
- Sempre faça backup do seu banco de dados antes de realizar operações destrutivas.
- Utilize o modo `-batch` para executar scripts automaticamente sem interação.
- Use `-header` para facilitar a leitura dos resultados das consultas.
- Explore a documentação do SQLite para aprender sobre funções e comandos SQL avançados.