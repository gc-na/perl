# [Linux] C Shell (csh) bzip2 : Compresser des fichiers

## Overview
La commande `bzip2` est utilisée pour compresser des fichiers afin de réduire leur taille. Elle utilise l'algorithme de compression Burrows-Wheeler et est particulièrement efficace pour les fichiers texte.

## Usage
La syntaxe de base de la commande `bzip2` est la suivante :

```csh
bzip2 [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `bzip2` :

- `-d` : Décompresse un fichier compressé.
- `-k` : Garde le fichier d'origine après compression.
- `-v` : Affiche des informations détaillées sur le processus de compression.
- `-z` : Compresse un fichier (c'est l'option par défaut).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `bzip2` :

1. Pour compresser un fichier nommé `exemple.txt` :

   ```csh
   bzip2 exemple.txt
   ```

2. Pour décompresser un fichier compressé nommé `exemple.txt.bz2` :

   ```csh
   bzip2 -d exemple.txt.bz2
   ```

3. Pour compresser un fichier tout en gardant l'original :

   ```csh
   bzip2 -k exemple.txt
   ```

4. Pour afficher des informations détaillées lors de la compression :

   ```csh
   bzip2 -v exemple.txt
   ```

## Tips
- Utilisez l'option `-k` si vous souhaitez conserver les fichiers d'origine après compression.
- Pour des fichiers très volumineux, envisagez d'utiliser `bzip2` en arrière-plan pour éviter de bloquer votre terminal.
- Vérifiez toujours l'intégrité de vos fichiers après compression et décompression pour vous assurer qu'aucune donnée n'a été perdue.