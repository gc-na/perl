# [Linux] C Shell (csh) comm : Comparer des fichiers ligne par ligne

## Overview
La commande `comm` est utilisée pour comparer deux fichiers triés ligne par ligne. Elle affiche les lignes qui sont uniques à chaque fichier ainsi que les lignes qui sont communes aux deux fichiers. Cela permet d'identifier facilement les différences et les similitudes entre les fichiers.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
comm [options] [fichier1] [fichier2]
```

## Common Options
- `-1` : Supprime les lignes qui sont uniquement dans le premier fichier.
- `-2` : Supprime les lignes qui sont uniquement dans le deuxième fichier.
- `-3` : Supprime les lignes qui sont communes aux deux fichiers.
- `-i` : Ignore la casse lors de la comparaison des lignes.

## Common Examples

### Comparer deux fichiers
Pour comparer deux fichiers appelés `fichier1.txt` et `fichier2.txt`, utilisez la commande suivante :

```csh
comm fichier1.txt fichier2.txt
```

### Afficher uniquement les lignes communes
Pour afficher uniquement les lignes qui sont présentes dans les deux fichiers :

```csh
comm -12 fichier1.txt fichier2.txt
```

### Afficher uniquement les lignes uniques à chaque fichier
Pour afficher les lignes qui sont uniquement dans `fichier1.txt` et `fichier2.txt` :

```csh
comm -3 fichier1.txt fichier2.txt
```

### Ignorer la casse
Pour comparer deux fichiers sans tenir compte de la casse :

```csh
comm -i fichier1.txt fichier2.txt
```

## Tips
- Assurez-vous que les fichiers sont triés avant d'utiliser `comm`, car la commande ne fonctionnera pas correctement sur des fichiers non triés.
- Utilisez les options en combinaison pour personnaliser la sortie selon vos besoins.
- Pour des fichiers très volumineux, envisagez d'utiliser `comm` avec des redirections pour enregistrer les résultats dans un nouveau fichier.