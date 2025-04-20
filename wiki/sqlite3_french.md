# [Linux] C Shell (csh) sqlite3 Utilisation : Interface de ligne de commande pour SQLite

## Overview
La commande `sqlite3` permet d'interagir avec des bases de données SQLite via une interface en ligne de commande. Elle permet de créer, modifier et interroger des bases de données de manière efficace.

## Usage
La syntaxe de base de la commande `sqlite3` est la suivante :

```bash
sqlite3 [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `sqlite3` :

- `-help` : Affiche l'aide et les options disponibles.
- `-version` : Affiche la version de SQLite.
- `-init <file>` : Exécute les commandes SQL contenues dans le fichier spécifié au démarrage.
- `-batch` : Exécute les commandes en mode batch, idéal pour les scripts.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `sqlite3` :

1. **Créer une nouvelle base de données :**
   ```bash
   sqlite3 ma_base_de_donnees.db
   ```

2. **Exécuter une commande SQL pour créer une table :**
   ```bash
   sqlite3 ma_base_de_donnees.db "CREATE TABLE utilisateurs (id INTEGER PRIMARY KEY, nom TEXT);"
   ```

3. **Insérer des données dans une table :**
   ```bash
   sqlite3 ma_base_de_donnees.db "INSERT INTO utilisateurs (nom) VALUES ('Alice');"
   ```

4. **Interroger des données :**
   ```bash
   sqlite3 ma_base_de_donnees.db "SELECT * FROM utilisateurs;"
   ```

5. **Exporter les résultats d'une requête vers un fichier :**
   ```bash
   sqlite3 ma_base_de_donnees.db "SELECT * FROM utilisateurs;" > utilisateurs.txt
   ```

## Tips
- Utilisez l'option `-init` pour charger des scripts SQL au démarrage, ce qui peut faciliter les configurations répétitives.
- Pensez à sauvegarder régulièrement vos bases de données pour éviter toute perte de données.
- Familiarisez-vous avec les commandes SQL de base pour tirer le meilleur parti de `sqlite3`.