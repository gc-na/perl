# [Linux] C Shell (csh) 7z Utilisation : Compresser et décompresser des fichiers

## Overview
La commande `7z` est un utilitaire de compression et de décompression de fichiers qui fait partie de l'outil 7-Zip. Elle permet de créer des archives compressées dans divers formats, ainsi que d'extraire des fichiers d'archives existantes.

## Usage
La syntaxe de base de la commande `7z` est la suivante :

```
7z [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `7z` :

- `a` : Ajouter des fichiers à une archive.
- `x` : Extraire des fichiers d'une archive.
- `l` : Lister le contenu d'une archive.
- `d` : Supprimer des fichiers d'une archive.
- `t` : Tester l'intégrité d'une archive.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `7z` :

### Créer une archive
Pour créer une archive nommée `archive.7z` contenant tous les fichiers du répertoire courant :

```bash
7z a archive.7z *
```

### Extraire une archive
Pour extraire le contenu d'une archive `archive.7z` dans le répertoire courant :

```bash
7z x archive.7z
```

### Lister le contenu d'une archive
Pour afficher la liste des fichiers contenus dans `archive.7z` :

```bash
7z l archive.7z
```

### Supprimer un fichier d'une archive
Pour supprimer un fichier nommé `fichier.txt` de `archive.7z` :

```bash
7z d archive.7z fichier.txt
```

### Tester l'intégrité d'une archive
Pour vérifier si `archive.7z` est intacte :

```bash
7z t archive.7z
```

## Tips
- Utilisez des chemins relatifs ou absolus pour spécifier les fichiers et les répertoires lors de la création ou de l'extraction d'archives.
- Pensez à utiliser l'option `-p` pour protéger vos archives par mot de passe.
- Vérifiez régulièrement l'intégrité de vos archives avec l'option `t` pour éviter toute perte de données.