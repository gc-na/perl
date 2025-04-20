# [Linux] C Shell (csh) update-rc.d : Gérer les scripts d'initialisation

## Overview
La commande `update-rc.d` est utilisée sous Linux pour gérer les scripts d'initialisation des services. Elle permet d'ajouter, de supprimer ou de modifier la façon dont les services sont lancés au démarrage du système.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
update-rc.d [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `update-rc.d` :

- `defaults` : Ajoute les scripts avec les niveaux d'exécution par défaut.
- `remove` : Supprime le script d'initialisation du système.
- `enable` : Active le script pour qu'il soit exécuté au démarrage.
- `disable` : Désactive le script pour qu'il ne soit pas exécuté au démarrage.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `update-rc.d` :

1. **Ajouter un script d'initialisation avec les paramètres par défaut :**

   ```csh
   update-rc.d mon_service defaults
   ```

2. **Supprimer un script d'initialisation :**

   ```csh
   update-rc.d mon_service remove
   ```

3. **Activer un script d'initialisation :**

   ```csh
   update-rc.d mon_service enable
   ```

4. **Désactiver un script d'initialisation :**

   ```csh
   update-rc.d mon_service disable
   ```

## Tips
- Assurez-vous d'avoir les droits d'administrateur pour exécuter `update-rc.d`.
- Vérifiez toujours les niveaux d'exécution pour vous assurer que le service démarre au bon moment.
- Utilisez `man update-rc.d` pour consulter la documentation complète et obtenir plus d'informations sur les options disponibles.