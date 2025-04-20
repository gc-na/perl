# [Linux] C Shell (csh) vmstat Utilisation : Afficher les statistiques de la mémoire et des processus

## Overview
La commande `vmstat` (Virtual Memory Statistics) est utilisée pour afficher des informations sur la mémoire virtuelle, les processus, l'entrée/sortie, et d'autres statistiques système. Elle permet aux utilisateurs de surveiller l'état de la mémoire et de diagnostiquer les problèmes de performance.

## Usage
La syntaxe de base de la commande `vmstat` est la suivante :

```csh
vmstat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `vmstat` :

- `-a` : Affiche la mémoire active et inactive.
- `-m` : Affiche les statistiques de la mémoire de page.
- `-s` : Affiche un résumé des statistiques de la mémoire.
- `-n` : N'affiche pas les en-têtes de colonne après la première ligne.
- `delay` : Spécifie le délai entre les mises à jour des statistiques (en secondes).
- `count` : Indique combien de fois les statistiques doivent être affichées.

## Common Examples

Voici quelques exemples pratiques de l'utilisation de `vmstat` :

1. Afficher les statistiques de mémoire toutes les 2 secondes :

   ```csh
   vmstat 2
   ```

2. Afficher les statistiques de mémoire avec des informations sur la mémoire active et inactive :

   ```csh
   vmstat -a
   ```

3. Afficher un résumé des statistiques de la mémoire :

   ```csh
   vmstat -s
   ```

4. Afficher les statistiques toutes les 5 secondes, 3 fois :

   ```csh
   vmstat 5 3
   ```

5. Afficher les statistiques de la mémoire de page :

   ```csh
   vmstat -m
   ```

## Tips
- Utilisez `vmstat` avec des intervalles courts pour surveiller les performances en temps réel.
- Combinez `vmstat` avec d'autres outils comme `top` ou `iostat` pour une analyse plus complète du système.
- Vérifiez régulièrement les statistiques de mémoire pour anticiper les problèmes de performance avant qu'ils ne deviennent critiques.