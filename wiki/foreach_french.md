# [Unix] C Shell (csh) foreach utilisation : Exécute une commande pour chaque élément d'une liste

## Overview
La commande `foreach` dans C Shell (csh) permet d'exécuter une série de commandes pour chaque élément d'une liste. C'est un outil puissant pour automatiser des tâches répétitives en itérant sur des éléments.

## Usage
La syntaxe de base de la commande `foreach` est la suivante :

```csh
foreach variable (liste)
    commande
end
```

## Common Options
La commande `foreach` n'a pas de nombreuses options comme d'autres commandes, mais voici quelques points à considérer :
- `variable` : Nom de la variable qui prendra la valeur de chaque élément de la liste à chaque itération.
- `liste` : Une liste d'éléments sur lesquels itérer.

## Common Examples

### Exemple 1 : Afficher des noms de fichiers
```csh
foreach file (*.txt)
    echo $file
end
```
Cet exemple affiche tous les fichiers avec l'extension `.txt` dans le répertoire courant.

### Exemple 2 : Compresser plusieurs fichiers
```csh
foreach file (*.log)
    gzip $file
end
```
Ici, tous les fichiers avec l'extension `.log` sont compressés en utilisant `gzip`.

### Exemple 3 : Renommer des fichiers
```csh
foreach file (file1.txt file2.txt file3.txt)
    mv $file ${file:r}.bak
end
```
Cet exemple renomme `file1.txt`, `file2.txt`, et `file3.txt` en ajoutant l'extension `.bak`.

## Tips
- Utilisez des glob patterns pour sélectionner des fichiers spécifiques dans votre liste.
- Soyez prudent avec les commandes destructrices comme `rm` ; vérifiez toujours la liste d'éléments avant d'exécuter des commandes qui pourraient supprimer des fichiers.
- Vous pouvez imbriquer des boucles `foreach` pour des tâches plus complexes, mais cela peut rendre le script plus difficile à lire.