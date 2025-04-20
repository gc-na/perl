# [Linux] C Shell (csh) vgcreate : Créer un groupe de volumes

## Overview
La commande `vgcreate` est utilisée pour créer un groupe de volumes dans le système de gestion de volumes logiques (LVM) sous Linux. Cela permet de regrouper plusieurs volumes physiques en une seule unité logique, facilitant ainsi la gestion de l'espace de stockage.

## Usage
La syntaxe de base de la commande `vgcreate` est la suivante :

```bash
vgcreate [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `vgcreate` :

- `-n, --name`: Spécifie le nom du groupe de volumes à créer.
- `-p, --max-pv`: Définit le nombre maximum de volumes physiques pouvant être ajoutés au groupe.
- `-s, --stripes`: Définit le nombre de bandes à utiliser pour le groupe de volumes.
- `-f, --force`: Force la création du groupe de volumes même si des erreurs sont détectées.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `vgcreate` :

1. **Créer un groupe de volumes simple :**
   ```bash
   vgcreate mon_groupe /dev/sda1 /dev/sda2
   ```

2. **Créer un groupe de volumes avec un nom spécifique :**
   ```bash
   vgcreate -n mon_groupe /dev/sdb1 /dev/sdb2
   ```

3. **Créer un groupe de volumes avec un nombre maximum de volumes physiques :**
   ```bash
   vgcreate -p 10 mon_groupe /dev/sdc1
   ```

4. **Forcer la création d'un groupe de volumes :**
   ```bash
   vgcreate -f mon_groupe /dev/sdd1
   ```

## Tips
- Assurez-vous que les volumes physiques que vous souhaitez ajouter au groupe de volumes sont disponibles et non montés.
- Vérifiez l'espace disponible sur les volumes physiques avant de créer un groupe de volumes pour éviter des erreurs.
- Utilisez la commande `vgs` après la création pour vérifier que votre groupe de volumes a été créé avec succès.