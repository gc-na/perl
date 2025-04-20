# [Linux] C Shell (csh) diff : Comparer les fichiers

## Overview
La commande `diff` est utilisée pour comparer le contenu de deux fichiers ou plus. Elle affiche les différences entre ces fichiers ligne par ligne, ce qui est particulièrement utile pour les développeurs et les rédacteurs qui souhaitent suivre les modifications apportées à des fichiers texte.

## Usage
La syntaxe de base de la commande `diff` est la suivante :

```csh
diff [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `diff` :

- `-u` : Affiche les différences en format unifié, ce qui rend la sortie plus lisible.
- `-c` : Affiche les différences en format contextuel, fournissant un contexte autour des changements.
- `-i` : Ignore la casse lors de la comparaison des fichiers.
- `-w` : Ignore les espaces blancs lors de la comparaison.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `diff` :

1. Comparer deux fichiers texte :

   ```csh
   diff fichier1.txt fichier2.txt
   ```

2. Afficher les différences en format unifié :

   ```csh
   diff -u fichier1.txt fichier2.txt
   ```

3. Comparer deux répertoires :

   ```csh
   diff -r repertoire1/ repertoire2/
   ```

4. Ignorer les espaces blancs :

   ```csh
   diff -w fichier1.txt fichier2.txt
   ```

## Tips
- Utilisez l'option `-u` pour obtenir une sortie plus facile à lire, surtout lors de la révision des modifications.
- Pour sauvegarder les différences dans un fichier, vous pouvez rediriger la sortie :

  ```csh
  diff fichier1.txt fichier2.txt > differences.txt
  ```

- Pensez à utiliser `diff` avec des outils de contrôle de version comme `git` pour suivre les modifications dans votre code.