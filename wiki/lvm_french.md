# [Linux] C Shell (csh) lvm Utilisation : Gestion des volumes logiques

## Overview
La commande `lvm` (Logical Volume Manager) permet de gérer des volumes logiques sur un système Linux. Elle offre des fonctionnalités pour créer, supprimer, redimensionner et gérer des volumes logiques, facilitant ainsi la gestion de l'espace disque.

## Usage
La syntaxe de base de la commande `lvm` est la suivante :

```csh
lvm [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `lvm` :

- `create` : Crée un nouveau volume logique.
- `remove` : Supprime un volume logique existant.
- `resize` : Redimensionne un volume logique.
- `list` : Affiche la liste des volumes logiques.
- `activate` : Active un volume logique.
- `deactivate` : Désactive un volume logique.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `lvm` :

### Créer un volume logique
```csh
lvm create -n mon_volume -L 10G mon_groupe
```

### Supprimer un volume logique
```csh
lvm remove mon_volume
```

### Redimensionner un volume logique
```csh
lvm resize -L +5G mon_volume
```

### Lister les volumes logiques
```csh
lvm list
```

### Activer un volume logique
```csh
lvm activate mon_volume
```

### Désactiver un volume logique
```csh
lvm deactivate mon_volume
```

## Tips
- Toujours vérifier l'état des volumes logiques avant d'effectuer des modifications avec `lvm list`.
- Utilisez des noms significatifs pour vos volumes logiques afin de faciliter leur identification.
- Faites des sauvegardes régulières de vos données avant de redimensionner ou de supprimer des volumes logiques.