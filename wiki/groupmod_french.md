# [Linux] C Shell (csh) groupmod : Modifier les groupes d'utilisateurs

## Overview
La commande `groupmod` est utilisée pour modifier les propriétés d'un groupe d'utilisateurs existant dans un système Linux. Cela inclut des actions telles que changer le nom du groupe ou son identifiant (GID).

## Usage
La syntaxe de base de la commande `groupmod` est la suivante :

```bash
groupmod [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `groupmod` :

- `-n, --new-name NOM` : Change le nom du groupe.
- `-g, --gid GID` : Change l'identifiant du groupe (GID).
- `-h, --help` : Affiche l'aide et les options disponibles.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `groupmod` :

1. **Changer le nom d'un groupe :**
   ```bash
   groupmod -n nouveau_nom ancien_nom
   ```

2. **Changer l'identifiant d'un groupe :**
   ```bash
   groupmod -g 1001 nom_du_groupe
   ```

3. **Modifier à la fois le nom et le GID d'un groupe :**
   ```bash
   groupmod -n nouveau_nom -g 1002 ancien_nom
   ```

## Tips
- Assurez-vous d'avoir les privilèges nécessaires (généralement en tant que superutilisateur) pour modifier les groupes.
- Vérifiez toujours les groupes existants avec la commande `getent group` avant de faire des modifications pour éviter les conflits.
- Utilisez `groupmod -h` pour obtenir de l'aide sur les options disponibles si vous n'êtes pas sûr de la syntaxe.