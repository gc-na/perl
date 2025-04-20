# [Linux] C Shell (csh) history : Affiche l'historique des commandes

## Overview
La commande `history` dans C Shell (csh) est utilisée pour afficher la liste des commandes précédemment exécutées dans la session actuelle. Cela permet aux utilisateurs de revoir et de réutiliser facilement les commandes sans avoir à les retaper.

## Usage
La syntaxe de base de la commande `history` est la suivante :

```csh
history [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `history` :

- `-c` : Efface l'historique des commandes.
- `-n` : Lit l'historique des commandes depuis le fichier d'historique.
- `-r` : Lit l'historique des commandes à partir d'un fichier spécifié.
- `-w` : Écrit l'historique des commandes dans le fichier d'historique.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `history` :

1. **Afficher l'historique des commandes :**
   ```csh
   history
   ```

2. **Effacer l'historique des commandes :**
   ```csh
   history -c
   ```

3. **Lire l'historique à partir d'un fichier :**
   ```csh
   history -r mon_fichier_historique
   ```

4. **Écrire l'historique dans un fichier :**
   ```csh
   history -w mon_fichier_historique
   ```

## Tips
- Utilisez `!n` pour exécuter la commande numéro `n` de l'historique.
- Pour rechercher une commande spécifique, vous pouvez utiliser `grep` avec `history`, par exemple : `history | grep "commande_recherchée"`.
- Pensez à sauvegarder régulièrement votre historique si vous utilisez souvent des commandes complexes.