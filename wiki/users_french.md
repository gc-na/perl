# [Linux] C Shell (csh) utilisateurs : Afficher les utilisateurs connectés

## Overview
La commande `users` dans C Shell (csh) permet d'afficher les noms des utilisateurs actuellement connectés au système. C'est un outil simple mais efficace pour obtenir rapidement des informations sur les sessions utilisateurs actives.

## Usage
La syntaxe de base de la commande `users` est la suivante :

```
users [options] [arguments]
```

## Common Options
- `-n` : Affiche le nombre d'utilisateurs connectés.
- `-r` : Affiche les utilisateurs connectés en mode "remote" (à distance).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `users` :

1. Afficher les utilisateurs connectés :
   ```csh
   users
   ```

2. Afficher le nombre d'utilisateurs connectés :
   ```csh
   users -n
   ```

3. Afficher les utilisateurs connectés à distance :
   ```csh
   users -r
   ```

## Tips
- Utilisez la commande `who` pour obtenir des informations plus détaillées sur les utilisateurs connectés, y compris l'heure de connexion et le terminal utilisé.
- Combinez `users` avec d'autres commandes comme `wc -l` pour compter le nombre d'utilisateurs connectés :
  ```csh
  users | wc -l
  ```
- Pensez à utiliser `users` dans des scripts pour surveiller l'activité des utilisateurs sur le système.