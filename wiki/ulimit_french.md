# [Linux] C Shell (csh) ulimit : Limiter les ressources du shell

## Overview
La commande `ulimit` dans C Shell (csh) permet de définir ou d'afficher les limites sur les ressources que les processus peuvent utiliser. Cela inclut des aspects tels que la taille de la mémoire, le temps d'exécution, et d'autres ressources système. En ajustant ces limites, les utilisateurs peuvent protéger le système contre des processus gourmands en ressources.

## Usage
La syntaxe de base de la commande `ulimit` est la suivante :

```csh
ulimit [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `ulimit` :

- `-a` : Affiche toutes les limites actuelles.
- `-c` : Définit la taille maximale des fichiers de core dump.
- `-d` : Définit la taille maximale de la mémoire de données.
- `-f` : Définit la taille maximale des fichiers créés.
- `-l` : Définit la taille maximale de la mémoire verrouillée.
- `-m` : Définit la taille maximale de la mémoire résidente.
- `-s` : Définit la taille maximale de la pile.
- `-t` : Définit le temps maximal d'exécution en secondes.
- `-v` : Définit la taille maximale de la mémoire virtuelle.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `ulimit` :

1. Afficher toutes les limites actuelles :
   ```csh
   ulimit -a
   ```

2. Définir la taille maximale d'un fichier à 100 Mo :
   ```csh
   ulimit -f 102400
   ```

3. Limiter le temps d'exécution d'un processus à 30 secondes :
   ```csh
   ulimit -t 30
   ```

4. Définir la taille maximale de la mémoire de données à 512 Mo :
   ```csh
   ulimit -d 524288
   ```

5. Activer la génération de fichiers de core dump :
   ```csh
   ulimit -c unlimited
   ```

## Tips
- Vérifiez régulièrement vos limites avec `ulimit -a` pour éviter des surprises lors de l'exécution de programmes gourmands en ressources.
- Utilisez `ulimit` avec précaution, car des limites trop strictes peuvent entraîner l'échec de programmes légitimes.
- Pour appliquer des limites de manière permanente, envisagez de les ajouter à votre fichier de configuration de shell (comme `.cshrc`).
- Testez les limites dans un environnement de développement avant de les appliquer en production pour éviter des interruptions de service.