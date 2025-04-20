# [Linux] C Shell (csh) unxz : Décompresser des fichiers .xz

## Overview
La commande `unxz` est utilisée pour décompresser des fichiers compressés au format .xz. Ce format est souvent utilisé pour réduire la taille des fichiers tout en maintenant une bonne qualité de compression.

## Usage
La syntaxe de base de la commande `unxz` est la suivante :

```
unxz [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `unxz` :

- `-k` : Conserve le fichier d'origine après la décompression.
- `-f` : Force la décompression, même si le fichier de destination existe déjà.
- `-v` : Affiche des informations détaillées sur le processus de décompression.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `unxz` :

1. Décompresser un fichier .xz :
   ```csh
   unxz fichier.xz
   ```

2. Décompresser un fichier tout en conservant l'original :
   ```csh
   unxz -k fichier.xz
   ```

3. Forcer la décompression d'un fichier existant :
   ```csh
   unxz -f fichier.xz
   ```

4. Afficher des informations détaillées lors de la décompression :
   ```csh
   unxz -v fichier.xz
   ```

## Tips
- Assurez-vous d'avoir suffisamment d'espace disque avant de décompresser un fichier, surtout si vous ne conservez pas l'original.
- Utilisez l'option `-k` si vous souhaitez garder le fichier compressé pour une utilisation future.
- Vérifiez toujours l'intégrité du fichier décompressé, surtout si vous l'avez téléchargé depuis Internet.