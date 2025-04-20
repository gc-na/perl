# [Linux] C Shell (csh) cal <Uso equivalente en español>: Muestra un calendario

## Overview
El comando `cal` se utiliza para mostrar un calendario en la terminal. Permite visualizar el calendario de un mes específico o de un año completo, facilitando la consulta de fechas.

## Usage
La sintaxis básica del comando es la siguiente:

```csh
cal [opciones] [argumentos]
```

## Common Options
- `-m`: Muestra el calendario comenzando por lunes.
- `-y`: Muestra el calendario del año actual.
- `-3`: Muestra el mes actual y los meses anterior y siguiente.
- `-j`: Muestra el calendario con los días del año.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `cal`:

1. Mostrar el calendario del mes actual:
   ```csh
   cal
   ```

2. Mostrar el calendario de un mes específico (por ejemplo, marzo de 2023):
   ```csh
   cal 03 2023
   ```

3. Mostrar el calendario del año actual:
   ```csh
   cal -y
   ```

4. Mostrar el calendario de tres meses (el mes actual, el anterior y el siguiente):
   ```csh
   cal -3
   ```

5. Mostrar el calendario con los días del año (por ejemplo, para 2023):
   ```csh
   cal -j 2023
   ```

## Tips
- Utiliza la opción `-m` si prefieres que la semana comience el lunes, lo cual es común en muchos países.
- Combina opciones para personalizar la salida según tus necesidades, como `cal -3 -m`.
- Recuerda que puedes usar el comando `man cal` para obtener más información sobre las opciones disponibles y su uso.