# [Linux] C Shell (csh) mkfifo : Créer des fichiers FIFO

## Overview
La commande `mkfifo` est utilisée pour créer des fichiers FIFO (First In, First Out) dans le système de fichiers. Ces fichiers permettent la communication entre différents processus en utilisant un modèle de file d'attente.

## Usage
La syntaxe de base de la commande `mkfifo` est la suivante :

```csh
mkfifo [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `mkfifo` :

- `-m` : Définit les permissions du fichier FIFO. Par exemple, `-m 644` attribue des permissions de lecture et d'écriture au propriétaire et de lecture aux autres.
- `--help` : Affiche l'aide et les options disponibles pour la commande.
- `--version` : Affiche la version de la commande `mkfifo`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `mkfifo` :

1. Créer un fichier FIFO nommé `mon_fifo` :

   ```csh
   mkfifo mon_fifo
   ```

2. Créer un fichier FIFO avec des permissions spécifiques :

   ```csh
   mkfifo -m 666 mon_fifo
   ```

3. Vérifier que le fichier FIFO a été créé :

   ```csh
   ls -l mon_fifo
   ```

4. Utiliser le fichier FIFO dans un processus de communication :

   - Dans un terminal, vous pouvez écrire dans le FIFO :

     ```csh
     echo "Bonjour" > mon_fifo
     ```

   - Dans un autre terminal, vous pouvez lire à partir du FIFO :

     ```csh
     cat mon_fifo
     ```

## Tips
- Assurez-vous de gérer correctement les fichiers FIFO pour éviter les blocages dans les processus.
- Utilisez les permissions appropriées lors de la création de fichiers FIFO pour contrôler l'accès.
- Testez toujours vos commandes dans un environnement sûr avant de les utiliser en production.