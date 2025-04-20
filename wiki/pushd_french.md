# [Linux] C Shell (csh) pushd : [changer de répertoire avec une pile]

## Overview
La commande `pushd` dans C Shell (csh) est utilisée pour changer de répertoire tout en stockant l'ancien répertoire dans une pile. Cela permet de naviguer facilement entre plusieurs répertoires sans perdre la trace de votre emplacement précédent.

## Usage
La syntaxe de base de la commande `pushd` est la suivante :

```csh
pushd [options] [arguments]
```

## Common Options
- `+n` : Accède au n-ième répertoire de la pile, en commençant par 0.
- `-n` : Accède au n-ième répertoire de la pile en partant de la fin.
- `-` : Retourne au répertoire précédent.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `pushd` :

1. **Changer de répertoire et ajouter à la pile :**
   ```csh
   pushd /chemin/vers/nouveau/répertoire
   ```

2. **Accéder à un répertoire spécifique dans la pile :**
   ```csh
   pushd +1
   ```

3. **Revenir au répertoire précédent :**
   ```csh
   pushd -
   ```

4. **Afficher la pile des répertoires :**
   ```csh
   dirs
   ```

## Tips
- Utilisez `popd` pour revenir au répertoire précédent et retirer ce répertoire de la pile.
- Pensez à utiliser `dirs` pour afficher la pile actuelle des répertoires, ce qui peut vous aider à garder une trace de votre navigation.
- Combinez `pushd` avec des scripts pour automatiser la navigation entre plusieurs répertoires.