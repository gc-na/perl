# [Linux] C Shell (csh) nohup : Exécuter des commandes sans interruption

## Overview
La commande `nohup` permet d'exécuter des processus en arrière-plan sans être interrompus par la déconnexion de l'utilisateur. Cela est particulièrement utile pour les tâches longues qui doivent continuer à s'exécuter même si vous fermez votre terminal.

## Usage
La syntaxe de base de la commande `nohup` est la suivante :

```csh
nohup [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `nohup` :

- `&` : Exécute la commande en arrière-plan.
- `-o` : Spécifie un fichier de sortie pour les messages de sortie standard.
- `-e` : Spécifie un fichier de sortie pour les messages d'erreur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `nohup` :

1. Exécuter un script en arrière-plan :
   ```csh
   nohup ./mon_script.sh &
   ```

2. Exécuter une commande avec redirection de la sortie :
   ```csh
   nohup ls -l > sortie.txt &
   ```

3. Exécuter une commande avec redirection des erreurs :
   ```csh
   nohup ./mon_programme 2> erreurs.txt &
   ```

4. Exécuter une commande sans sortie :
   ```csh
   nohup ./mon_application > /dev/null 2>&1 &
   ```

## Tips
- Utilisez `jobs` pour vérifier les tâches en arrière-plan.
- Pensez à rediriger la sortie et les erreurs pour éviter l'encombrement de votre terminal.
- Assurez-vous que le script ou la commande que vous exécutez est bien testé, car une fois lancé avec `nohup`, il continuera à s'exécuter sans interaction.