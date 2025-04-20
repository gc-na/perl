# [Linux] C Shell (csh) basename Utilisation : Extraire le nom de fichier sans le chemin

## Overview
La commande `basename` est utilisée pour extraire le nom d'un fichier à partir d'un chemin complet, en supprimant le répertoire et l'extension de fichier si nécessaire. Cela permet de travailler facilement avec des noms de fichiers dans des scripts ou en ligne de commande.

## Usage
La syntaxe de base de la commande `basename` est la suivante :

```csh
basename [options] [arguments]
```

## Common Options
- `-s, --suffix`: Supprime une suffixe spécifique du nom de fichier.
- `-a, --multiple`: Traite plusieurs chemins en une seule commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `basename` :

1. Extraire le nom de fichier d'un chemin :

```csh
basename /chemin/vers/fichier.txt
```
Sortie :
```
fichier.txt
```

2. Supprimer une extension de fichier :

```csh
basename /chemin/vers/fichier.txt .txt
```
Sortie :
```
fichier
```

3. Traiter plusieurs chemins :

```csh
basename -a /chemin/vers/fichier1.txt /chemin/vers/fichier2.txt
```
Sortie :
```
fichier1.txt
fichier2.txt
```

4. Supprimer un suffixe spécifique :

```csh
basename -s .txt /chemin/vers/fichier.txt
```
Sortie :
```
fichier
```

## Tips
- Utilisez `basename` dans des scripts pour simplifier le traitement des noms de fichiers.
- Combinez `basename` avec d'autres commandes comme `find` pour automatiser la gestion des fichiers.
- Soyez prudent avec les extensions de fichiers, car la suppression d'une extension peut entraîner des noms de fichiers non uniques.