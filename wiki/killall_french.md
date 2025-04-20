# [Linux] C Shell (csh) killall : Terminer des processus par nom

## Overview
La commande `killall` est utilisée pour terminer tous les processus qui correspondent à un nom de programme spécifique. Cela permet de gérer facilement les processus en cours d'exécution sans avoir à chercher leur identifiant de processus (PID).

## Usage
La syntaxe de base de la commande `killall` est la suivante :

```csh
killall [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `killall` :

- `-9` : Force l'arrêt immédiat des processus.
- `-v` : Affiche des informations détaillées sur les processus terminés.
- `-i` : Demande une confirmation avant de terminer chaque processus.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `killall` :

1. Terminer tous les processus de Firefox :
   ```csh
   killall firefox
   ```

2. Terminer tous les processus de manière forcée :
   ```csh
   killall -9 firefox
   ```

3. Afficher les processus qui vont être terminés :
   ```csh
   killall -v firefox
   ```

4. Demander une confirmation avant de terminer chaque processus :
   ```csh
   killall -i firefox
   ```

## Tips
- Utilisez l'option `-v` pour vérifier quels processus sont terminés, cela peut être utile pour le débogage.
- Soyez prudent avec l'option `-9`, car elle force l'arrêt des processus sans leur permettre de se fermer proprement, ce qui peut entraîner une perte de données.
- Avant d'utiliser `killall`, assurez-vous que vous avez les droits nécessaires pour terminer les processus ciblés.