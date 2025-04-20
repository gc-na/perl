# [Linux] C Shell (csh) tmux : Gestion des sessions de terminal

## Overview
La commande `tmux` est un multiplexeur de terminal qui permet aux utilisateurs de créer, gérer et naviguer entre plusieurs sessions de terminal dans une seule fenêtre. Cela est particulièrement utile pour les utilisateurs qui souhaitent exécuter plusieurs processus simultanément ou maintenir des sessions actives même après la déconnexion.

## Usage
La syntaxe de base de la commande `tmux` est la suivante :

```bash
tmux [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `tmux` :

- `new`: Crée une nouvelle session.
- `attach`: Attache une session existante.
- `list-sessions`: Affiche toutes les sessions en cours.
- `kill-session`: Termine une session spécifiée.
- `detach`: Détache la session en cours.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `tmux` :

1. **Créer une nouvelle session** :
   ```bash
   tmux new -s ma_session
   ```

2. **Attacher une session existante** :
   ```bash
   tmux attach -t ma_session
   ```

3. **Lister toutes les sessions** :
   ```bash
   tmux list-sessions
   ```

4. **Détacher la session en cours** :
   ```bash
   Ctrl + b, d
   ```

5. **Terminer une session** :
   ```bash
   tmux kill-session -t ma_session
   ```

## Tips
- Utilisez des noms de session significatifs pour faciliter la gestion de plusieurs sessions.
- Familiarisez-vous avec les raccourcis clavier de `tmux` pour une navigation plus rapide.
- Pensez à sauvegarder votre travail avant de détacher ou de terminer des sessions pour éviter toute perte de données.