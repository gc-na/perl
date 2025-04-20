# [Linux] C Shell (csh) du : Afficher l'utilisation de l'espace disque

## Overview
La commande `du` (Disk Usage) est utilisée pour estimer et afficher l'utilisation de l'espace disque des fichiers et des répertoires dans un système de fichiers. Elle permet aux utilisateurs de comprendre combien d'espace est occupé par des fichiers spécifiques ou des répertoires entiers.

## Usage
La syntaxe de base de la commande `du` est la suivante :

```csh
du [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `du` :

- `-h` : Affiche la taille dans un format lisible par l'homme (par exemple, Ko, Mo, Go).
- `-s` : Affiche uniquement le total pour chaque argument, sans afficher les sous-répertoires.
- `-a` : Inclut les fichiers dans la sortie, pas seulement les répertoires.
- `-c` : Affiche un total cumulatif à la fin de la sortie.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `du` :

1. Afficher l'utilisation de l'espace disque d'un répertoire spécifique :

   ```csh
   du /chemin/vers/repertoire
   ```

2. Afficher l'utilisation de l'espace disque dans un format lisible par l'homme :

   ```csh
   du -h /chemin/vers/repertoire
   ```

3. Afficher uniquement le total pour un répertoire :

   ```csh
   du -sh /chemin/vers/repertoire
   ```

4. Inclure les fichiers dans la sortie :

   ```csh
   du -ah /chemin/vers/repertoire
   ```

5. Afficher un total cumulatif pour plusieurs répertoires :

   ```csh
   du -c /chemin/vers/repertoire1 /chemin/vers/repertoire2
   ```

## Tips
- Utilisez l'option `-h` pour rendre les résultats plus compréhensibles, surtout si vous travaillez avec de grandes quantités de données.
- Combinez l'option `-s` avec d'autres options pour obtenir un aperçu rapide de l'utilisation de l'espace sans détails superflus.
- Pensez à utiliser `du` avec `sort` pour trier les résultats par taille, par exemple :

  ```csh
  du -h /chemin/vers/repertoire | sort -h
  ``` 

Ces conseils vous aideront à mieux gérer et comprendre l'utilisation de l'espace disque sur votre système.