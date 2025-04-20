# [Linux] C Shell (csh) iostat Utilisation : Surveillance des statistiques d'entrée/sortie

## Overview
La commande `iostat` est utilisée pour surveiller les statistiques d'entrée/sortie des systèmes de fichiers et des périphériques de stockage. Elle fournit des informations sur l'utilisation du CPU ainsi que sur les performances des disques, ce qui peut aider à diagnostiquer des problèmes de performance.

## Usage
La syntaxe de base de la commande `iostat` est la suivante :

```csh
iostat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `iostat` :

- `-c` : Affiche uniquement les statistiques du CPU.
- `-d` : Affiche uniquement les statistiques des périphériques.
- `-x` : Affiche les statistiques étendues pour les périphériques.
- `-t` : Affiche l'heure et la date avec les statistiques.
- `interval` : Spécifie l'intervalle de temps entre les rapports.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `iostat` :

1. Afficher les statistiques de base :
   ```csh
   iostat
   ```

2. Afficher uniquement les statistiques du CPU :
   ```csh
   iostat -c
   ```

3. Afficher les statistiques des périphériques avec des détails étendus :
   ```csh
   iostat -dx
   ```

4. Afficher les statistiques toutes les 5 secondes :
   ```csh
   iostat 5
   ```

5. Afficher les statistiques avec la date et l'heure :
   ```csh
   iostat -t
   ```

## Tips
- Utilisez l'option `-x` pour obtenir des informations détaillées sur les performances des disques, ce qui est utile pour le dépannage.
- Combinez `iostat` avec d'autres outils comme `vmstat` ou `mpstat` pour une analyse plus complète des performances système.
- Surveillez régulièrement les statistiques d'entrée/sortie pour identifier les goulets d'étranglement potentiels avant qu'ils ne deviennent des problèmes majeurs.