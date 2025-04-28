<!--
Meta Description: # El Comando "import" en Perl: Guía Completa ## Sinopsis El comando `import` en Perl es una herramienta fundamental que permite a los módulos exportar...
Meta Keywords: funciones, import, módulo, mimodulo, use
-->

# El Comando "import" en Perl: Guía Completa

## Sinopsis
El comando `import` en Perl es una herramienta fundamental que permite a los módulos exportar funciones y variables a otros espacios de nombres, facilitando la reutilización del código y la organización de los mismos.

## Documentación
### Propósito
El comando `import` se utiliza en Perl para facilitar la inclusión de funciones y variables de un módulo en el espacio de nombres de un script o de otro módulo. Esto permite que el código sea más limpio y que las funciones sean accesibles sin necesidad de prefijar el nombre del módulo.

### Uso
Para utilizar `import`, generalmente se define en el módulo que se desea exportar. Por ejemplo, al crear un módulo, puedes especificar qué funciones o variables deseas exportar al utilizar el comando `Exporter`.

```perl
package MiModulo;
use Exporter 'import';
our @EXPORT = qw(funcion1 funcion2);
```

En este caso, `funcion1` y `funcion2` estarán disponibles para cualquier script que use `MiModulo`.

### Detalles
- **@EXPORT**: Esta variable contiene una lista de nombres de funciones o variables a exportar por defecto.
- **@EXPORT_OK**: Permite exportar funciones opcionalmente. Los usuarios pueden elegir qué funciones importar.
- **import**: Se llama automáticamente cuando un módulo es utilizado con `use`.

## Ejemplos
### Ejemplo básico de uso de `import`
```perl
# MiModulo.pm
package MiModulo;
use Exporter 'import';
our @EXPORT = qw(saludo);

sub saludo {
    return "¡Hola, mundo!";
}

1; # Fin del módulo

# script.pl
use MiModulo;
print saludo(); # Salida: ¡Hola, mundo!
```

### Ejemplo de uso de `@EXPORT_OK`
```perl
# MiModulo.pm
package MiModulo;
use Exporter 'import';
our @EXPORT_OK = qw(funcion1);

sub funcion1 {
    return "Función 1 ejecutada";
}

1; # Fin del módulo

# script.pl
use MiModulo qw(funcion1);
print funcion1(); # Salida: Función 1 ejecutada
```

## Explicación
### Errores Comunes
- **No incluir el módulo**: Si olvidas incluir el módulo con `use MiModulo;`, no podrás acceder a las funciones exportadas.
- **Conflictos de nombres**: Si dos módulos exportan funciones con el mismo nombre, puede haber confusión. Es recomendable utilizar `@EXPORT_OK` para evitar conflictos.

### Notas Adicionales
- Siempre es buena práctica documentar qué funciones se exportan y cómo se deben usar.
- Considera el uso de `:tag` para agrupar funciones relacionadas y facilitar su importación.

## Resumen en una línea
El comando `import` en Perl permite a los módulos exportar funciones y variables a otros espacios de nombres, mejorando la organización y reutilización del código.