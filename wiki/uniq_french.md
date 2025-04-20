# [Linux] C Shell (csh) uniq Utilisation : Filtrer les lignes uniques d'un fichier

## Overview
La commande `uniq` est utilisée pour filtrer les lignes uniques d'un fichier ou d'une entrée standard. Elle supprime les lignes en double consécutives, ce qui permet d'obtenir une liste de lignes distinctes.

## Usage
La syntaxe de base de la commande `uniq` est la suivante :

```shell
uniq [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `uniq` :

- `-c` : Compte le nombre d'occurrences de chaque ligne.
- `-d` : Affiche uniquement les lignes qui apparaissent plus d'une fois.
- `-u` : Affiche uniquement les lignes qui apparaissent une seule fois.
- `-i` : Ignore la casse lors de la comparaison des lignes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `uniq` :

1. **Filtrer les lignes uniques d'un fichier :**
   ```shell
   uniq fichier.txt
   ```

2. **Compter les occurrences de chaque ligne :**
   ```shell
   uniq -c fichier.txt
   ```

3. **Afficher uniquement les lignes dupliquées :**
   ```shell
   uniq -d fichier.txt
   ```

4. **Afficher uniquement les lignes uniques :**
   ```shell
   uniq -u fichier.txt
   ```

5. **Ignorer la casse lors de la comparaison :**
   ```shell
   uniq -i fichier.txt
   ```

## Tips
- Assurez-vous que le fichier d'entrée est trié avant d'utiliser `uniq`, car il ne supprime que les doublons consécutifs.
- Vous pouvez combiner `uniq` avec d'autres commandes comme `sort` pour obtenir des résultats plus complets. Par exemple :
  ```shell
  sort fichier.txt | uniq
  ```
- Utilisez l'option `-c` pour avoir un aperçu rapide des occurrences, ce qui peut être utile pour analyser des données.