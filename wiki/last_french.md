# [Linux] C Shell (csh) last : afficher les connexions précédentes des utilisateurs

## Overview
La commande `last` dans C Shell (csh) est utilisée pour afficher les connexions précédentes des utilisateurs sur le système. Elle lit le fichier de journalisation des connexions et fournit des informations sur les utilisateurs qui se sont connectés et déconnectés, ainsi que sur les heures de connexion.

## Usage
La syntaxe de base de la commande `last` est la suivante :

```
last [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `last` :

- `-n [nombre]` : Affiche les derniers enregistrements de connexion, où `[nombre]` spécifie combien d'entrées afficher.
- `-R` : N'affiche pas le nom d'hôte des connexions.
- `-a` : Affiche l'adresse IP ou le nom d'hôte de la connexion à la fin de chaque ligne.
- `-f [fichier]` : Utilise un fichier de journalisation spécifique au lieu du fichier par défaut.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `last` :

1. Afficher toutes les connexions précédentes :
   ```csh
   last
   ```

2. Afficher les 5 dernières connexions :
   ```csh
   last -n 5
   ```

3. Afficher les connexions sans le nom d'hôte :
   ```csh
   last -R
   ```

4. Afficher les connexions avec l'adresse IP :
   ```csh
   last -a
   ```

5. Utiliser un fichier de journalisation spécifique :
   ```csh
   last -f /var/log/wtmp.1
   ```

## Tips
- Utilisez l'option `-n` pour limiter le nombre d'entrées affichées, ce qui peut être utile pour des systèmes avec de nombreux utilisateurs.
- Combinez les options pour personnaliser la sortie selon vos besoins, par exemple, `last -n 10 -a` pour afficher les 10 dernières connexions avec les adresses IP.
- Pensez à vérifier régulièrement les connexions pour surveiller l'activité des utilisateurs sur le système.