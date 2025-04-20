# [Linux] C Shell (csh) cp Utilisation : Copier des fichiers et des répertoires

## Overview
La commande `cp` dans C Shell (csh) est utilisée pour copier des fichiers et des répertoires d'un emplacement à un autre. Elle permet de dupliquer des fichiers tout en préservant leur contenu.

## Usage
La syntaxe de base de la commande `cp` est la suivante :

```csh
cp [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `cp` :

- `-i` : Demande une confirmation avant d'écraser un fichier existant.
- `-r` : Copie récursivement les répertoires et leur contenu.
- `-u` : Copie uniquement si le fichier source est plus récent que le fichier de destination ou si le fichier de destination n'existe pas.
- `-v` : Affiche les fichiers au fur et à mesure qu'ils sont copiés (mode verbeux).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cp` :

1. Copier un fichier simple :
   ```csh
   cp fichier.txt copie_fichier.txt
   ```

2. Copier un répertoire et son contenu :
   ```csh
   cp -r dossier_source/ dossier_destination/
   ```

3. Copier un fichier avec confirmation avant écrasement :
   ```csh
   cp -i fichier.txt copie_fichier.txt
   ```

4. Copier un fichier uniquement s'il est plus récent :
   ```csh
   cp -u fichier.txt copie_fichier.txt
   ```

5. Copier un fichier en mode verbeux :
   ```csh
   cp -v fichier.txt copie_fichier.txt
   ```

## Tips
- Toujours utiliser l'option `-i` si vous n'êtes pas sûr d'écraser des fichiers existants.
- Pour copier plusieurs fichiers vers un répertoire, listez les fichiers avant le répertoire :
  ```csh
  cp fichier1.txt fichier2.txt dossier_destination/
  ```
- Vérifiez toujours les permissions des fichiers et répertoires avant de copier pour éviter des erreurs d'accès.