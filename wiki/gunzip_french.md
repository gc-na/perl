# [Linux] C Shell (csh) gunzip : Décompresser des fichiers gzip

## Overview
La commande `gunzip` est utilisée pour décompresser des fichiers qui ont été compressés au format gzip. Elle permet de restaurer les fichiers à leur état original, facilitant ainsi leur utilisation.

## Usage
La syntaxe de base de la commande `gunzip` est la suivante :

```csh
gunzip [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `gunzip` :

- `-c` : Affiche le contenu décompressé sur la sortie standard sans supprimer le fichier compressé.
- `-f` : Force la décompression, même si le fichier de destination existe déjà.
- `-k` : Conserve le fichier compressé après la décompression.
- `-v` : Affiche des informations détaillées sur le processus de décompression.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `gunzip` :

1. Décompresser un fichier gzip :
   ```csh
   gunzip fichier.txt.gz
   ```

2. Décompresser un fichier tout en conservant l'original :
   ```csh
   gunzip -k fichier.txt.gz
   ```

3. Afficher le contenu décompressé sans supprimer le fichier :
   ```csh
   gunzip -c fichier.txt.gz
   ```

4. Forcer la décompression d'un fichier existant :
   ```csh
   gunzip -f fichier.txt.gz
   ```

5. Afficher des informations détaillées pendant la décompression :
   ```csh
   gunzip -v fichier.txt.gz
   ```

## Tips
- Toujours vérifier l'espace disque disponible avant de décompresser de gros fichiers pour éviter des erreurs.
- Utilisez l'option `-k` si vous souhaitez conserver les fichiers compressés pour une utilisation future.
- Si vous travaillez avec plusieurs fichiers, vous pouvez spécifier plusieurs fichiers à la fois :
  ```csh
  gunzip fichier1.gz fichier2.gz fichier3.gz
  ```