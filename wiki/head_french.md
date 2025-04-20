# [Linux] C Shell (csh) head : afficher les premières lignes d'un fichier

## Overview
La commande `head` est utilisée pour afficher les premières lignes d'un fichier texte. Par défaut, elle montre les dix premières lignes, mais cela peut être modifié en utilisant des options.

## Usage
Voici la syntaxe de base de la commande `head` :

```csh
head [options] [arguments]
```

## Common Options
- `-n [nombre]` : Spécifie le nombre de lignes à afficher. Par exemple, `-n 5` affichera les cinq premières lignes.
- `-q` : Supprime l'en-tête des fichiers multiples lors de l'affichage.
- `-v` : Affiche l'en-tête des fichiers multiples.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `head` :

1. Afficher les dix premières lignes d'un fichier :
   ```csh
   head fichier.txt
   ```

2. Afficher les cinq premières lignes d'un fichier :
   ```csh
   head -n 5 fichier.txt
   ```

3. Afficher les premières lignes de plusieurs fichiers :
   ```csh
   head fichier1.txt fichier2.txt
   ```

4. Afficher les trois premières lignes d'un fichier sans l'en-tête :
   ```csh
   head -q -n 3 fichier1.txt fichier2.txt
   ```

## Tips
- Utilisez `head` en combinaison avec d'autres commandes, comme `grep`, pour filtrer et afficher les résultats pertinents.
- Pensez à rediriger la sortie de `head` vers un autre fichier si vous souhaitez conserver les lignes affichées :
  ```csh
  head -n 10 fichier.txt > premier_dix_lignes.txt
  ```
- Pour une visualisation rapide, `head` est utile pour vérifier le contenu d'un fichier sans l'ouvrir complètement.