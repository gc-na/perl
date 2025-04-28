<!--
Meta Description: # Renombrar Archivos en Perl: Cómo Usar la Función rename ## Sinopsis La función `rename` en Perl permite cambiar el nombre de archivos y directorios ...
Meta Keywords: archivo, rename, que, renombrar, perl
-->

# Renombrar Archivos en Perl: Cómo Usar la Función rename

## Sinopsis
La función `rename` en Perl permite cambiar el nombre de archivos y directorios de manera sencilla y eficaz. Esta operación es fundamental en la manipulación de archivos y es parte de las funciones de entrada/salida de Perl.

## Documentación

### Propósito
La función `rename` se utiliza para modificar el nombre de un archivo o directorio existente en el sistema de archivos. Si se proporciona una ruta diferente, también puede mover el archivo a un nuevo directorio.

### Uso
La sintaxis básica de la función `rename` es la siguiente:

```perl
rename($nombre_actual, $nuevo_nombre);
```

- `$nombre_actual`: El nombre actual del archivo o directorio que deseas renombrar.
- `$nuevo_nombre`: El nuevo nombre que deseas asignar al archivo o directorio.

### Detalles
- La función devuelve un valor verdadero (true) si la operación se realiza con éxito; de lo contrario, devuelve falso (false).
- En caso de error, se puede utilizar la variable especial `$!` para obtener información sobre el error que ocurrió durante la operación.
- Es importante tener en cuenta que el archivo o directorio debe existir y que el nuevo nombre no debe estar en uso.

## Ejemplos

### Ejemplo 1: Renombrar un archivo
```perl
use strict;
use warnings;

my $archivo_actual = 'documento.txt';
my $nuevo_archivo = 'documento_renombrado.txt';

if (rename($archivo_actual, $nuevo_archivo)) {
    print "Archivo renombrado con éxito.\n";
} else {
    warn "No se pudo renombrar el archivo: $!\n";
}
```

### Ejemplo 2: Mover y renombrar un archivo
```perl
use strict;
use warnings;

my $archivo_actual = 'documento.txt';
my $nuevo_archivo = '/ruta/nueva/documento_renombrado.txt';

if (rename($archivo_actual, $nuevo_archivo)) {
    print "Archivo movido y renombrado con éxito.\n";
} else {
    warn "No se pudo mover y renombrar el archivo: $!\n";
}
```

## Explicación
Al usar la función `rename`, es crucial asegurarse de que:
- El archivo o directorio que se desea renombrar realmente exista en la ubicación especificada.
- No se esté intentando renombrar a un nombre que ya exista, ya que esto generará un error.
- El script debe tener los permisos necesarios para modificar el archivo o directorio.

Además, se recomienda manejar los errores adecuadamente utilizando `warn` o `die` para notificar al usuario si algo sale mal durante la operación.

## Resumen en una Línea
La función `rename` en Perl permite cambiar el nombre de archivos y directorios de forma eficiente, manejando errores de manera sencilla.