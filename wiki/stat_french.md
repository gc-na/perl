# [Linux] C Shell (csh) stat : afficher les informations sur les fichiers

## Overview
La commande `stat` est utilisée pour afficher des informations détaillées sur un fichier ou un répertoire. Ces informations incluent des détails tels que la taille du fichier, les permissions, les dates de modification et d'accès, ainsi que d'autres attributs.

## Usage
La syntaxe de base de la commande `stat` est la suivante :

```csh
stat [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec la commande `stat` :

- `-f` : Affiche les informations dans un format spécifique.
- `-c` : Permet de spécifier un format de sortie personnalisé.
- `--help` : Affiche l'aide sur la commande `stat`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `stat` :

1. Afficher les informations par défaut d'un fichier :
   ```csh
   stat mon_fichier.txt
   ```

2. Afficher les informations d'un répertoire :
   ```csh
   stat mon_repertoire/
   ```

3. Utiliser l'option `-f` pour afficher les informations dans un format spécifique :
   ```csh
   stat -f "%N : %z octets" mon_fichier.txt
   ```

4. Utiliser l'option `-c` pour un format de sortie personnalisé :
   ```csh
   stat -c "Taille: %s, Modifié: %y" mon_fichier.txt
   ```

## Tips
- Utilisez l'option `--help` pour obtenir des informations supplémentaires sur les options disponibles.
- Pour des scripts, envisagez d'utiliser l'option `-c` pour formater la sortie de manière à faciliter l'analyse.
- Vérifiez régulièrement les permissions et les dates de modification des fichiers importants pour éviter toute perte de données.