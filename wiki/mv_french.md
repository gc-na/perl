# [Linux] C Shell (csh) mv Utilisation : Déplacer ou renommer des fichiers

## Overview
La commande `mv` est utilisée dans le C Shell pour déplacer ou renommer des fichiers et des répertoires. Elle permet de changer l'emplacement d'un fichier ou de modifier son nom sans créer de copie.

## Usage
La syntaxe de base de la commande `mv` est la suivante :

```csh
mv [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `mv` :

- `-i` : Demande une confirmation avant d'écraser un fichier existant.
- `-u` : Déplace le fichier uniquement si la source est plus récente que la destination ou si la destination n'existe pas.
- `-v` : Affiche des informations détaillées sur les fichiers déplacés.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mv` :

1. **Déplacer un fichier vers un autre répertoire :**
   ```csh
   mv fichier.txt /chemin/vers/nouveau/répertoire/
   ```

2. **Renommer un fichier :**
   ```csh
   mv ancien_nom.txt nouveau_nom.txt
   ```

3. **Déplacer plusieurs fichiers vers un répertoire :**
   ```csh
   mv fichier1.txt fichier2.txt /chemin/vers/nouveau/répertoire/
   ```

4. **Déplacer un fichier avec confirmation :**
   ```csh
   mv -i fichier.txt /chemin/vers/nouveau/répertoire/
   ```

5. **Déplacer un fichier uniquement s'il est plus récent :**
   ```csh
   mv -u fichier.txt /chemin/vers/nouveau/répertoire/
   ```

## Tips
- Utilisez l'option `-i` pour éviter d'écraser accidentellement des fichiers importants.
- Vérifiez toujours le chemin de destination pour éviter de déplacer des fichiers dans des emplacements inattendus.
- Pour une meilleure visibilité, combinez l'option `-v` avec d'autres options afin de voir ce qui se passe lors du déplacement.