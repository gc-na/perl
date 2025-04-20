# [Linux] C Shell (csh) expr : Évaluer des expressions

## Overview
La commande `expr` est utilisée dans le C Shell pour évaluer des expressions et effectuer des opérations arithmétiques, des comparaisons et des manipulations de chaînes. Elle renvoie le résultat de l'évaluation, ce qui en fait un outil utile pour les scripts et les opérations en ligne de commande.

## Usage
La syntaxe de base de la commande `expr` est la suivante :

```csh
expr [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `expr` :

- `+` : Additionne deux nombres.
- `-` : Soustrait le deuxième nombre du premier.
- `*` : Multiplie deux nombres.
- `/` : Divise le premier nombre par le deuxième.
- `%` : Renvoie le reste de la division du premier nombre par le deuxième.
- `=` : Évalue l'égalité entre deux expressions.
- `!=` : Évalue l'inégalité entre deux expressions.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `expr` :

1. **Addition de deux nombres :**

```csh
set result = `expr 5 + 3`
echo $result  # Affiche 8
```

2. **Soustraction :**

```csh
set result = `expr 10 - 4`
echo $result  # Affiche 6
```

3. **Multiplication :**

```csh
set result = `expr 7 \* 6`
echo $result  # Affiche 42
```

4. **Division :**

```csh
set result = `expr 20 / 4`
echo $result  # Affiche 5
```

5. **Reste de la division :**

```csh
set result = `expr 10 % 3`
echo $result  # Affiche 1
```

6. **Comparaison d'égalité :**

```csh
set is_equal = `expr 5 = 5`
echo $is_equal  # Affiche 1 (vrai)
```

7. **Comparaison d'inégalité :**

```csh
set is_not_equal = `expr 5 != 3`
echo $is_not_equal  # Affiche 1 (vrai)
```

## Tips
- N'oubliez pas d'échapper l'astérisque (`*`) avec un antislash (`\`) pour éviter que le shell ne l'interprète comme un caractère générique.
- Utilisez des guillemets autour des expressions pour éviter les erreurs de syntaxe, surtout si elles contiennent des espaces.
- `expr` peut être moins performant que d'autres méthodes pour des calculs plus complexes, envisagez d'utiliser des langages de script comme Perl ou Python si nécessaire.