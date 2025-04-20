# [Linux] C Shell (csh) dirname : [extraire le nom de répertoire]

## Overview
La commande `dirname` est utilisée pour extraire le nom du répertoire d'un chemin de fichier donné. Elle renvoie la partie du chemin qui précède le nom du fichier, ce qui est utile pour manipuler des chemins dans des scripts ou des commandes.

## Usage
La syntaxe de base de la commande `dirname` est la suivante :

```csh
dirname [options] [arguments]
```

## Common Options
- `-z` : Traite les chemins vides comme des chaînes vides.
- `--help` : Affiche l'aide sur l'utilisation de la commande.
- `--version` : Affiche la version de la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `dirname` :

1. Extraire le répertoire d'un chemin de fichier :

```csh
dirname /home/user/documents/file.txt
```
*Sortie :* `/home/user/documents`

2. Utiliser dirname avec un chemin relatif :

```csh
dirname ./images/photo.jpg
```
*Sortie :* `./images`

3. Traiter un chemin vide :

```csh
dirname ""
```
*Sortie :* `.` (représente le répertoire courant)

4. Extraire le répertoire d'un chemin absolu :

```csh
dirname /usr/local/bin/script.sh
```
*Sortie :* `/usr/local/bin`

## Tips
- Utilisez `dirname` dans des scripts pour manipuler des chemins de fichiers de manière dynamique.
- Combinez `dirname` avec d'autres commandes comme `basename` pour obtenir à la fois le répertoire et le nom de fichier d'un chemin.
- Faites attention aux chemins relatifs et absolus pour éviter des résultats inattendus.