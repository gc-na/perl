# [Linux] C Shell (csh) screen <Utilisation équivalente en français> : Gérer des sessions de terminal

## Overview
La commande `screen` permet de créer des sessions de terminal détachées, ce qui permet aux utilisateurs de continuer à exécuter des programmes même après avoir quitté le terminal. Cela est particulièrement utile pour les tâches de longue durée ou lorsque vous devez vous déconnecter d'une session SSH.

## Usage
La syntaxe de base de la commande `screen` est la suivante :

```bash
screen [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `screen` :

- `-S <nom>` : Crée une nouvelle session avec un nom spécifique.
- `-d -r` : Détache une session et la rattache à l'écran actuel.
- `-list` : Affiche la liste des sessions `screen` en cours d'exécution.
- `-X <commande>` : Envoie une commande à une session `screen` existante.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `screen` :

1. **Créer une nouvelle session :**
   ```bash
   screen -S ma_session
   ```

2. **Détacher une session :**
   Appuyez sur `Ctrl + A`, puis `D`.

3. **Lister les sessions en cours :**
   ```bash
   screen -list
   ```

4. **Rattacher une session existante :**
   ```bash
   screen -r ma_session
   ```

5. **Envoyer une commande à une session :**
   ```bash
   screen -S ma_session -X quit
   ```

## Tips
- Nommez vos sessions avec `-S` pour les retrouver facilement.
- Utilisez `Ctrl + A` suivi de `?` pour afficher l'aide des commandes de `screen`.
- Pensez à détacher vos sessions avant de fermer le terminal pour éviter de perdre vos travaux en cours.