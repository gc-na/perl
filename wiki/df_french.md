# [Linux] C Shell (csh) df Utilisation : Afficher l'espace disque disponible

## Overview
La commande `df` est utilisée pour afficher des informations sur l'espace disque disponible et utilisé sur les systèmes de fichiers montés. Elle permet aux utilisateurs de vérifier rapidement l'état de l'espace disque sur leur système.

## Usage
La syntaxe de base de la commande `df` est la suivante :

```csh
df [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `df` :

- `-h` : Affiche les tailles dans un format lisible par l'homme (par exemple, en Ko, Mo, Go).
- `-T` : Affiche le type de système de fichiers.
- `-i` : Affiche des informations sur les inodes au lieu de l'espace disque.
- `-a` : Affiche tous les systèmes de fichiers, y compris ceux qui sont à 0 blocs.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `df` :

1. Afficher l'espace disque disponible sur tous les systèmes de fichiers :

   ```csh
   df
   ```

2. Afficher l'espace disque dans un format lisible par l'homme :

   ```csh
   df -h
   ```

3. Afficher le type de système de fichiers en plus de l'espace disque :

   ```csh
   df -T
   ```

4. Afficher des informations sur les inodes :

   ```csh
   df -i
   ```

5. Afficher tous les systèmes de fichiers, y compris ceux qui sont à 0 blocs :

   ```csh
   df -a
   ```

## Tips
- Utilisez l'option `-h` pour rendre les résultats plus faciles à lire, surtout si vous travaillez avec de grandes quantités de données.
- Vérifiez régulièrement l'espace disque disponible pour éviter des problèmes de stockage.
- Combinez `df` avec d'autres commandes comme `grep` pour filtrer les résultats selon vos besoins.