# [Linux] C Shell (csh) parted : Gestion des partitions de disque

## Overview
La commande `parted` est un outil utilisé pour gérer les partitions de disque. Elle permet de créer, supprimer, redimensionner et manipuler les partitions sur des disques durs et des périphériques de stockage.

## Usage
La syntaxe de base de la commande `parted` est la suivante :

```bash
parted [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `parted` :

- `-s` : Exécute `parted` en mode silencieux, sans afficher d'invite.
- `-m` : Affiche les informations sur les partitions dans un format lisible par machine.
- `--script` : Exécute la commande sans demander de confirmation.
- `mkpart` : Crée une nouvelle partition.
- `rm` : Supprime une partition existante.
- `resizepart` : Redimensionne une partition existante.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `parted` :

1. **Lancer parted sur un disque spécifique :**
   ```bash
   parted /dev/sda
   ```

2. **Créer une nouvelle partition :**
   ```bash
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Supprimer une partition :**
   ```bash
   parted /dev/sda rm 1
   ```

4. **Redimensionner une partition :**
   ```bash
   parted /dev/sda resizepart 1 200MiB
   ```

5. **Afficher la table des partitions :**
   ```bash
   parted /dev/sda print
   ```

## Tips
- Toujours sauvegarder vos données avant de manipuler les partitions pour éviter toute perte accidentelle.
- Utilisez l'option `--script` si vous souhaitez automatiser des scripts sans intervention manuelle.
- Vérifiez toujours la table des partitions après avoir effectué des modifications pour vous assurer que tout est en ordre.