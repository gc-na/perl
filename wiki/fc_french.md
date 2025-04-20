# [Linux] C Shell (csh) fc <Utilisation équivalente en français>: [modifier l'historique des commandes]

## Overview
La commande `fc` dans C Shell (csh) est utilisée pour modifier ou réexécuter des commandes précédemment exécutées dans la session de terminal. Elle permet aux utilisateurs de récupérer des commandes de l'historique, de les éditer et de les exécuter à nouveau.

## Usage
La syntaxe de base de la commande `fc` est la suivante :

```
fc [options] [arguments]
```

## Common Options
- `-l` : Liste les commandes dans l'historique.
- `-s` : Exécute la commande sans l'ouvrir dans un éditeur.
- `-n` : Ne pas afficher les numéros de lignes lors de la liste des commandes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `fc` :

1. **Lister les commandes précédentes :**
   ```csh
   fc -l
   ```

2. **Modifier la dernière commande :**
   ```csh
   fc
   ```

3. **Modifier une commande spécifique (par exemple, la commande numéro 5) :**
   ```csh
   fc 5
   ```

4. **Exécuter la dernière commande sans l'éditer :**
   ```csh
   fc -s
   ```

5. **Lister les 10 dernières commandes :**
   ```csh
   fc -l -10
   ```

## Tips
- Utilisez `fc` régulièrement pour corriger rapidement des erreurs dans les commandes précédentes sans avoir à les retaper.
- Familiarisez-vous avec votre éditeur de texte par défaut, car `fc` ouvrira les commandes dans cet éditeur pour modification.
- N'oubliez pas que `fc` ne modifie pas l'historique des commandes, il ne fait que vous permettre de les éditer et de les réexécuter.