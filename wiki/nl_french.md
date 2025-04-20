# [Linux] C Shell (csh) nl : numéroter les lignes d'un fichier

## Overview
La commande `nl` est utilisée pour numéroter les lignes d'un fichier texte. Elle permet d'ajouter des numéros de ligne à chaque ligne du fichier, ce qui peut être utile pour la lecture ou la référence.

## Usage
La syntaxe de base de la commande `nl` est la suivante :

```csh
nl [options] [arguments]
```

## Common Options
Voici quelques options courantes de la commande `nl` :

- `-b` : Définit la méthode de numérotation des lignes (par exemple, `-b a` pour numéroter toutes les lignes).
- `-f` : Ignore les lignes vides lors de la numérotation.
- `-n` : Définit le format de numérotation (par exemple, `-n ln` pour un numéro de ligne à gauche).
- `-w` : Définit la largeur du numéro de ligne.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `nl` :

1. Numéroter toutes les lignes d'un fichier :

   ```csh
   nl fichier.txt
   ```

2. Numéroter uniquement les lignes non vides :

   ```csh
   nl -f fichier.txt
   ```

3. Utiliser un format de numérotation spécifique :

   ```csh
   nl -n ln -w 3 fichier.txt
   ```

4. Numéroter toutes les lignes avec des numéros à droite :

   ```csh
   nl -n rn fichier.txt
   ```

## Tips
- Utilisez l'option `-b` pour contrôler quelles lignes sont numérotées selon vos besoins.
- Combinez `nl` avec d'autres commandes comme `grep` pour filtrer le contenu avant la numérotation.
- Pensez à rediriger la sortie vers un nouveau fichier si vous souhaitez conserver le résultat :

   ```csh
   nl fichier.txt > fichier_numéroté.txt
   ```