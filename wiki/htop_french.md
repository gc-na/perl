# [Linux] C Shell (csh) htop Utilisation : Afficher et gérer les processus système

## Overview
La commande `htop` est un outil interactif de surveillance des processus qui permet aux utilisateurs de visualiser en temps réel l'utilisation des ressources système, tels que le CPU, la mémoire et les processus en cours d'exécution. Contrairement à la commande `top`, `htop` offre une interface plus conviviale et permet une navigation plus facile à travers les processus.

## Usage
La syntaxe de base de la commande `htop` est la suivante :

```csh
htop [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `htop` :

- `-d <delay>` : Définit le délai entre les mises à jour de l'affichage (en secondes).
- `-u <user>` : Affiche uniquement les processus appartenant à un utilisateur spécifique.
- `-p <pid>` : Affiche uniquement le processus avec l'ID spécifié.
- `--sort-key <key>` : Définit la clé de tri pour les processus (par exemple, `PID`, `MEM`, `CPU`).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `htop` :

1. Lancer `htop` sans options :

   ```csh
   htop
   ```

2. Afficher les processus d'un utilisateur spécifique :

   ```csh
   htop -u nom_utilisateur
   ```

3. Afficher un processus particulier par son ID :

   ```csh
   htop -p 1234
   ```

4. Changer le délai de mise à jour à 2 secondes :

   ```csh
   htop -d 2
   ```

5. Trier les processus par utilisation de la mémoire :

   ```csh
   htop --sort-key MEM
   ```

## Tips
- Utilisez les touches fléchées pour naviguer dans la liste des processus et `F9` pour tuer un processus sélectionné.
- Appuyez sur `F2` pour accéder au menu de configuration et personnaliser l'affichage selon vos préférences.
- Pour quitter `htop`, appuyez sur `q` ou `Ctrl+C`.