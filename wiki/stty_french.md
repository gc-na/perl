# [Linux] C Shell (csh) stty : Configurer les paramètres du terminal

## Overview
La commande `stty` est utilisée pour modifier et afficher les paramètres du terminal dans le shell C. Elle permet de configurer des aspects tels que le contrôle de flux, les caractères spéciaux, et d'autres options de terminal.

## Usage
La syntaxe de base de la commande `stty` est la suivante :

```csh
stty [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `stty` :

- `-a` : Affiche tous les paramètres du terminal.
- `-g` : Affiche les paramètres sous forme de chaîne de caractères, pouvant être réutilisés.
- `erase` : Définit le caractère utilisé pour effacer le dernier caractère (généralement `^H` ou `DEL`).
- `kill` : Définit le caractère utilisé pour supprimer toute la ligne (généralement `^U`).
- `intr` : Définit le caractère utilisé pour interrompre un processus (généralement `^C`).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `stty` :

1. **Afficher tous les paramètres du terminal :**
   ```csh
   stty -a
   ```

2. **Modifier le caractère d'effacement :**
   ```csh
   stty erase ^H
   ```

3. **Modifier le caractère de suppression de ligne :**
   ```csh
   stty kill ^U
   ```

4. **Afficher les paramètres sous forme de chaîne :**
   ```csh
   stty -g
   ```

5. **Configurer le caractère d'interruption :**
   ```csh
   stty intr ^C
   ```

## Tips
- Utilisez `stty -a` pour vérifier rapidement tous les paramètres actuels de votre terminal.
- Soyez prudent lors de la modification des caractères spéciaux, car cela peut affecter votre capacité à interagir avec le terminal.
- Vous pouvez sauvegarder les paramètres actuels en utilisant `stty -g` avant de faire des modifications, afin de pouvoir les restaurer plus tard.