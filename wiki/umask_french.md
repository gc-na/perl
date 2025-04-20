# [Linux] C Shell (csh) umask : [définir les permissions par défaut des fichiers]

## Overview
La commande `umask` dans C Shell (csh) est utilisée pour définir les permissions par défaut des fichiers et des répertoires créés par l'utilisateur. Elle détermine les permissions qui seront retirées des permissions par défaut lors de la création d'un nouveau fichier ou répertoire.

## Usage
La syntaxe de base de la commande `umask` est la suivante :

```csh
umask [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `umask` :

- `-S` : Affiche les permissions sous forme symbolique.
- `-p` : Affiche la valeur actuelle de umask en mode symbolique.
- `n` : Définit umask à une valeur numérique.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `umask` :

1. **Afficher la valeur actuelle de umask :**
   ```csh
   umask
   ```

2. **Définir umask à 022 (permissions par défaut pour les fichiers créés : rw-r--r--) :**
   ```csh
   umask 022
   ```

3. **Afficher umask en mode symbolique :**
   ```csh
   umask -S
   ```

4. **Définir umask à 007 (permissions pour le propriétaire et le groupe, aucune pour les autres) :**
   ```csh
   umask 007
   ```

## Tips
- Il est recommandé de vérifier la valeur de `umask` avant de créer des fichiers importants pour s'assurer que les permissions sont conformes à vos attentes.
- Utilisez `umask -S` pour comprendre facilement les permissions actuelles sous une forme plus lisible.
- Pensez à définir `umask` dans votre fichier de configuration de shell (comme `.cshrc`) pour appliquer vos préférences de permissions par défaut à chaque session.