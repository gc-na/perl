# [Linux] C Shell (csh) uptime : Afficher le temps de fonctionnement du système

## Overview
La commande `uptime` dans C Shell (csh) permet d'afficher depuis combien de temps le système est en fonctionnement, ainsi que le nombre d'utilisateurs connectés et la charge moyenne du système sur différentes périodes.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
uptime [options]
```

## Common Options
Voici quelques options courantes pour la commande `uptime` :

- `-p` : Affiche le temps de fonctionnement sous une forme lisible.
- `-s` : Affiche l'heure à laquelle le système a démarré.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `uptime` :

1. Afficher le temps de fonctionnement du système :
   ```csh
   uptime
   ```

2. Afficher le temps de fonctionnement dans un format lisible :
   ```csh
   uptime -p
   ```

3. Afficher l'heure de démarrage du système :
   ```csh
   uptime -s
   ```

## Tips
- Utilisez `uptime` régulièrement pour surveiller la santé de votre système.
- Combinez `uptime` avec d'autres commandes comme `who` pour obtenir des informations supplémentaires sur les utilisateurs connectés.
- Pensez à vérifier la charge moyenne pour évaluer la performance du système, surtout lors de périodes de forte utilisation.