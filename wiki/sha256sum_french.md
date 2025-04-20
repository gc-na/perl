# [Linux] C Shell (csh) sha256sum : Calculer des sommes de contrôle SHA-256

## Overview
La commande `sha256sum` est utilisée pour calculer et vérifier les sommes de contrôle SHA-256 d'un fichier. Cela permet de garantir l'intégrité des données en s'assurant qu'un fichier n'a pas été altéré.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
sha256sum [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `sha256sum` :

- `-b` : Traite le fichier en mode binaire.
- `-c` : Vérifie les sommes de contrôle à partir d'un fichier.
- `-h` : Affiche l'aide et les options disponibles.
- `-o` : Écrit la sortie dans un fichier spécifié.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `sha256sum` :

1. Calculer la somme de contrôle d'un fichier :
   ```csh
   sha256sum monfichier.txt
   ```

2. Vérifier les sommes de contrôle à partir d'un fichier :
   ```csh
   sha256sum -c checksums.txt
   ```

3. Calculer la somme de contrôle d'un fichier en mode binaire :
   ```csh
   sha256sum -b monfichier.bin
   ```

4. Écrire la sortie dans un fichier :
   ```csh
   sha256sum monfichier.txt -o somme.txt
   ```

## Tips
- Utilisez `sha256sum` avec des fichiers de vérification pour assurer l'intégrité des téléchargements.
- Combinez `sha256sum` avec d'autres commandes, comme `find`, pour vérifier plusieurs fichiers à la fois.
- Gardez un fichier de sommes de contrôle à jour pour vos fichiers importants afin de faciliter les vérifications futures.