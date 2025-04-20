# [Linux] C Shell (csh) finger : Afficher des informations sur les utilisateurs

## Overview
La commande `finger` est utilisée pour afficher des informations sur les utilisateurs d'un système. Elle fournit des détails tels que le nom complet, le statut de connexion, et d'autres informations pertinentes sur les utilisateurs.

## Usage
La syntaxe de base de la commande `finger` est la suivante :

```bash
finger [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `finger` :

- `-l` : Affiche les informations détaillées sur les utilisateurs.
- `-m` : Ignore la casse lors de la recherche d'un utilisateur.
- `-s` : Affiche un résumé des informations sur les utilisateurs.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `finger` :

1. Afficher des informations sur tous les utilisateurs :
   ```bash
   finger
   ```

2. Afficher des informations détaillées sur un utilisateur spécifique :
   ```bash
   finger nom_utilisateur
   ```

3. Afficher un résumé des informations sur tous les utilisateurs :
   ```bash
   finger -s
   ```

4. Afficher des informations sur un utilisateur sans tenir compte de la casse :
   ```bash
   finger -m Nom_Utilisateur
   ```

## Tips
- Utilisez `finger` sans arguments pour obtenir une vue d'ensemble rapide de tous les utilisateurs connectés.
- Pour obtenir des informations détaillées, n'hésitez pas à utiliser l'option `-l`.
- Si vous recherchez un utilisateur dont vous n'êtes pas sûr de l'orthographe, l'option `-m` peut être très utile.