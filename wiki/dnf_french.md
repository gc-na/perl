# [Linux] C Shell (csh) dnf : Gestionnaire de paquets pour les distributions basées sur RPM

## Overview
La commande `dnf` (Dandified YUM) est un gestionnaire de paquets utilisé pour installer, mettre à jour et gérer les logiciels sur les distributions Linux basées sur RPM, comme Fedora et CentOS. Elle remplace l'ancien gestionnaire YUM et offre une interface plus moderne et des fonctionnalités améliorées.

## Usage
La syntaxe de base de la commande `dnf` est la suivante :

```bash
dnf [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `dnf` :

- `install` : Installe un ou plusieurs paquets.
- `remove` : Supprime un ou plusieurs paquets.
- `update` : Met à jour tous les paquets installés vers la dernière version.
- `search` : Recherche des paquets dans les dépôts.
- `info` : Affiche des informations sur un paquet spécifique.
- `list` : Liste tous les paquets installés ou disponibles.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `dnf` :

- Installer un paquet :
  ```bash
  dnf install nom_du_paquet
  ```

- Supprimer un paquet :
  ```bash
  dnf remove nom_du_paquet
  ```

- Mettre à jour tous les paquets installés :
  ```bash
  dnf update
  ```

- Rechercher un paquet :
  ```bash
  dnf search nom_du_paquet
  ```

- Afficher des informations sur un paquet :
  ```bash
  dnf info nom_du_paquet
  ```

## Tips
- Toujours exécuter `dnf update` régulièrement pour garder votre système à jour et sécurisé.
- Utilisez `dnf history` pour voir l'historique des transactions et restaurer des installations précédentes si nécessaire.
- Pour éviter les conflits de dépendances, essayez d'installer des paquets en une seule commande plutôt que de les installer un par un.