# [Linux] C Shell (csh) pwd : Afficher le répertoire de travail actuel

## Overview
La commande `pwd` (print working directory) dans le C Shell affiche le chemin complet du répertoire de travail actuel. C'est un outil essentiel pour naviguer dans le système de fichiers et savoir où vous vous trouvez à tout moment.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
pwd [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `pwd` :

- `-L` : Affiche le chemin logique du répertoire de travail actuel.
- `-P` : Affiche le chemin physique, en résolvant les liens symboliques.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `pwd` :

1. Afficher le répertoire de travail actuel :
   ```csh
   pwd
   ```

2. Afficher le chemin logique :
   ```csh
   pwd -L
   ```

3. Afficher le chemin physique :
   ```csh
   pwd -P
   ```

## Tips
- Utilisez `pwd` régulièrement pour vous assurer que vous êtes dans le bon répertoire avant d'exécuter d'autres commandes.
- Combinez `pwd` avec d'autres commandes comme `cd` pour naviguer efficacement dans le système de fichiers.
- Si vous travaillez avec des liens symboliques, utilisez l'option `-P` pour obtenir le chemin réel du répertoire.