# [Linux] C Shell (csh) lvextend : Étendre la taille d'un volume logique

## Overview
La commande `lvextend` est utilisée pour augmenter la taille d'un volume logique dans un système de gestion de volumes logiques (LVM). Cela permet d'augmenter l'espace de stockage disponible pour un système de fichiers ou une application sans avoir à recréer le volume.

## Usage
La syntaxe de base de la commande `lvextend` est la suivante :

```bash
lvextend [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `lvextend` :

- `-L +size` : Ajoute une taille spécifiée au volume logique.
- `-l +number` : Ajoute un nombre spécifié d'unités de logique (extents) au volume.
- `-r` : Redimensionne automatiquement le système de fichiers après l'extension du volume.
- `-n new_name` : Renomme le volume logique lors de l'extension.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `lvextend` :

1. **Augmenter la taille d'un volume logique de 10 Go :**

   ```bash
   lvextend -L +10G /dev/vg01/lv01
   ```

2. **Ajouter 5 unités de logique au volume :**

   ```bash
   lvextend -l +5 /dev/vg01/lv01
   ```

3. **Étendre le volume et redimensionner le système de fichiers en même temps :**

   ```bash
   lvextend -r -L +20G /dev/vg01/lv01
   ```

4. **Renommer un volume logique tout en l'augmentant :**

   ```bash
   lvextend -n new_lv_name -L +15G /dev/vg01/lv01
   ```

## Tips
- Assurez-vous que l'espace disponible dans le groupe de volumes est suffisant avant d'utiliser `lvextend`.
- Utilisez l'option `-r` pour simplifier le processus de redimensionnement du système de fichiers après l'extension.
- Vérifiez toujours l'état du volume logique après l'extension avec la commande `lvdisplay` pour vous assurer que les modifications ont été appliquées correctement.