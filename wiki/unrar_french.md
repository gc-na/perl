# [Linux] C Shell (csh) unrar : Extraire des fichiers RAR

## Overview
La commande `unrar` est utilisée pour extraire des fichiers compressés au format RAR. Elle permet de décompresser des archives RAR et d'accéder aux fichiers qu'elles contiennent.

## Usage
La syntaxe de base de la commande `unrar` est la suivante :

```csh
unrar [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `unrar` :

- `x` : Extraire tous les fichiers de l'archive dans le répertoire courant.
- `e` : Extraire tous les fichiers de l'archive sans recréer la structure de répertoires.
- `l` : Lister le contenu de l'archive sans l'extraire.
- `v` : Afficher des informations détaillées sur les fichiers extraits.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `unrar` :

1. **Extraire tous les fichiers d'une archive RAR :**
   ```csh
   unrar x archive.rar
   ```

2. **Extraire tous les fichiers d'une archive RAR sans structure de répertoires :**
   ```csh
   unrar e archive.rar
   ```

3. **Lister le contenu d'une archive RAR :**
   ```csh
   unrar l archive.rar
   ```

4. **Afficher des informations détaillées sur les fichiers dans une archive RAR :**
   ```csh
   unrar v archive.rar
   ```

## Tips
- Assurez-vous d'avoir installé `unrar` sur votre système avant de l'utiliser.
- Utilisez l'option `-o+` pour écraser les fichiers existants sans confirmation lors de l'extraction.
- Pour une utilisation fréquente, envisagez de créer des alias dans votre fichier de configuration csh pour simplifier les commandes.