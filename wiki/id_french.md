# [Linux] C Shell (csh) id : afficher les informations d'identité de l'utilisateur

## Overview
La commande `id` dans C Shell (csh) est utilisée pour afficher les informations d'identité de l'utilisateur courant. Elle fournit des détails tels que l'UID (User ID), le GID (Group ID) et les groupes auxquels l'utilisateur appartient.

## Usage
La syntaxe de base de la commande `id` est la suivante :

```
id [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `id` :

- `-u` : Affiche uniquement l'UID de l'utilisateur courant.
- `-g` : Affiche uniquement le GID du groupe principal de l'utilisateur.
- `-G` : Affiche tous les GIDs des groupes auxquels l'utilisateur appartient.
- `-n` : Utilisé avec `-u` ou `-g` pour afficher le nom au lieu de l'ID.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `id` :

1. Afficher les informations d'identité de l'utilisateur courant :
   ```csh
   id
   ```

2. Afficher uniquement l'UID de l'utilisateur courant :
   ```csh
   id -u
   ```

3. Afficher uniquement le GID du groupe principal de l'utilisateur :
   ```csh
   id -g
   ```

4. Afficher tous les GIDs des groupes auxquels l'utilisateur appartient :
   ```csh
   id -G
   ```

5. Afficher le nom de l'utilisateur courant et son UID :
   ```csh
   id -nu
   ```

## Tips
- Utilisez `id` sans options pour obtenir un aperçu complet de votre identité utilisateur.
- Combinez les options pour obtenir des informations spécifiques selon vos besoins.
- Vérifiez vos groupes d'appartenance avec `id -G` si vous rencontrez des problèmes d'autorisation.