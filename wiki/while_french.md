# [Linux] C Shell (csh) while : Exécuter des commandes en boucle

## Overview
La commande `while` dans C Shell (csh) permet d'exécuter un bloc de commandes tant qu'une condition spécifiée est vraie. C'est un outil puissant pour automatiser des tâches répétitives.

## Usage
La syntaxe de base de la commande `while` est la suivante :

```csh
while (condition)
    commande1
    commande2
end
```

## Common Options
La commande `while` n'a pas d'options spécifiques, mais elle fonctionne avec des conditions qui peuvent inclure des expressions logiques ou des tests.

## Common Examples

### Exemple 1 : Compter jusqu'à 5
```csh
set i = 1
while ($i <= 5)
    echo "Compteur : $i"
    @ i++
end
```

### Exemple 2 : Lire des lignes d'un fichier
```csh
set filename = "mon_fichier.txt"
set i = 1
while (1)
    set line = `head -n $i $filename | tail -n 1`
    if ("$line" == "") break
    echo "Ligne $i : $line"
    @ i++
end
```

### Exemple 3 : Boucle infinie avec condition d'arrêt
```csh
set count = 0
while (1)
    echo "Compteur : $count"
    @ count++
    if ($count >= 10) break
end
```

## Tips
- Assurez-vous que la condition de votre boucle finisse par devenir fausse pour éviter les boucles infinies.
- Utilisez des commentaires pour clarifier le but de chaque section de votre boucle.
- Testez vos conditions avec des valeurs simples avant de les utiliser dans des scripts plus complexes.