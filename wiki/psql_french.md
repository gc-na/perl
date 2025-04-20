# [Linux] C Shell (csh) psql : Exécuter des requêtes SQL

## Overview
La commande `psql` est un outil en ligne de commande pour interagir avec une base de données PostgreSQL. Elle permet d'exécuter des requêtes SQL, de gérer des bases de données et d'effectuer diverses opérations administratives.

## Usage
La syntaxe de base de la commande `psql` est la suivante :

```bash
psql [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `psql` :

- `-h` : Spécifie l'hôte de la base de données.
- `-p` : Définit le port de connexion à la base de données.
- `-U` : Indique le nom d'utilisateur pour se connecter à la base de données.
- `-d` : Spécifie le nom de la base de données à laquelle se connecter.
- `-c` : Permet d'exécuter une commande SQL directement depuis la ligne de commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `psql` :

1. Se connecter à une base de données par défaut :
   ```bash
   psql
   ```

2. Se connecter à une base de données spécifique avec un utilisateur :
   ```bash
   psql -U nom_utilisateur -d nom_base_de_données
   ```

3. Exécuter une commande SQL directement :
   ```bash
   psql -U nom_utilisateur -d nom_base_de_données -c "SELECT * FROM table_exemple;"
   ```

4. Se connecter à une base de données sur un hôte spécifique :
   ```bash
   psql -h hôte_exemple -U nom_utilisateur -d nom_base_de_données
   ```

## Tips
- Utilisez `\?` dans l'interface `psql` pour afficher l'aide et la liste des commandes disponibles.
- Pour quitter `psql`, tapez `\q`.
- Pensez à utiliser des fichiers de script SQL pour exécuter plusieurs commandes à la fois en utilisant `psql -f fichier_script.sql`.