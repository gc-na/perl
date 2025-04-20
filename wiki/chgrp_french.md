# [Linux] C Shell (csh) chgrp : Changer le groupe d'un fichier

## Overview
La commande `chgrp` permet de changer le groupe associé à un ou plusieurs fichiers ou répertoires. Cela est particulièrement utile pour gérer les permissions d'accès dans un environnement multi-utilisateur.

## Usage
La syntaxe de base de la commande `chgrp` est la suivante :

```csh
chgrp [options] [arguments]
```

## Common Options
- `-R` : Applique le changement de groupe de manière récursive à tous les fichiers et sous-répertoires.
- `-v` : Affiche des messages détaillés pour chaque fichier traité.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `chgrp` :

1. Changer le groupe d'un fichier unique :
   ```csh
   chgrp staff document.txt
   ```

2. Changer le groupe de plusieurs fichiers à la fois :
   ```csh
   chgrp users file1.txt file2.txt file3.txt
   ```

3. Changer le groupe d'un répertoire et de son contenu de manière récursive :
   ```csh
   chgrp -R admin /chemin/vers/repertoire
   ```

4. Afficher les changements effectués :
   ```csh
   chgrp -v staff document.txt
   ```

## Tips
- Assurez-vous d'avoir les permissions nécessaires pour changer le groupe d'un fichier.
- Utilisez l'option `-R` avec précaution, car elle affecte tous les fichiers et sous-répertoires.
- Vérifiez le groupe actuel d'un fichier avec la commande `ls -l` avant de faire des modifications.