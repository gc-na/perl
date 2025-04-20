# [Linux] C Shell (csh) pidstat : [surveiller l'utilisation des ressources des processus]

## Overview
La commande `pidstat` est utilisée pour surveiller l'utilisation des ressources des processus en cours d'exécution sur un système. Elle permet d'afficher des informations détaillées sur l'utilisation du CPU, de la mémoire, et d'autres ressources par chaque processus.

## Usage
La syntaxe de base de la commande `pidstat` est la suivante :

```csh
pidstat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `pidstat` :

- `-h` : Affiche les en-têtes de colonnes en format lisible.
- `-r` : Affiche l'utilisation de la mémoire par processus.
- `-u` : Affiche l'utilisation du CPU par processus.
- `-p <pid>` : Spécifie le PID du processus à surveiller.
- `-t` : Affiche les threads d'un processus.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `pidstat` :

1. **Surveiller l'utilisation du CPU de tous les processus :**

   ```csh
   pidstat -u
   ```

2. **Afficher l'utilisation de la mémoire pour tous les processus :**

   ```csh
   pidstat -r
   ```

3. **Surveiller un processus spécifique avec son PID :**

   ```csh
   pidstat -p 1234
   ```

4. **Surveiller l'utilisation du CPU et de la mémoire toutes les 5 secondes :**

   ```csh
   pidstat -u -r 5
   ```

5. **Afficher les threads d'un processus spécifique :**

   ```csh
   pidstat -t -p 1234
   ```

## Tips
- Utilisez l'option `-h` pour rendre les résultats plus lisibles, surtout si vous traitez avec de nombreux processus.
- Combinez les options `-u` et `-r` pour obtenir une vue d'ensemble complète de l'utilisation des ressources par processus.
- Pour une surveillance continue, vous pouvez exécuter `pidstat` dans une boucle ou avec un cron job pour collecter des données sur une période prolongée.