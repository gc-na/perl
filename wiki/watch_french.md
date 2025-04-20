# [Linux] C Shell (csh) watch utilisation : surveiller les commandes en temps réel

## Overview
La commande `watch` permet d'exécuter une commande à intervalles réguliers et d'afficher sa sortie à l'écran. Cela est particulièrement utile pour surveiller les changements dans l'état d'un système ou d'un fichier.

## Usage
La syntaxe de base de la commande `watch` est la suivante :

```csh
watch [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `watch` :

- `-n <seconds>` : Définit l'intervalle en secondes entre chaque exécution de la commande.
- `-d` : Met en surbrillance les différences entre les sorties successives.
- `-t` : Supprime l'affichage de l'en-tête, montrant uniquement la sortie de la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `watch` :

1. Surveiller l'utilisation de la mémoire :
   ```csh
   watch -n 5 free -h
   ```

2. Vérifier les processus en cours :
   ```csh
   watch ps aux
   ```

3. Surveiller les changements dans un répertoire :
   ```csh
   watch -d ls -l /path/to/directory
   ```

4. Afficher l'espace disque toutes les 10 secondes :
   ```csh
   watch -n 10 df -h
   ```

## Tips
- Utilisez l'option `-d` pour mieux visualiser les changements dans les sorties.
- Choisissez un intervalle raisonnable avec `-n` pour éviter de surcharger le système avec trop d'exécutions.
- Pensez à utiliser `-t` si vous souhaitez une sortie plus propre sans l'en-tête.