# [Linux] C Shell (csh) systemctl : Gérer les services système

## Overview
La commande `systemctl` est utilisée pour examiner et contrôler le système d'initialisation `systemd`. Elle permet de gérer les services, les unités et l'état du système.

## Usage
La syntaxe de base de la commande `systemctl` est la suivante :

```bash
systemctl [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `systemctl` :

- `start` : Démarre un service.
- `stop` : Arrête un service.
- `restart` : Redémarre un service.
- `status` : Affiche l'état d'un service.
- `enable` : Active un service au démarrage.
- `disable` : Désactive un service au démarrage.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `systemctl` :

- Pour démarrer un service, par exemple `nginx` :

```bash
systemctl start nginx
```

- Pour arrêter un service, par exemple `apache2` :

```bash
systemctl stop apache2
```

- Pour redémarrer un service, par exemple `mysql` :

```bash
systemctl restart mysql
```

- Pour vérifier l'état d'un service, par exemple `ssh` :

```bash
systemctl status ssh
```

- Pour activer un service au démarrage, par exemple `cron` :

```bash
systemctl enable cron
```

- Pour désactiver un service au démarrage, par exemple `bluetooth` :

```bash
systemctl disable bluetooth
```

## Tips
- Toujours vérifier l'état d'un service après l'avoir démarré ou arrêté pour s'assurer qu'il fonctionne comme prévu.
- Utiliser `systemctl list-units` pour obtenir une liste de tous les services et leurs états.
- Pour des opérations nécessitant des privilèges administratifs, n'oubliez pas d'utiliser `sudo` avant la commande `systemctl`.