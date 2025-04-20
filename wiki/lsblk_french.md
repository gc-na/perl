# [Linux] C Shell (csh) lsblk Utilisation : Afficher les périphériques de bloc

## Overview
La commande `lsblk` est utilisée pour afficher des informations sur les périphériques de bloc disponibles sur le système. Elle permet de visualiser la structure des disques, des partitions et des volumes logiques, facilitant ainsi la gestion des ressources de stockage.

## Usage
La syntaxe de base de la commande `lsblk` est la suivante :

```csh
lsblk [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `lsblk` :

- `-a` : Affiche tous les périphériques, y compris ceux qui ne sont pas montés.
- `-f` : Affiche les informations sur le système de fichiers.
- `-l` : Affiche la sortie sous forme de liste, plutôt que de l'arborescence par défaut.
- `-o` : Permet de spécifier les colonnes à afficher dans la sortie.
- `-p` : Affiche les chemins complets des périphériques.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `lsblk` :

1. Afficher tous les périphériques de bloc :
   ```csh
   lsblk
   ```

2. Afficher tous les périphériques, y compris ceux non montés :
   ```csh
   lsblk -a
   ```

3. Afficher les informations sur le système de fichiers :
   ```csh
   lsblk -f
   ```

4. Afficher la sortie sous forme de liste :
   ```csh
   lsblk -l
   ```

5. Afficher des colonnes spécifiques, comme le nom et la taille :
   ```csh
   lsblk -o NAME,SIZE
   ```

## Tips
- Utilisez l'option `-f` pour obtenir des informations détaillées sur le système de fichiers, ce qui peut être utile pour le dépannage.
- Combinez `lsblk` avec d'autres commandes comme `grep` pour filtrer les résultats selon vos besoins.
- Pensez à exécuter `lsblk` avec des privilèges d'administrateur si vous ne voyez pas tous les périphériques, car certains peuvent nécessiter des autorisations élevées pour être affichés.