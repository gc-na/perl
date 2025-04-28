<!--
Meta Description: # Subrutinas en Perl: Uso y Ejemplos de la Palabra Clave "sub" ## Sinopsis La palabra clave `sub` en Perl se utiliza para definir subrutinas, que son ...
Meta Keywords: que, subrutinas, perl, código, sub
-->

# Subrutinas en Perl: Uso y Ejemplos de la Palabra Clave "sub"

## Sinopsis
La palabra clave `sub` en Perl se utiliza para definir subrutinas, que son bloques de código reutilizables que pueden ser llamados en diferentes partes del programa, facilitando la organización y modularidad del código.

## Documentación
### Propósito
Las subrutinas en Perl permiten encapsular lógica y funcionalidad en una unidad que puede ser invocada múltiples veces, lo que ayuda a evitar la repetición de código y mejora la legibilidad.

### Uso
Para definir una subrutina, se utiliza la palabra clave `sub`, seguida del nombre de la subrutina y un bloque de código. La sintaxis básica es la siguiente:

```perl
sub nombre_sub {
    # Código de la subrutina
}
```

Para llamar a una subrutina, simplemente se utiliza su nombre seguido de paréntesis:

```perl
nombre_sub();
```

### Detalles
- **Parámetros**: Las subrutinas pueden aceptar parámetros pasados a través de la lista `@_`, que es una variable especial que contiene todos los argumentos enviados a la subrutina.
- **Valor de retorno**: Para devolver un valor, se utiliza la función `return`, aunque Perl automáticamente devuelve el valor de la última expresión evaluada si no se especifica un `return`.
- **Alcance**: Las subrutinas pueden ser llamadas dentro de su propio bloque de código, así como desde otros bloques, lo que permite una gran flexibilidad.

## Ejemplos
### Ejemplo Básico de Definición y Llamada
```perl
sub saludar {
    my ($nombre) = @_;
    print "Hola, $nombre!\n";
}

saludar("Juan");  # Salida: Hola, Juan!
```

### Ejemplo con Valor de Retorno
```perl
sub suma {
    my ($a, $b) = @_;
    return $a + $b;
}

my $resultado = suma(5, 7);
print "La suma es: $resultado\n";  # Salida: La suma es: 12
```

## Explicación
Al trabajar con subrutinas, es importante tener en cuenta algunos aspectos:

- **Contexto**: Las subrutinas pueden comportarse de manera diferente dependiendo del contexto en el que se llamen (escalares o listas).
- **Escalabilidad**: Asegúrate de que los nombres de las subrutinas sean únicos para evitar conflictos y facilitar la escalabilidad del código.
- **Uso de `my`**: Es recomendable declarar variables locales dentro de las subrutinas utilizando `my` para evitar interferencias con variables globales.

## Resumen en Una Línea
La palabra clave `sub` en Perl permite definir subrutinas, que son bloques de código reutilizables que mejoran la modularidad y la organización del código.