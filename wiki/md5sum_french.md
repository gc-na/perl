# [Linux] C Shell (csh) md5sum : Calculer des sommes de contrôle MD5

## Overview
La commande `md5sum` est utilisée pour calculer et vérifier les sommes de contrôle MD5 d'un fichier. Cela permet de s'assurer que le contenu d'un fichier n'a pas été altéré.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
md5sum [options] [arguments]
```

## Common Options
- `-b` : Traite les fichiers en mode binaire.
- `-c` : Vérifie les sommes de contrôle à partir d'un fichier.
- `-t` : Traite les fichiers en mode texte.
- `--help` : Affiche l'aide sur l'utilisation de la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `md5sum` :

1. Calculer la somme de contrôle MD5 d'un fichier :
   ```csh
   md5sum fichier.txt
   ```

2. Vérifier les sommes de contrôle à partir d'un fichier :
   ```csh
   md5sum -c checksums.md5
   ```

3. Calculer la somme de contrôle MD5 d'un fichier en mode binaire :
   ```csh
   md5sum -b fichier.bin
   ```

4. Afficher l'aide sur la commande :
   ```csh
   md5sum --help
   ```

## Tips
- Utilisez `md5sum` pour vérifier l'intégrité des fichiers téléchargés.
- Conservez un fichier de sommes de contrôle pour les fichiers importants afin de pouvoir vérifier leur intégrité ultérieurement.
- Évitez d'utiliser MD5 pour des applications de sécurité critiques, car il est considéré comme vulnérable à certaines attaques.