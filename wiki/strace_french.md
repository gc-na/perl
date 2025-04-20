# [Linux] C Shell (csh) strace Utilisation : Suivre les appels système

## Overview
La commande `strace` est un outil puissant qui permet de suivre les appels système effectués par un programme en cours d'exécution. Cela peut être extrêmement utile pour le débogage et l'analyse des performances des applications.

## Usage
La syntaxe de base de la commande `strace` est la suivante :

```csh
strace [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `strace` :

- `-c` : Résumé des statistiques des appels système.
- `-e` : Filtrer les appels système par expression.
- `-o <file>` : Écrire la sortie dans un fichier spécifié.
- `-p <pid>` : Attacher `strace` à un processus existant par son identifiant de processus (PID).
- `-f` : Suivre les processus fils créés par le programme.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `strace` :

1. Suivre un programme simple :
   ```csh
   strace ls
   ```

2. Écrire la sortie dans un fichier :
   ```csh
   strace -o sortie.txt ls
   ```

3. Suivre un processus existant :
   ```csh
   strace -p 1234
   ```

4. Résumer les statistiques des appels système :
   ```csh
   strace -c ls
   ```

5. Filtrer les appels système par expression :
   ```csh
   strace -e trace=open,close ls
   ```

## Tips
- Utilisez l'option `-c` pour obtenir un aperçu rapide des appels système sans trop de détails.
- Lorsque vous suivez un processus avec `-p`, assurez-vous d'avoir les permissions nécessaires pour accéder au processus.
- Redirigez la sortie vers un fichier pour une analyse plus facile, surtout si le programme génère beaucoup de sorties.
- Familiarisez-vous avec les différents appels système pour mieux interpréter les résultats de `strace`.