# [Linux] C Shell (csh) dstat Utilisation : surveiller les ressources système

## Overview
La commande `dstat` est un outil puissant qui permet de surveiller en temps réel les ressources système sur un système Linux. Elle combine les fonctionnalités de plusieurs outils de surveillance, offrant une vue d'ensemble des performances du système, y compris l'utilisation du processeur, la mémoire, le réseau et le disque.

## Usage
La syntaxe de base de la commande `dstat` est la suivante :

```csh
dstat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `dstat` :

- `-c` : Affiche l'utilisation du processeur.
- `-d` : Montre l'activité du disque.
- `-n` : Affiche l'activité du réseau.
- `-m` : Montre l'utilisation de la mémoire.
- `-t` : Affiche le timestamp pour chaque ligne de sortie.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `dstat` :

1. Pour afficher l'utilisation du processeur et de la mémoire :

   ```csh
   dstat -c -m
   ```

2. Pour surveiller l'activité du disque et du réseau :

   ```csh
   dstat -d -n
   ```

3. Pour afficher toutes les statistiques disponibles avec un timestamp :

   ```csh
   dstat -tcdmn
   ```

4. Pour enregistrer les résultats dans un fichier pour une analyse ultérieure :

   ```csh
   dstat -tcdmn > stats.txt
   ```

## Tips
- Utilisez `dstat` avec des options combinées pour obtenir une vue complète des performances du système.
- Pensez à rediriger la sortie vers un fichier si vous souhaitez analyser les données plus tard.
- Pour une surveillance continue, exécutez `dstat` dans un terminal séparé pendant que vous effectuez d'autres tâches sur le système.