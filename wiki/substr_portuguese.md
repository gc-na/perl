<!--
Meta Description: # Substr: Extraindo Substrings em Perl ## Sinopse O comando `substr` em Perl é uma função poderosa utilizada para extrair partes específicas de string...
Meta Keywords: string, substr, perl, uma, substring
-->

# Substr: Extraindo Substrings em Perl

## Sinopse
O comando `substr` em Perl é uma função poderosa utilizada para extrair partes específicas de strings. Ele permite manipulações eficientes e precisas de substrings em variáveis.

## Documentação
A função `substr` em Perl é utilizada para acessar ou modificar uma parte de uma string. A sintaxe básica é a seguinte:

```perl
substr STRING, OFFSET, LENGTH, REPLACEMENT
```

- **STRING**: A string original da qual a substring será extraída.
- **OFFSET**: A posição inicial (zero-based) a partir da qual a substring será extraída.
- **LENGTH**: (Opcional) O número de caracteres a serem extraídos. Se omitido, a substring será extraída até o final da string.
- **REPLACEMENT**: (Opcional) Um valor que pode ser usado para substituir a substring especificada.

### Exemplo de Uso
Aqui estão alguns exemplos básicos para ilustrar o uso da função `substr`:

1. **Extraindo uma Substring:**
   ```perl
   my $string = "Olá, Mundo!";
   my $sub = substr($string, 5, 6); # Extrai "Mundo!"
   print $sub; # Saída: Mundo!
   ```

2. **Modificando uma Substring:**
   ```perl
   my $string = "Olá, Mundo!";
   substr($string, 5, 6, "Planeta"); # Substitui "Mundo!" por "Planeta"
   print $string; # Saída: Olá, Planeta!
   ```

3. **Extraindo até o final da String:**
   ```perl
   my $string = "Perl é divertido!";
   my $sub = substr($string, 5); # Extrai "é divertido!"
   print $sub; # Saída: é divertido!
   ```

## Explicação
Embora `substr` seja bastante útil, existem alguns pontos importantes a serem considerados:

- **Offset Baseado em Zero**: Lembre-se de que o índice começa em zero. Portanto, um `OFFSET` de 0 refere-se ao primeiro caractere da string.
  
- **LENGTH Negativo**: Se o `LENGTH` for negativo, a função considerará o valor como a contagem de caracteres a partir do final da string, o que pode causar confusão se não for bem compreendido.

- **Strings Imutáveis**: Em Perl, as strings são imutáveis. Isso significa que, ao modificar uma substring, você está criando uma nova versão da string, e não alterando a string original.

- **Cuidado com o Tipo de Dados**: Ao usar `substr`, assegure-se de que a variável é uma string. O uso em outros tipos de dados pode levar a erros inesperados.

## Resumo em Uma Linha
A função `substr` em Perl é utilizada para extrair ou modificar partes específicas de strings de forma eficiente e versátil.