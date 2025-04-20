# [Linux] C Shell (csh) docker utilisation : Gestion des conteneurs

## Overview
La commande `docker` est utilisée pour gérer des conteneurs, qui sont des environnements légers et portables permettant d'exécuter des applications de manière isolée. Docker facilite le déploiement, la gestion et la mise à l'échelle d'applications dans des conteneurs.

## Usage
La syntaxe de base de la commande `docker` est la suivante :

```
docker [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `docker` :

- `run` : Crée et exécute un conteneur à partir d'une image spécifiée.
- `ps` : Affiche les conteneurs en cours d'exécution.
- `stop` : Arrête un conteneur en cours d'exécution.
- `rm` : Supprime un conteneur arrêté.
- `images` : Liste toutes les images disponibles sur le système.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `docker` :

1. **Exécuter un conteneur à partir d'une image :**
   ```bash
   docker run hello-world
   ```

2. **Lister les conteneurs en cours d'exécution :**
   ```bash
   docker ps
   ```

3. **Arrêter un conteneur :**
   ```bash
   docker stop <container_id>
   ```

4. **Supprimer un conteneur arrêté :**
   ```bash
   docker rm <container_id>
   ```

5. **Lister toutes les images disponibles :**
   ```bash
   docker images
   ```

## Tips
- Utilisez `docker-compose` pour gérer des applications multi-conteneurs de manière plus simple.
- Gardez vos images à jour en utilisant `docker pull` régulièrement.
- Nommez vos conteneurs et images de manière descriptive pour faciliter la gestion et l'identification.