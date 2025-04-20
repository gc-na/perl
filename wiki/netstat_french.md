# [Linux] C Shell (csh) netstat Utilisation : Afficher les connexions réseau

## Overview
La commande `netstat` est utilisée pour afficher des informations sur les connexions réseau, les tables de routage, les interfaces réseau et d'autres statistiques liées au réseau. Elle est particulièrement utile pour le diagnostic des problèmes de réseau et pour surveiller l'activité réseau sur un système.

## Usage
La syntaxe de base de la commande `netstat` est la suivante :

```csh
netstat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `netstat` :

- `-a` : Affiche toutes les connexions et les ports d'écoute.
- `-n` : Affiche les adresses et numéros de port sous forme numérique, sans tenter de résoudre les noms.
- `-r` : Affiche la table de routage du système.
- `-i` : Affiche les statistiques des interfaces réseau.
- `-s` : Affiche les statistiques des protocoles réseau.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `netstat` :

1. Afficher toutes les connexions et ports d'écoute :
   ```csh
   netstat -a
   ```

2. Afficher les connexions avec des adresses numériques :
   ```csh
   netstat -n
   ```

3. Afficher la table de routage :
   ```csh
   netstat -r
   ```

4. Afficher les statistiques des interfaces réseau :
   ```csh
   netstat -i
   ```

5. Afficher les statistiques des protocoles :
   ```csh
   netstat -s
   ```

## Tips
- Utilisez l'option `-n` pour accélérer l'affichage des résultats, surtout sur des systèmes avec de nombreuses connexions.
- Combinez plusieurs options pour obtenir des informations plus détaillées, par exemple `netstat -an` pour voir toutes les connexions avec des adresses numériques.
- Vérifiez régulièrement les connexions réseau pour détecter toute activité suspecte ou non autorisée.