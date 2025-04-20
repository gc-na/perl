# [Linux] C Shell (csh) fdisk Utilisation : Gestion des partitions de disque

## Overview
La commande `fdisk` est utilisée pour manipuler les tables de partitions des disques durs sous les systèmes d'exploitation de type Unix. Elle permet de créer, supprimer, modifier et afficher les partitions sur un disque.

## Usage
La syntaxe de base de la commande `fdisk` est la suivante :

```bash
fdisk [options] [arguments]
```

## Common Options
Voici quelques options courantes de la commande `fdisk` :

- `-l` : Liste toutes les partitions disponibles sur les disques.
- `-u` : Utilise des unités de secteur pour les tailles de partition.
- `-s` : Affiche la taille d'une partition spécifiée.
- `-n` : Crée une nouvelle partition.
- `-d` : Supprime une partition existante.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `fdisk` :

1. **Lister les partitions sur un disque :**
   ```bash
   fdisk -l
   ```

2. **Créer une nouvelle partition :**
   ```bash
   fdisk /dev/sda
   ```
   (Puis, suivez les instructions à l'écran pour créer une nouvelle partition.)

3. **Supprimer une partition :**
   ```bash
   fdisk /dev/sda
   ```
   (Sélectionnez l'option pour supprimer une partition et suivez les instructions.)

4. **Afficher la taille d'une partition spécifique :**
   ```bash
   fdisk -s /dev/sda1
   ```

## Tips
- Toujours faire une sauvegarde des données importantes avant de modifier les partitions.
- Utilisez `fdisk` avec précaution, car des erreurs peuvent entraîner la perte de données.
- Vérifiez le type de partition (MBR ou GPT) avant de faire des modifications, car cela peut affecter la compatibilité avec d'autres systèmes d'exploitation.