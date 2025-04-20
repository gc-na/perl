# [Linux] C Shell (csh) docker-compose : Gérer des applications multi-conteneurs

## Overview
La commande `docker-compose` est un outil qui permet de définir et de gérer des applications composées de plusieurs conteneurs Docker. Grâce à un fichier de configuration, généralement nommé `docker-compose.yml`, vous pouvez facilement orchestrer le déploiement et la gestion de vos services.

## Usage
La syntaxe de base de la commande `docker-compose` est la suivante :

```bash
docker-compose [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `docker-compose` :

- `up` : Démarre les conteneurs définis dans le fichier `docker-compose.yml`.
- `down` : Arrête et supprime les conteneurs, les réseaux et les volumes créés par `up`.
- `build` : Construit ou reconstruit les services définis dans le fichier.
- `logs` : Affiche les journaux des conteneurs en cours d'exécution.
- `ps` : Affiche l'état des conteneurs gérés par `docker-compose`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `docker-compose` :

1. **Démarrer les services** :
   ```bash
   docker-compose up
   ```

2. **Démarrer les services en arrière-plan** :
   ```bash
   docker-compose up -d
   ```

3. **Arrêter et supprimer les conteneurs** :
   ```bash
   docker-compose down
   ```

4. **Construire les services** :
   ```bash
   docker-compose build
   ```

5. **Afficher les journaux des services** :
   ```bash
   docker-compose logs
   ```

6. **Afficher l'état des conteneurs** :
   ```bash
   docker-compose ps
   ```

## Tips
- Utilisez l'option `-d` pour exécuter vos conteneurs en mode détaché, ce qui vous permet de continuer à utiliser votre terminal.
- Assurez-vous que votre fichier `docker-compose.yml` est correctement configuré pour éviter des erreurs lors du démarrage des services.
- N'hésitez pas à utiliser des alias dans votre shell pour simplifier les commandes que vous utilisez fréquemment avec `docker-compose`.