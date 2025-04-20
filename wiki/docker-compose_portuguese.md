# [Linux] C Shell (csh) docker-compose uso: Gerenciar aplicações Docker com múltiplos contêineres

## Overview
O comando `docker-compose` é uma ferramenta que permite definir e executar aplicações Docker compostas por múltiplos contêineres. Com um arquivo de configuração, geralmente chamado `docker-compose.yml`, você pode especificar os serviços, redes e volumes necessários para sua aplicação, facilitando a orquestração e o gerenciamento dos contêineres.

## Usage
A sintaxe básica do comando `docker-compose` é a seguinte:

```bash
docker-compose [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `docker-compose`:

- `up`: Cria e inicia os contêineres definidos no arquivo `docker-compose.yml`.
- `down`: Para e remove os contêineres, redes e volumes criados pelo `up`.
- `build`: Constrói ou reconstrói os serviços definidos no arquivo.
- `logs`: Exibe os logs dos contêineres em execução.
- `ps`: Lista os contêineres em execução e seus estados.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `docker-compose`:

1. **Iniciar os serviços definidos:**
   ```bash
   docker-compose up
   ```

2. **Iniciar os serviços em segundo plano (modo detached):**
   ```bash
   docker-compose up -d
   ```

3. **Parar e remover os contêineres:**
   ```bash
   docker-compose down
   ```

4. **Construir os serviços antes de iniciar:**
   ```bash
   docker-compose up --build
   ```

5. **Exibir logs dos serviços:**
   ```bash
   docker-compose logs
   ```

6. **Listar os contêineres em execução:**
   ```bash
   docker-compose ps
   ```

## Tips
- Sempre verifique se o arquivo `docker-compose.yml` está corretamente configurado antes de executar o comando `up`.
- Utilize o modo detached (`-d`) para executar os contêineres em segundo plano, permitindo que você continue usando o terminal.
- Para depuração, use o comando `logs` para visualizar a saída dos contêineres e identificar possíveis problemas.
- Mantenha seu arquivo `docker-compose.yml` organizado e documentado para facilitar a manutenção e a colaboração com outros desenvolvedores.