# [Linux] C Shell (csh) à at : [planifier des tâches]

## Overview
La commande `at` permet de planifier l'exécution de commandes ou de scripts à un moment précis dans le futur. C'est un outil pratique pour automatiser des tâches sans avoir à rester connecté à la session.

## Usage
La syntaxe de base de la commande `at` est la suivante :

```bash
at [options] [arguments]
```

## Common Options
- `-f`: Spécifie un fichier contenant les commandes à exécuter.
- `-m`: Envoie un e-mail lorsque la tâche est terminée, même si la sortie est vide.
- `-q`: Définit la file d'attente à utiliser pour la tâche.
- `-l`: Liste les tâches programmées.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `at` :

1. **Planifier une commande pour s'exécuter à une heure précise :**
   ```bash
   echo "echo 'Bonjour, monde!'" | at 15:00
   ```

2. **Planifier l'exécution d'un script à une date et heure spécifiques :**
   ```bash
   at 2023-10-15 10:30 < mon_script.sh
   ```

3. **Envoyer un e-mail après l'exécution d'une tâche :**
   ```bash
   echo "backup.sh" | at -m now + 1 hour
   ```

4. **Lister les tâches programmées :**
   ```bash
   at -l
   ```

## Tips
- Assurez-vous que le service `atd` est en cours d'exécution pour que les tâches programmées soient exécutées.
- Utilisez `atq` pour vérifier les tâches en attente et `atrm` pour supprimer une tâche spécifique.
- Pensez à rediriger la sortie des commandes vers un fichier pour garder une trace des résultats.