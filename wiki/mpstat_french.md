# [Linux] C Shell (csh) mpstat : surveiller l'utilisation du processeur

## Overview
La commande `mpstat` est utilisée pour afficher des statistiques sur l'utilisation du processeur. Elle fournit des informations détaillées sur la charge du processeur, permettant aux utilisateurs de surveiller la performance de leur système en temps réel.

## Usage
La syntaxe de base de la commande `mpstat` est la suivante :

```bash
mpstat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `mpstat` :

- `-P ALL` : Affiche les statistiques pour tous les processeurs.
- `-u` : Affiche l'utilisation du processeur en pourcentage.
- `-h` : Affiche les résultats dans un format lisible.
- `-t` : Affiche l'heure et la date avec les statistiques.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mpstat` :

1. Afficher les statistiques d'utilisation du processeur pour tous les processeurs :
   ```bash
   mpstat -P ALL
   ```

2. Afficher l'utilisation du processeur en pourcentage :
   ```bash
   mpstat -u
   ```

3. Afficher les statistiques avec un format lisible :
   ```bash
   mpstat -h
   ```

4. Afficher les statistiques avec l'heure et la date :
   ```bash
   mpstat -t
   ```

## Tips
- Utilisez l'option `-P ALL` pour obtenir une vue d'ensemble de tous les cœurs de processeur, ce qui est particulièrement utile sur les systèmes multicœurs.
- Combinez `mpstat` avec d'autres outils comme `grep` pour filtrer les résultats et obtenir des informations spécifiques.
- Exécutez `mpstat` à intervalles réguliers en utilisant une boucle dans un script pour surveiller l'utilisation du processeur sur une période prolongée.