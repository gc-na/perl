<!--
Meta Description: # Uso de "each" en Perl: Iteración sobre Hashes y Arrays ## Sinopsis El comando `each` en Perl es una función que permite iterar sobre los pares clave...
Meta Keywords: each, valor, clave, hash, que
-->

# Uso de "each" en Perl: Iteración sobre Hashes y Arrays

## Sinopsis
El comando `each` en Perl es una función que permite iterar sobre los pares clave-valor de un hash, facilitando la manipulación y el acceso a sus elementos de manera eficiente.

## Documentación
La función `each` se utiliza principalmente con hashes, aunque también puede aplicarse a arrays. Su propósito es devolver la siguiente clave y valor de un hash en cada llamada, lo que la convierte en una herramienta útil en situaciones donde se necesita recorrer todos los elementos de un hash.

### Uso
```perl
while (my ($clave, $valor) = each %hash) {
    # Hacer algo con $clave y $valor
}
```

### Detalles
- **Tipo de dato:** `each` solo se puede usar con hashes o arrays.
- **Estado:** `each` mantiene un estado interno, lo que significa que en cada llamada devolverá el siguiente par clave-valor hasta que no haya más elementos, momento en el cual devolverá `undef`.
- **Reinicio:** Si se quiere reiniciar el recorrido, se debe llamar a `each` nuevamente sobre el hash o array.

## Ejemplos
### Ejemplo 1: Iterar sobre un hash
```perl
my %frutas = (
    'manzana' => 5,
    'naranja' => 10,
    'plátano' => 3,
);

while (my ($clave, $valor) = each %frutas) {
    print "La $clave tiene $valor unidades.\n";
}
```

### Ejemplo 2: Iterar sobre un array
```perl
my @numeros = (10, 20, 30, 40);

while (my ($indice, $valor) = each @numeros) {
    print "El valor en el índice $indice es $valor.\n";
}
```

## Explicación
Al utilizar `each`, es importante tener en cuenta que:
- **No se puede usar después de `keys` o `values` en el mismo hash sin reiniciar el iterador.** Esto puede causar confusiones si se intenta acceder a los elementos de manera no secuencial.
- **El orden de extracción no está garantizado** en hashes, ya que estos no mantienen un orden. Si el orden es crítico, se debe considerar el uso de arrays o de la función `sort`.

## Resumen en una línea
La función `each` en Perl permite iterar sobre los pares clave-valor de un hash, facilitando el acceso y manipulación de sus elementos.