# [Linux] C Shell (csh) who <Utilisation>: Affiche les utilisateurs connectés

## Overview
La commande `who` dans C Shell (csh) est utilisée pour afficher une liste des utilisateurs actuellement connectés au système. Elle fournit des informations telles que le nom d'utilisateur, le terminal utilisé, la date et l'heure de connexion.

## Usage
La syntaxe de base de la commande `who` est la suivante :

```
who [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `who` :

- `-a` : Affiche toutes les informations disponibles, y compris les utilisateurs connectés et les utilisateurs qui ont quitté.
- `-b` : Affiche la dernière fois que le système a été redémarré.
- `-q` : Affiche uniquement les noms des utilisateurs connectés, suivis d'un compte total.
- `-H` : Affiche les en-têtes de colonne pour les informations affichées.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `who` :

1. Afficher tous les utilisateurs connectés :
   ```csh
   who
   ```

2. Afficher toutes les informations disponibles :
   ```csh
   who -a
   ```

3. Afficher la dernière fois que le système a été redémarré :
   ```csh
   who -b
   ```

4. Afficher uniquement les noms des utilisateurs connectés :
   ```csh
   who -q
   ```

5. Afficher les en-têtes de colonne :
   ```csh
   who -H
   ```

## Tips
- Utilisez `who -q` pour obtenir rapidement un aperçu du nombre d'utilisateurs connectés sans trop de détails.
- Combinez `who` avec d'autres commandes comme `grep` pour filtrer les résultats selon des critères spécifiques.
- Pensez à utiliser `who -b` de temps en temps pour savoir quand le système a été redémarré, ce qui peut être utile pour le dépannage.