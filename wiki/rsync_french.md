# [Linux] C Shell (csh) rsync : Synchronisation de fichiers

## Overview
La commande `rsync` est utilisée pour synchroniser des fichiers et des répertoires entre deux emplacements, que ce soit localement ou à travers un réseau. Elle est particulièrement efficace car elle ne transfère que les différences entre les fichiers source et destination, ce qui réduit le temps et la bande passante nécessaires.

## Usage
La syntaxe de base de la commande `rsync` est la suivante :

```csh
rsync [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `rsync` :

- `-a` : Archive mode, qui préserve les permissions, les timestamps, et les liens symboliques.
- `-v` : Mode verbeux, pour afficher les fichiers en cours de transfert.
- `-z` : Compression des données pendant le transfert pour économiser la bande passante.
- `-r` : Récursif, pour copier des répertoires et leur contenu.
- `--delete` : Supprime les fichiers dans le répertoire de destination qui ne sont pas présents dans le répertoire source.

## Common Examples
Voici quelques exemples pratiques d'utilisation de `rsync` :

1. **Synchroniser un répertoire local avec un autre répertoire local :**

```csh
rsync -av /chemin/vers/source/ /chemin/vers/destination/
```

2. **Synchroniser un répertoire local avec un répertoire distant :**

```csh
rsync -av /chemin/vers/source/ utilisateur@serveur:/chemin/vers/destination/
```

3. **Synchroniser un répertoire distant avec un répertoire local :**

```csh
rsync -av utilisateur@serveur:/chemin/vers/source/ /chemin/vers/destination/
```

4. **Synchroniser tout en compressant les données :**

```csh
rsync -avz /chemin/vers/source/ utilisateur@serveur:/chemin/vers/destination/
```

5. **Synchroniser en supprimant les fichiers obsolètes dans la destination :**

```csh
rsync -av --delete /chemin/vers/source/ /chemin/vers/destination/
```

## Tips
- Toujours tester vos commandes `rsync` avec l'option `-n` (mode simulation) pour voir ce qui sera transféré sans effectuer de modifications.
- Utilisez des chemins relatifs pour éviter les erreurs de chemin d'accès.
- Pensez à utiliser des clés SSH pour sécuriser vos transferts lorsque vous travaillez avec des serveurs distants.