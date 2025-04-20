# [Linux] C Shell (csh) if : Exécuter des commandes conditionnelles

## Overview
La commande `if` dans C Shell (csh) permet d'exécuter des commandes en fonction d'une condition. Si la condition est vraie, les commandes spécifiées sont exécutées.

## Usage
La syntaxe de base de la commande `if` est la suivante :

```csh
if (condition) then
    commandes
endif
```

## Common Options
- `then` : Indique le début des commandes à exécuter si la condition est vraie.
- `endif` : Marque la fin de la structure conditionnelle.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `if` :

### Exemple 1 : Vérifier si un fichier existe
```csh
if (-e monfichier.txt) then
    echo "Le fichier existe."
endif
```

### Exemple 2 : Vérifier si une variable est vide
```csh
set maVariable = ""
if ("$maVariable" == "") then
    echo "La variable est vide."
endif
```

### Exemple 3 : Comparer des nombres
```csh
set a = 5
set b = 10
if ($a < $b) then
    echo "$a est inférieur à $b."
endif
```

## Tips
- Utilisez des parenthèses pour encadrer la condition afin d'améliorer la lisibilité.
- N'oubliez pas de toujours terminer une structure `if` par `endif` pour éviter les erreurs de syntaxe.
- Testez vos conditions avec des commandes simples avant de les intégrer dans des scripts plus complexes.