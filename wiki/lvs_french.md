# [Linux] C Shell (csh) lvs : afficher les volumes logiques

## Overview
La commande `lvs` est utilisée pour afficher des informations sur les volumes logiques dans un système de gestion de volumes logiques (LVM). Elle permet aux utilisateurs de visualiser des détails tels que la taille, l'état et d'autres attributs des volumes logiques.

## Usage
La syntaxe de base de la commande `lvs` est la suivante :

```bash
lvs [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `lvs` :

- `-o, --units`: Spécifie les unités pour l'affichage des tailles.
- `-a, --all`: Affiche tous les volumes, y compris ceux qui sont inactifs.
- `-f, --full`: Montre toutes les informations disponibles sur les volumes.
- `-S, --select`: Permet de filtrer les volumes affichés selon des critères spécifiques.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `lvs` :

1. Afficher tous les volumes logiques :
   ```bash
   lvs
   ```

2. Afficher des informations détaillées sur tous les volumes logiques, y compris ceux inactifs :
   ```bash
   lvs -a
   ```

3. Afficher les volumes logiques avec des tailles en unités spécifiques (par exemple, mégaoctets) :
   ```bash
   lvs -o +devices --units m
   ```

4. Filtrer les volumes logiques selon des critères spécifiques :
   ```bash
   lvs -S 'lv_size > 10G'
   ```

## Tips
- Utilisez l'option `-o` pour personnaliser les colonnes affichées et obtenir les informations les plus pertinentes pour vos besoins.
- Pensez à combiner `lvs` avec d'autres commandes LVM pour une gestion plus efficace de vos volumes.
- Vérifiez régulièrement l'état de vos volumes logiques pour anticiper d'éventuels problèmes de capacité.