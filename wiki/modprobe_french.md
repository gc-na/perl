# [Linux] C Shell (csh) modprobe : Charger des modules du noyau

## Overview
La commande `modprobe` est utilisée pour charger et décharger des modules du noyau Linux. Elle gère les dépendances entre les modules, ce qui permet de s'assurer que tous les modules nécessaires sont chargés correctement.

## Usage
La syntaxe de base de la commande `modprobe` est la suivante :

```csh
modprobe [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `modprobe` :

- `-r` : Décharge un module.
- `--list` : Affiche les modules qui seraient chargés.
- `--show-depends` : Montre les dépendances d'un module.
- `--quiet` : Réduit la sortie d'information.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `modprobe` :

1. Charger un module :
   ```csh
   modprobe nouveau
   ```

2. Décharger un module :
   ```csh
   modprobe -r nouveau
   ```

3. Afficher les dépendances d'un module :
   ```csh
   modprobe --show-depends nouveau
   ```

4. Lister les modules qui seraient chargés :
   ```csh
   modprobe --list nouveau
   ```

## Tips
- Assurez-vous d'avoir les droits d'administrateur pour charger ou décharger des modules.
- Utilisez l'option `--quiet` pour réduire le bruit lors de l'exécution de scripts automatisés.
- Vérifiez toujours les dépendances d'un module avant de le décharger pour éviter des problèmes de stabilité du système.