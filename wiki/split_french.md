# [Linux] C Shell (csh) split : Diviser des fichiers en morceaux

## Overview
La commande `split` est utilisée pour diviser un fichier en plusieurs parties plus petites. Cela peut être utile pour gérer de grands fichiers ou pour faciliter leur transfert.

## Usage
La syntaxe de base de la commande `split` est la suivante :

```csh
split [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `split` :

- `-l [nombre]` : Divise le fichier en morceaux contenant un nombre spécifié de lignes.
- `-b [taille]` : Divise le fichier en morceaux d'une taille spécifiée (par exemple, `100k` pour 100 Ko).
- `-d` : Utilise des suffixes numériques pour nommer les fichiers résultants au lieu des lettres par défaut.
- `--additional-suffix=[suffixe]` : Ajoute un suffixe supplémentaire aux fichiers divisés.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `split` :

1. Diviser un fichier en morceaux de 100 lignes :
   ```csh
   split -l 100 mon_fichier.txt
   ```

2. Diviser un fichier en morceaux de 1 Mo :
   ```csh
   split -b 1M mon_fichier.txt
   ```

3. Diviser un fichier et utiliser des suffixes numériques :
   ```csh
   split -d -l 50 mon_fichier.txt
   ```

4. Diviser un fichier en morceaux de 500 Ko avec un suffixe personnalisé :
   ```csh
   split -b 500k --additional-suffix=.part mon_fichier.txt mon_fichier_part_
   ```

## Tips
- Vérifiez la taille de votre fichier avant de le diviser pour choisir la taille appropriée des morceaux.
- Utilisez l'option `-d` si vous souhaitez des noms de fichiers plus faciles à trier.
- Pensez à ajouter un suffixe supplémentaire pour mieux identifier les fichiers divisés, surtout si vous divisez plusieurs fichiers.