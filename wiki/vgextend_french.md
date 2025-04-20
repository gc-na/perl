# [Linux] C Shell (csh) vgextend : Ajouter des volumes à un groupe de volumes

## Overview
La commande `vgextend` est utilisée pour ajouter un ou plusieurs volumes physiques à un groupe de volumes (VG) dans un système de gestion de volumes logiques (LVM). Cela permet d'augmenter la capacité de stockage disponible dans le groupe de volumes.

## Usage
La syntaxe de base de la commande `vgextend` est la suivante :

```bash
vgextend [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `vgextend` :

- `-f` : Force l'ajout des volumes même si cela pourrait entraîner des problèmes.
- `-n` : Ne pas mettre à jour les métadonnées du groupe de volumes.
- `-s` : Spécifie la taille des segments lors de l'ajout de nouveaux volumes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `vgextend` :

1. Ajouter un volume physique à un groupe de volumes :

```bash
vgextend mon_groupe_de_volumes /dev/sdb1
```

2. Ajouter plusieurs volumes physiques à un groupe de volumes :

```bash
vgextend mon_groupe_de_volumes /dev/sdb1 /dev/sdc1
```

3. Forcer l'ajout d'un volume physique :

```bash
vgextend -f mon_groupe_de_volumes /dev/sdd1
```

## Tips
- Assurez-vous que le volume physique que vous ajoutez est correctement initialisé avec `pvcreate`.
- Vérifiez l'espace disponible dans le groupe de volumes après l'ajout avec `vgdisplay`.
- Utilisez `lvextend` après `vgextend` pour augmenter la taille des volumes logiques si nécessaire.