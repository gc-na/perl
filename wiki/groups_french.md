# [Linux] C Shell (csh) groups : afficher les groupes d'utilisateurs

## Overview
La commande `groups` dans C Shell (csh) permet d'afficher les groupes auxquels un utilisateur appartient. Cela peut être utile pour vérifier les permissions et les accès associés à un utilisateur dans un système.

## Usage
La syntaxe de base de la commande est la suivante :

```
groups [options] [arguments]
```

## Common Options
- `-a` : Affiche tous les groupes, y compris les groupes secondaires.
- `-g` : Affiche uniquement les groupes principaux de l'utilisateur spécifié.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `groups` :

1. Afficher les groupes de l'utilisateur courant :
   ```csh
   groups
   ```

2. Afficher les groupes d'un utilisateur spécifique :
   ```csh
   groups nom_utilisateur
   ```

3. Afficher tous les groupes, y compris les groupes secondaires :
   ```csh
   groups -a nom_utilisateur
   ```

4. Afficher uniquement le groupe principal d'un utilisateur :
   ```csh
   groups -g nom_utilisateur
   ```

## Tips
- Utilisez `groups` sans arguments pour rapidement vérifier les groupes de l'utilisateur connecté.
- Si vous êtes administrateur, vous pouvez vérifier les groupes d'autres utilisateurs pour gérer les permissions efficacement.
- Pensez à utiliser l'option `-a` pour obtenir une vue complète des groupes d'un utilisateur, surtout si vous gérez des accès complexes.