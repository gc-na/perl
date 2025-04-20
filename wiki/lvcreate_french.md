# [Linux] C Shell (csh) lvcreate : Créer des volumes logiques

## Overview
La commande `lvcreate` est utilisée pour créer des volumes logiques dans un groupe de volumes sous Linux. Cela permet de gérer l'espace de stockage de manière flexible et efficace.

## Usage
La syntaxe de base de la commande `lvcreate` est la suivante :

```bash
lvcreate [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `lvcreate` :

- `-n` : Spécifie le nom du volume logique à créer.
- `-L` : Définit la taille du volume logique.
- `-l` : Définit la taille du volume logique en unités de "logical extents".
- `-m` : Crée un volume miroir avec le nombre spécifié de copies.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `lvcreate` :

1. **Créer un volume logique de 10 Go :**

   ```bash
   lvcreate -L 10G -n mon_volume logique_vg
   ```

2. **Créer un volume logique de 5 extents :**

   ```bash
   lvcreate -l 5 -n mon_volume logique_vg
   ```

3. **Créer un volume miroir :**

   ```bash
   lvcreate -m 1 -L 20G -n volume_miroir logique_vg
   ```

4. **Créer un volume logique avec un système de fichiers :**

   ```bash
   lvcreate -L 15G -n volume_fs logique_vg
   mkfs.ext4 /dev/logique_vg/volume_fs
   ```

## Tips
- Toujours vérifier l'espace disponible dans le groupe de volumes avant de créer un nouveau volume logique.
- Utilisez des noms descriptifs pour vos volumes logiques afin de faciliter leur identification.
- Pensez à sauvegarder vos données avant de manipuler des volumes logiques, surtout lors de l'utilisation de volumes miroirs.