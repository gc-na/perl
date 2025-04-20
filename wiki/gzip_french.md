# [Linux] C Shell (csh) gzip : Compression de fichiers

## Overview
La commande `gzip` est utilisée pour compresser des fichiers afin de réduire leur taille. Elle utilise l'algorithme de compression DEFLATE et est souvent utilisée pour économiser de l'espace de stockage ou pour accélérer le transfert de fichiers sur le réseau.

## Usage
La syntaxe de base de la commande `gzip` est la suivante :

```csh
gzip [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `gzip` :

- `-d` : Décompresse un fichier compressé.
- `-k` : Conserve le fichier original après compression.
- `-v` : Affiche des informations détaillées sur le processus de compression.
- `-r` : Compresse les fichiers dans les sous-répertoires de manière récursive.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `gzip` :

1. **Compresser un fichier :**
   ```csh
   gzip fichier.txt
   ```

2. **Décompresser un fichier :**
   ```csh
   gzip -d fichier.txt.gz
   ```

3. **Compresser un fichier tout en conservant l'original :**
   ```csh
   gzip -k fichier.txt
   ```

4. **Compresser tous les fichiers d'un répertoire :**
   ```csh
   gzip *.txt
   ```

5. **Compresser récursivement tous les fichiers dans un répertoire :**
   ```csh
   gzip -r mon_repertoire/
   ```

## Tips
- Utilisez l'option `-v` pour vérifier la taille des fichiers avant et après compression.
- Pensez à utiliser `gzip -k` si vous souhaitez conserver une copie non compressée de vos fichiers.
- Pour décompresser plusieurs fichiers à la fois, vous pouvez utiliser un joker, par exemple `gzip -d *.gz`.