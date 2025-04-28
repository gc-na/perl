<!--
Meta Description: # substr en Perl: Función para Extraer Subcadenas ## Sinopsis La función `substr` en Perl permite extraer una subcadena de una cadena dada, facilitand...
Meta Keywords: cadena, perl, substr, subcadena, una
-->

# substr en Perl: Función para Extraer Subcadenas

## Sinopsis
La función `substr` en Perl permite extraer una subcadena de una cadena dada, facilitando la manipulación de texto y el procesamiento de cadenas.

## Documentación
La función `substr` se utiliza para obtener una parte específica de una cadena. Su sintaxis básica es:

```perl
substr($cadena, $inicio, $longitud, $nuevo_valor);
```

### Parámetros:
- **$cadena**: La cadena original de la cual se extraerá la subcadena.
- **$inicio**: La posición inicial (basada en 0) desde la cual se comenzará a extraer.
- **$longitud**: (Opcional) La cantidad de caracteres a extraer. Si no se especifica, se extraerá desde el inicio hasta el final de la cadena.
- **$nuevo_valor**: (Opcional) Si se proporciona, reemplazará la subcadena extraída con este nuevo valor.

### Retorno:
Devuelve la subcadena extraída. Si se proporciona un nuevo valor, devuelve el valor modificado de la cadena original.

## Ejemplos

### Ejemplo Básico:
```perl
my $cadena = "Hola, mundo!";
my $subcadena = substr($cadena, 0, 4);
print $subcadena;  # Salida: Hola
```

### Ejemplo con Reemplazo:
```perl
my $cadena = "Perl es genial";
substr($cadena, 5, 2, "maravilloso");
print $cadena;  # Salida: Perl es maravilloso
```

### Ejemplo sin Longitud Especificada:
```perl
my $cadena = "Programación en Perl";
my $subcadena = substr($cadena, 5);
print $subcadena;  # Salida: ración en Perl
```

## Explicación
Un error común al usar `substr` es no considerar que el índice de inicio es cero basado. Esto significa que el primer carácter de la cadena se encuentra en la posición 0. Otro punto a tener en cuenta es que si el índice de inicio es mayor que la longitud de la cadena, se devolverá una cadena vacía.

Además, al usar el parámetro `$nuevo_valor`, la longitud de la cadena original puede cambiar, lo que afecta al índice de cualquier operación posterior que dependa de la longitud inicial.

## Resumen en Una Línea
La función `substr` en Perl permite extraer y manipular subcadenas de una cadena original de forma eficiente.