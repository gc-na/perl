# [Linux] C Shell (csh) shutdown : Arrêter le système

## Overview
La commande `shutdown` est utilisée pour arrêter, redémarrer ou mettre en veille un système. Elle permet aux administrateurs de gérer l'état du système de manière contrôlée et sécurisée.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
shutdown [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande shutdown :

- `-h` : Arrête le système.
- `-r` : Redémarre le système après l'arrêt.
- `-k` : Envoie un message d'avertissement sans réellement arrêter le système.
- `+m` : Planifie l'arrêt dans `m` minutes.
- `hh:mm` : Planifie l'arrêt à une heure spécifique.

## Common Examples
Voici quelques exemples pratiques de la commande shutdown :

1. Pour arrêter le système immédiatement :
   ```csh
   shutdown -h now
   ```

2. Pour redémarrer le système dans 5 minutes :
   ```csh
   shutdown -r +5
   ```

3. Pour envoyer un message d'avertissement sans arrêter le système :
   ```csh
   shutdown -k now "Le système va être arrêté."
   ```

4. Pour planifier un arrêt à 22h00 :
   ```csh
   shutdown -h 22:00
   ```

## Tips
- Toujours avertir les utilisateurs avant d'arrêter le système pour éviter la perte de données.
- Utiliser l'option `-k` pour tester les messages d'avertissement avant un arrêt réel.
- Vérifier les processus en cours pour éviter d'interrompre des tâches critiques.