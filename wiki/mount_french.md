# [Linux] C Shell (csh) mount : Monter des systèmes de fichiers

## Overview
La commande `mount` est utilisée pour monter des systèmes de fichiers dans le système d'exploitation. Cela permet d'accéder aux données stockées sur des périphériques de stockage tels que des disques durs, des clés USB ou des partitions.

## Usage
La syntaxe de base de la commande `mount` est la suivante :

```
mount [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `mount` :

- `-t type` : Spécifie le type de système de fichiers à monter (par exemple, ext4, ntfs).
- `-o options` : Permet de spécifier des options supplémentaires pour le montage, comme `ro` pour lecture seule ou `rw` pour lecture-écriture.
- `-a` : Monte tous les systèmes de fichiers mentionnés dans le fichier `/etc/fstab`.
- `-r` : Monte le système de fichiers en mode lecture seule.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mount` :

1. Monter un disque dur avec un type de système de fichiers spécifié :
   ```bash
   mount -t ext4 /dev/sda1 /mnt
   ```

2. Monter une clé USB en lecture-écriture :
   ```bash
   mount -o rw /dev/sdb1 /media/usb
   ```

3. Monter tous les systèmes de fichiers définis dans `/etc/fstab` :
   ```bash
   mount -a
   ```

4. Monter un système de fichiers en mode lecture seule :
   ```bash
   mount -o ro /dev/sdc1 /mnt/readonly
   ```

## Tips
- Assurez-vous d'avoir les permissions nécessaires pour monter des systèmes de fichiers, souvent requises pour l'utilisateur root.
- Vérifiez toujours que le point de montage (le répertoire où vous montez) est vide avant de monter un nouveau système de fichiers.
- Utilisez la commande `umount` pour démonter un système de fichiers lorsque vous avez terminé d'y accéder.