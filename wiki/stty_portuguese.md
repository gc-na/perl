# [Linux] C Shell (csh) stty: Configurar opções do terminal

## Overview
O comando `stty` é utilizado para modificar e exibir as configurações do terminal. Ele permite que os usuários ajustem como o terminal se comporta, como a manipulação de caracteres, controle de fluxo e outras opções relacionadas à entrada e saída.

## Usage
A sintaxe básica do comando `stty` é a seguinte:

```bash
stty [opções] [argumentos]
```

## Common Options
- `-a`: Exibe todas as configurações atuais do terminal.
- `-g`: Exibe as configurações atuais em um formato que pode ser usado como argumento para `stty`.
- `erase <caractere>`: Define o caractere de exclusão.
- `kill <caractere>`: Define o caractere de finalização da linha.
- `intr <caractere>`: Define o caractere de interrupção.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `stty`:

1. **Exibir todas as configurações do terminal:**
   ```bash
   stty -a
   ```

2. **Definir o caractere de exclusão como `^H`:**
   ```bash
   stty erase ^H
   ```

3. **Definir o caractere de finalização da linha como `^U`:**
   ```bash
   stty kill ^U
   ```

4. **Exibir as configurações atuais em um formato utilizável:**
   ```bash
   stty -g
   ```

5. **Definir o caractere de interrupção como `^C`:**
   ```bash
   stty intr ^C
   ```

## Tips
- Sempre verifique as configurações atuais do terminal antes de fazer alterações, usando `stty -a`.
- Use `stty -g` para salvar as configurações atuais, permitindo que você as restaure mais tarde.
- Tenha cuidado ao alterar caracteres de controle, pois isso pode afetar a maneira como você interage com o terminal.