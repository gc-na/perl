# [Linux] C Shell (csh) w : Afficher les utilisateurs connectés

## Overview
La commande `w` dans C Shell (csh) est utilisée pour afficher une liste des utilisateurs actuellement connectés au système ainsi que des informations sur leur activité. Cela inclut des détails tels que le temps de connexion, l'activité en cours et l'adresse IP.

## Usage
La syntaxe de base de la commande `w` est la suivante :

```csh
w [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `w` :

- `-h` : Ne pas afficher l'en-tête de la sortie.
- `-s` : Afficher une sortie plus concise, sans les informations supplémentaires.
- `-f` : Afficher l'adresse IP des utilisateurs au lieu de leur nom d'hôte.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `w` :

1. Afficher tous les utilisateurs connectés :
   ```csh
   w
   ```

2. Afficher les utilisateurs connectés sans l'en-tête :
   ```csh
   w -h
   ```

3. Afficher une sortie concise :
   ```csh
   w -s
   ```

4. Afficher les utilisateurs avec leurs adresses IP :
   ```csh
   w -f
   ```

## Tips
- Utilisez `w` régulièrement pour surveiller l'activité des utilisateurs sur le système.
- Combinez `w` avec d'autres commandes comme `grep` pour filtrer les résultats selon des critères spécifiques.
- Familiarisez-vous avec les options pour personnaliser la sortie selon vos besoins.