# [Linux] C Shell (csh) unalias : Supprimer des alias

## Overview
La commande `unalias` dans C Shell (csh) est utilisée pour supprimer des alias définis précédemment. Les alias sont des raccourcis pour des commandes plus longues, et parfois il est nécessaire de les retirer pour éviter des conflits ou pour revenir à un comportement par défaut.

## Usage
La syntaxe de base de la commande `unalias` est la suivante :

```csh
unalias [options] [arguments]
```

## Common Options
- `-a` : Supprime tous les alias définis.
- `-m` : Supprime les alias qui correspondent à un motif spécifique.

## Common Examples

### Supprimer un alias spécifique
Pour supprimer un alias nommé `ll`, utilisez la commande suivante :

```csh
unalias ll
```

### Supprimer tous les alias
Pour supprimer tous les alias définis dans votre session, utilisez l'option `-a` :

```csh
unalias -a
```

### Supprimer un alias avec un motif
Si vous avez plusieurs alias qui commencent par `g`, vous pouvez les supprimer en utilisant l'option `-m` :

```csh
unalias -m g*
```

## Tips
- Vérifiez vos alias actuels avec la commande `alias` avant de les supprimer pour éviter de supprimer quelque chose d'utile.
- Utilisez `unalias -a` avec précaution, car cela supprimera tous les alias sans possibilité de récupération.
- Pensez à sauvegarder vos alias dans un fichier de configuration si vous prévoyez de les réutiliser à l'avenir.