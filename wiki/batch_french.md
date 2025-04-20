# [Linux] C Shell (csh) batch : exécuter des commandes en arrière-plan

## Overview
La commande `batch` permet d'exécuter des tâches en arrière-plan à un moment où le système est moins occupé. Elle est particulièrement utile pour les commandes qui nécessitent beaucoup de ressources et qui peuvent être exécutées sans interaction de l'utilisateur.

## Usage
La syntaxe de base de la commande `batch` est la suivante :

```csh
batch [options] [arguments]
```

## Common Options
- `-l` : Utiliser le shell de connexion.
- `-m` : Envoyer un message lorsque le travail est terminé.
- `-q` : Exécuter le travail en mode silencieux.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `batch` :

1. **Exécuter un script à l'heure creuse :**
   ```csh
   echo "sh /chemin/vers/script.sh" | batch
   ```

2. **Envoyer un message à la fin de l'exécution :**
   ```csh
   echo "sh /chemin/vers/script.sh" | batch -m
   ```

3. **Exécuter une commande simple :**
   ```csh
   echo "date >> /chemin/vers/fichier.txt" | batch
   ```

4. **Utiliser le shell de connexion :**
   ```csh
   echo "sh /chemin/vers/script.sh" | batch -l
   ```

## Tips
- Assurez-vous que les scripts ou commandes que vous exécutez avec `batch` ne nécessitent pas d'interaction, car ils s'exécutent sans interface utilisateur.
- Vérifiez régulièrement la file d'attente des travaux en attente avec la commande `atq` pour vous assurer que vos tâches sont planifiées comme prévu.
- Utilisez des chemins absolus dans vos scripts pour éviter les problèmes de chemin d'accès lors de l'exécution en arrière-plan.