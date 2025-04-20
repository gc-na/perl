# [Linux] C Shell (csh) bg : Mettre un processus en arrière-plan

## Overview
La commande `bg` dans C Shell (csh) est utilisée pour reprendre un processus suspendu et l'exécuter en arrière-plan. Cela permet à l'utilisateur de continuer à utiliser le terminal tout en laissant le processus s'exécuter.

## Usage
La syntaxe de base de la commande `bg` est la suivante :

```csh
bg [options] [arguments]
```

## Common Options
- `job_id` : Identifiant du travail que vous souhaitez mettre en arrière-plan. Vous pouvez spécifier le numéro de travail précédé d'un `%`, par exemple `%1`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `bg` :

1. **Mettre un processus en arrière-plan**  
   Supposons que vous ayez suspendu un processus en cours d'exécution avec `Ctrl+Z`. Pour le reprendre en arrière-plan, utilisez :
   ```csh
   bg %1
   ```

2. **Mettre un processus en arrière-plan sans spécifier l'identifiant**  
   Si vous n'avez qu'un seul processus suspendu, vous pouvez simplement utiliser :
   ```csh
   bg
   ```

3. **Vérifier les processus en arrière-plan**  
   Pour voir tous les travaux en arrière-plan, utilisez la commande :
   ```csh
   jobs
   ```

## Tips
- Assurez-vous de vérifier les travaux en arrière-plan avec `jobs` pour éviter de perdre le suivi de vos processus.
- Si vous souhaitez ramener un processus en avant-plan, utilisez la commande `fg` suivie de l'identifiant du travail.
- Utilisez `disown` si vous souhaitez que le processus continue à s'exécuter même après la fermeture de votre terminal.