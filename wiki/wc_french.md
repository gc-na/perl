# [Linux] C Shell (csh) wc : Compter les lignes, mots et caractères

## Overview
La commande `wc` (word count) est utilisée pour compter le nombre de lignes, de mots et de caractères dans un fichier ou dans l'entrée standard. C'est un outil pratique pour obtenir des statistiques simples sur le contenu textuel.

## Usage
La syntaxe de base de la commande `wc` est la suivante :

```bash
wc [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `wc` :

- `-l` : Compte uniquement le nombre de lignes.
- `-w` : Compte uniquement le nombre de mots.
- `-c` : Compte uniquement le nombre de caractères.
- `-m` : Compte le nombre de caractères (en tenant compte des caractères multibyte).
- `-L` : Affiche la longueur de la ligne la plus longue.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `wc` :

1. Compter le nombre de lignes dans un fichier :
   ```bash
   wc -l mon_fichier.txt
   ```

2. Compter le nombre de mots dans un fichier :
   ```bash
   wc -w mon_fichier.txt
   ```

3. Compter le nombre de caractères dans un fichier :
   ```bash
   wc -c mon_fichier.txt
   ```

4. Compter les lignes, mots et caractères en une seule commande :
   ```bash
   wc mon_fichier.txt
   ```

5. Compter les lignes dans l'entrée standard (par exemple, en utilisant un pipe) :
   ```bash
   cat mon_fichier.txt | wc -l
   ```

## Tips
- Utilisez `wc` avec d'autres commandes en utilisant des pipes pour analyser rapidement le contenu généré.
- Combinez plusieurs options pour obtenir des statistiques complètes en une seule commande.
- Pour des fichiers très volumineux, utilisez `wc` sur des segments de fichiers pour éviter des temps de traitement trop longs.