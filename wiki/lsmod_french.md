# [Linux] C Shell (csh) lsmod : Afficher les modules du noyau

## Overview
La commande `lsmod` est utilisée pour afficher les modules du noyau actuellement chargés dans le système. Elle fournit une liste des modules, ainsi que des informations sur leur utilisation et leurs dépendances.

## Usage
La syntaxe de base de la commande `lsmod` est la suivante :

```csh
lsmod [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `lsmod` :

- **-h, --help** : Affiche l'aide et les options disponibles pour la commande.
- **-v, --verbose** : Affiche des informations détaillées sur les modules.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `lsmod` :

1. **Afficher tous les modules chargés :**

   ```csh
   lsmod
   ```

2. **Afficher l'aide de la commande :**

   ```csh
   lsmod --help
   ```

3. **Afficher les modules avec des informations détaillées :**

   ```csh
   lsmod --verbose
   ```

## Tips
- Utilisez `lsmod` régulièrement pour surveiller les modules chargés et leur utilisation.
- Combinez `lsmod` avec d'autres commandes comme `modinfo` pour obtenir des informations supplémentaires sur un module spécifique.
- Pensez à vérifier les dépendances des modules pour mieux comprendre leur interconnexion et leur impact sur le système.