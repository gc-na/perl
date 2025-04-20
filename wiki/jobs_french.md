# [Linux] C Shell (csh) jobs : Gérer les tâches en arrière-plan

## Overview
La commande `jobs` dans C Shell (csh) permet de lister les tâches en cours d'exécution dans le shell actuel. Elle affiche les processus qui s'exécutent en arrière-plan ou qui sont suspendus, ce qui est utile pour gérer plusieurs tâches simultanément.

## Usage
La syntaxe de base de la commande `jobs` est la suivante :

```csh
jobs [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `jobs` :

- `-l` : Affiche les numéros de processus (PID) en plus des informations sur les tâches.
- `-n` : Affiche uniquement les tâches qui ont changé d'état depuis la dernière exécution de la commande.
- `-p` : Affiche uniquement les numéros de processus des tâches.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `jobs` :

1. **Lister toutes les tâches en cours :**
   ```csh
   jobs
   ```

2. **Lister les tâches avec les numéros de processus :**
   ```csh
   jobs -l
   ```

3. **Afficher uniquement les tâches qui ont changé d'état :**
   ```csh
   jobs -n
   ```

4. **Afficher uniquement les numéros de processus des tâches :**
   ```csh
   jobs -p
   ```

## Tips
- Utilisez `bg` pour reprendre une tâche suspendue en arrière-plan après avoir utilisé `Ctrl+Z`.
- Utilisez `fg` pour ramener une tâche en avant-plan.
- Vérifiez régulièrement vos tâches en cours avec `jobs` pour éviter d'avoir trop de processus en arrière-plan qui pourraient consommer des ressources système.