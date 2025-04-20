# [Linux] C Shell (csh) ss : Afficher les connexions réseau

## Overview
La commande `ss` est utilisée pour afficher des informations sur les connexions réseau, les sockets et les statistiques de réseau. Elle est souvent utilisée pour diagnostiquer des problèmes de réseau ou pour surveiller l'état des connexions.

## Usage
La syntaxe de base de la commande `ss` est la suivante :

```csh
ss [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `ss` :

- `-t` : Affiche uniquement les connexions TCP.
- `-u` : Affiche uniquement les connexions UDP.
- `-l` : Affiche uniquement les sockets à l'écoute.
- `-p` : Affiche les processus utilisant les sockets.
- `-n` : Affiche les adresses et numéros de port sous forme numérique.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `ss` :

1. Afficher toutes les connexions TCP :
   ```csh
   ss -t
   ```

2. Afficher toutes les connexions UDP :
   ```csh
   ss -u
   ```

3. Afficher les sockets à l'écoute :
   ```csh
   ss -l
   ```

4. Afficher les connexions avec les processus associés :
   ```csh
   ss -p
   ```

5. Afficher les connexions avec des adresses numériques :
   ```csh
   ss -n
   ```

## Tips
- Utilisez `ss -tuln` pour obtenir une vue d'ensemble des connexions TCP et UDP à l'écoute avec des adresses numériques.
- Combinez plusieurs options pour affiner vos résultats, par exemple `ss -tunlp` pour afficher les connexions TCP et UDP avec les processus.
- Pensez à exécuter la commande avec des privilèges élevés (par exemple, en utilisant `sudo`) pour voir toutes les connexions, y compris celles des autres utilisateurs.