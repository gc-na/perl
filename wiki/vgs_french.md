# [Linux] C Shell (csh) vgs : [afficher des groupes de volumes]

## Overview
La commande `vgs` est utilisée pour afficher des informations sur les groupes de volumes dans un système utilisant LVM (Logical Volume Manager). Elle permet aux utilisateurs de visualiser des détails tels que la taille, l'espace utilisé et l'espace libre des groupes de volumes.

## Usage
La syntaxe de base de la commande `vgs` est la suivante :

```bash
vgs [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `vgs` :

- `-o` : Spécifie les colonnes à afficher.
- `-h` : Affiche l'aide sur l'utilisation de la commande.
- `--units` : Définit les unités pour l'affichage des tailles.
- `-n` : Affiche uniquement les noms des groupes de volumes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `vgs` :

1. **Afficher tous les groupes de volumes :**
   ```bash
   vgs
   ```

2. **Afficher des informations spécifiques sur les groupes de volumes :**
   ```bash
   vgs -o vg_name,lv_count,vg_size
   ```

3. **Afficher les groupes de volumes avec des unités spécifiques :**
   ```bash
   vgs --units m
   ```

4. **Afficher uniquement les noms des groupes de volumes :**
   ```bash
   vgs -n
   ```

## Tips
- Utilisez l'option `-o` pour personnaliser les colonnes affichées selon vos besoins.
- Pour une aide rapide, n'hésitez pas à utiliser l'option `-h`.
- Vérifiez régulièrement l'espace libre dans vos groupes de volumes pour éviter les problèmes de stockage.