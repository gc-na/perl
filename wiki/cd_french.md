# [Linux] C Shell (csh) cd : Changer de répertoire

## Overview
La commande `cd` (change directory) est utilisée dans le C Shell pour changer le répertoire de travail actuel. Cela permet à l'utilisateur de naviguer dans le système de fichiers et d'accéder à différents dossiers.

## Usage
La syntaxe de base de la commande `cd` est la suivante :

```csh
cd [options] [arguments]
```

## Common Options
- `-` : Retourne au dernier répertoire utilisé.
- `~` : Accède au répertoire personnel de l'utilisateur.
- `..` : Monte d'un niveau dans l'arborescence des répertoires.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cd` :

1. Changer vers un répertoire spécifique :
   ```csh
   cd /chemin/vers/le/répertoire
   ```

2. Retourner au répertoire personnel :
   ```csh
   cd ~
   ```

3. Revenir au dernier répertoire utilisé :
   ```csh
   cd -
   ```

4. Monter d'un niveau dans l'arborescence :
   ```csh
   cd ..
   ```

## Tips
- Utilisez `cd -` pour naviguer rapidement entre deux répertoires.
- Pour éviter les erreurs de chemin, utilisez toujours des chemins absolus lorsque cela est possible.
- Vous pouvez utiliser la touche de tabulation pour compléter automatiquement les noms de répertoires, ce qui facilite la navigation.