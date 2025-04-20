# [Linux] C Shell (csh) nice : Ajuster la priorité des processus

## Overview
La commande `nice` dans le C Shell (csh) permet de modifier la priorité d'exécution des processus. En utilisant `nice`, vous pouvez exécuter des commandes avec une priorité plus basse ou plus élevée, ce qui influence la quantité de ressources CPU allouées à ces processus.

## Usage
La syntaxe de base de la commande `nice` est la suivante :

```csh
nice [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `nice` :

- `-n [valeur]` : Définit la valeur de "niceness" du processus. Une valeur positive diminue la priorité, tandis qu'une valeur négative l'augmente.
- `-h` : Affiche l'aide et les options disponibles pour la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `nice` :

1. Exécuter une commande avec une priorité plus basse :
   ```csh
   nice -n 10 myscript.sh
   ```

2. Exécuter un programme avec une priorité normale :
   ```csh
   nice myprogram
   ```

3. Exécuter une commande avec une priorité plus élevée (nécessite des privilèges administratifs) :
   ```csh
   sudo nice -n -5 mycriticaltask
   ```

## Tips
- Utilisez `nice` pour éviter que des processus gourmands en ressources n'affectent les performances d'autres tâches importantes.
- Vérifiez la priorité actuelle d'un processus avec la commande `ps` pour décider si vous devez utiliser `nice`.
- Soyez prudent lorsque vous augmentez la priorité d'un processus, car cela peut affecter négativement le système si trop de ressources sont allouées à une seule tâche.