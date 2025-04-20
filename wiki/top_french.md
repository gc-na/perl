# [Linux] C Shell (csh) top : Afficher les processus en cours

## Overview
La commande `top` est utilisée pour afficher en temps réel les processus en cours d'exécution sur un système. Elle fournit des informations détaillées sur l'utilisation du processeur, de la mémoire et d'autres ressources système, permettant ainsi aux utilisateurs de surveiller l'état de leur système.

## Usage
La syntaxe de base de la commande `top` est la suivante :

```
top [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec la commande `top` :

- `-d <seconds>` : Définit le délai entre les mises à jour de l'affichage.
- `-n <number>` : Limite le nombre d'itérations d'affichage.
- `-u <user>` : Affiche uniquement les processus appartenant à l'utilisateur spécifié.
- `-p <pid>` : Affiche uniquement le processus avec l'identifiant de processus spécifié.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `top` :

1. Afficher les processus avec des mises à jour toutes les 5 secondes :
   ```bash
   top -d 5
   ```

2. Limiter l'affichage à 10 mises à jour :
   ```bash
   top -n 10
   ```

3. Afficher uniquement les processus d'un utilisateur spécifique :
   ```bash
   top -u username
   ```

4. Surveiller un processus spécifique par son PID :
   ```bash
   top -p 1234
   ```

## Tips
- Pour quitter l'affichage de `top`, appuyez sur `q`.
- Vous pouvez trier les processus par différentes colonnes en appuyant sur les touches correspondantes (par exemple, `M` pour trier par utilisation de la mémoire).
- Utilisez `h` pour afficher l'aide à l'intérieur de l'interface `top` pour plus d'options et de commandes.