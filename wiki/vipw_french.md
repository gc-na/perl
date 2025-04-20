# [Linux] C Shell (csh) vipw : Modifier les fichiers de mots de passe

## Overview
La commande `vipw` est utilisée pour éditer le fichier des mots de passe de manière sécurisée. Elle verrouille le fichier pendant l'édition pour éviter les conflits d'accès, garantissant ainsi que les modifications sont effectuées en toute sécurité.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
vipw [options] [arguments]
```

## Common Options
- `-s` : Utiliser un éditeur de texte spécifique pour l'édition.
- `-l` : Afficher le fichier de mots de passe au format lisible.
- `-h` : Afficher l'aide sur l'utilisation de la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `vipw` :

### Édition du fichier de mots de passe
Pour éditer le fichier de mots de passe par défaut :

```csh
vipw
```

### Utilisation d'un éditeur spécifique
Pour utiliser un éditeur spécifique, par exemple `vim` :

```csh
vipw -s vim
```

### Affichage du fichier de mots de passe
Pour afficher le fichier de mots de passe dans un format lisible :

```csh
vipw -l
```

## Tips
- Toujours faire une sauvegarde du fichier de mots de passe avant de le modifier.
- Utilisez `vipw` plutôt que d'éditer directement le fichier `/etc/passwd` pour éviter les problèmes de concurrence.
- Familiarisez-vous avec l'éditeur que vous utilisez pour éviter des erreurs lors de l'édition.