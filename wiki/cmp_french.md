# [Linux] C Shell (csh) cmp : Comparer des fichiers binaires

## Overview
La commande `cmp` est utilisée pour comparer deux fichiers binaires ou texte, en affichant les différences entre eux. Elle est particulièrement utile pour détecter les variations dans des fichiers de données ou des programmes.

## Usage
La syntaxe de base de la commande `cmp` est la suivante :

```
cmp [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `cmp` :

- `-l` : Affiche les octets différents en format octal.
- `-s` : Ne produit aucune sortie, mais retourne un code de sortie indiquant si les fichiers sont identiques ou non.
- `-i` : Ignore les premiers N octets de chaque fichier.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cmp` :

1. Comparer deux fichiers et afficher les différences :
   ```csh
   cmp fichier1.txt fichier2.txt
   ```

2. Comparer deux fichiers sans afficher de sortie, juste le code de retour :
   ```csh
   cmp -s fichier1.bin fichier2.bin
   ```

3. Comparer deux fichiers en affichant les octets différents :
   ```csh
   cmp -l fichier1.txt fichier2.txt
   ```

4. Ignorer les premiers 10 octets lors de la comparaison :
   ```csh
   cmp -i 10 fichier1.txt fichier2.txt
   ```

## Tips
- Utilisez l'option `-s` si vous souhaitez simplement vérifier l'égalité des fichiers sans afficher les différences.
- Lorsque vous comparez des fichiers binaires, il est souvent utile d'utiliser l'option `-l` pour obtenir une vue détaillée des différences.
- Pensez à rediriger la sortie vers un fichier si vous comparez de grands fichiers et que vous souhaitez conserver un enregistrement des différences.