# [Linux] C Shell (csh) cksum : Calculer les sommes de contrôle des fichiers

## Overview
La commande `cksum` dans le C Shell (csh) est utilisée pour calculer et afficher la somme de contrôle d'un fichier ainsi que sa taille en octets. Cela peut être utile pour vérifier l'intégrité des fichiers.

## Usage
La syntaxe de base de la commande `cksum` est la suivante :

```csh
cksum [options] [arguments]
```

## Common Options
- `-a, --algorithm=ALGO` : Spécifie l'algorithme de somme de contrôle à utiliser.
- `--help` : Affiche l'aide et les options disponibles pour la commande.
- `--version` : Affiche la version de la commande `cksum`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cksum` :

1. Calculer la somme de contrôle d'un fichier :
   ```csh
   cksum fichier.txt
   ```

2. Calculer la somme de contrôle de plusieurs fichiers :
   ```csh
   cksum fichier1.txt fichier2.txt
   ```

3. Afficher l'aide de la commande :
   ```csh
   cksum --help
   ```

4. Vérifier la somme de contrôle d'un fichier avec un algorithme spécifique :
   ```csh
   cksum -a md5 fichier.txt
   ```

## Tips
- Utilisez `cksum` pour vérifier l'intégrité des fichiers après un transfert ou une sauvegarde.
- Combinez `cksum` avec d'autres commandes comme `find` pour traiter plusieurs fichiers à la fois.
- Gardez à l'esprit que la somme de contrôle peut varier selon les algorithmes utilisés, alors choisissez celui qui convient le mieux à vos besoins.