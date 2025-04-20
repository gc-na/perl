# [Unix] C Shell (csh) @ Utilisation : Exécute des opérations arithmétiques

## Overview
La commande `@` dans C Shell (csh) est utilisée pour effectuer des opérations arithmétiques simples sur des variables. Elle permet d'assigner des valeurs numériques à des variables et d'effectuer des calculs directement dans le shell.

## Usage
La syntaxe de base de la commande `@` est la suivante :

```csh
@ [options] [arguments]
```

## Common Options
La commande `@` ne possède pas d'options spécifiques, mais elle est souvent utilisée avec des opérations arithmétiques telles que :

- `=` : pour assigner une valeur à une variable.
- `+` : pour additionner des valeurs.
- `-` : pour soustraire des valeurs.
- `*` : pour multiplier des valeurs.
- `/` : pour diviser des valeurs.

## Common Examples

Voici quelques exemples pratiques de l'utilisation de la commande `@` :

### Exemple 1 : Addition
```csh
set a = 5
@ a = a + 3
echo $a  # Affiche 8
```

### Exemple 2 : Soustraction
```csh
set b = 10
@ b = b - 4
echo $b  # Affiche 6
```

### Exemple 3 : Multiplication
```csh
set c = 2
@ c = c * 5
echo $c  # Affiche 10
```

### Exemple 4 : Division
```csh
set d = 20
@ d = d / 4
echo $d  # Affiche 5
```

### Exemple 5 : Opérations combinées
```csh
set e = 10
@ e = e + 2 * 3
echo $e  # Affiche 16
```

## Tips
- Assurez-vous que les variables sont définies avant d'effectuer des opérations arithmétiques.
- Utilisez des parenthèses pour contrôler l'ordre des opérations, par exemple : `@ result = (a + b) * c`.
- Rappelez-vous que la commande `@` ne gère que les entiers. Pour les calculs à virgule flottante, envisagez d'utiliser des outils comme `bc`.