# [Linux] C Shell (csh) rmdir : Supprimer des répertoires vides

## Overview
La commande `rmdir` est utilisée pour supprimer des répertoires vides dans le système de fichiers. Si le répertoire contient des fichiers ou d'autres répertoires, la commande échouera et ne supprimera pas le répertoire.

## Usage
La syntaxe de base de la commande `rmdir` est la suivante :

```csh
rmdir [options] [arguments]
```

## Common Options
- `-p` : Supprime le répertoire spécifié ainsi que tous ses répertoires parents vides.
- `--help` : Affiche l'aide sur la commande `rmdir`.
- `--version` : Affiche la version de la commande `rmdir`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `rmdir` :

1. Supprimer un répertoire vide nommé `mon_repertoire` :

   ```csh
   rmdir mon_repertoire
   ```

2. Supprimer un répertoire vide et ses parents vides :

   ```csh
   rmdir -p mon_repertoire/parent/ancien_repertoire
   ```

3. Afficher l'aide de la commande `rmdir` :

   ```csh
   rmdir --help
   ```

## Tips
- Assurez-vous que le répertoire que vous souhaitez supprimer est vide avant d'utiliser `rmdir`, sinon la commande échouera.
- Utilisez l'option `-p` avec prudence, car elle supprimera tous les répertoires parents vides jusqu'à ce qu'un répertoire non vide soit atteint.
- Pour vérifier le contenu d'un répertoire avant de le supprimer, utilisez la commande `ls` pour lister les fichiers qu'il contient.