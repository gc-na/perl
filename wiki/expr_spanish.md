# [Linux] C Shell (csh) expr Uso: Evaluar expresiones

## Overview
El comando `expr` en C Shell se utiliza para evaluar expresiones aritméticas, lógicas y de cadena. Permite realizar cálculos simples y manipular cadenas de texto en la línea de comandos.

## Usage
La sintaxis básica del comando `expr` es la siguiente:

```csh
expr [opciones] [argumentos]
```

## Common Options
- `length`: Devuelve la longitud de una cadena.
- `index`: Devuelve la posición de la primera aparición de un carácter en una cadena.
- `substr`: Extrae una subcadena de una cadena dada.
- `+`, `-`, `*`, `/`: Operadores aritméticos para sumar, restar, multiplicar y dividir.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `expr`:

### Ejemplo 1: Sumar dos números
```csh
expr 5 + 3
```
Este comando devuelve `8`, que es la suma de 5 y 3.

### Ejemplo 2: Obtener la longitud de una cadena
```csh
expr length "Hola Mundo"
```
Este comando devuelve `10`, que es la longitud de la cadena "Hola Mundo".

### Ejemplo 3: Encontrar la posición de un carácter
```csh
expr index "Hola Mundo" "M"
```
Este comando devuelve `6`, que es la posición de la letra "M" en la cadena.

### Ejemplo 4: Extraer una subcadena
```csh
expr substr "Hola Mundo" 1 4
```
Este comando devuelve `Hola`, que es la subcadena que comienza en la posición 1 y tiene una longitud de 4.

### Ejemplo 5: Multiplicar dos números
```csh
expr 4 \* 5
```
Este comando devuelve `20`, que es el resultado de multiplicar 4 por 5. (Nota: el asterisco debe ser escapado con una barra invertida `\`).

## Tips
- Asegúrate de usar espacios adecuados entre los operadores y los operandos.
- Escapa los operadores especiales como `*` para evitar errores de interpretación.
- Utiliza paréntesis para agrupar operaciones y controlar el orden de evaluación.