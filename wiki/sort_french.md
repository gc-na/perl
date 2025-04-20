# [Linux] C Shell (csh) sort Utilisation : Trier des lignes de texte

## Overview
La commande `sort` dans C Shell (csh) est utilisée pour trier les lignes d'un fichier ou d'une entrée standard. Elle organise les lignes dans un ordre spécifique, généralement alphabétique ou numérique, facilitant ainsi la recherche et l'analyse des données.

## Usage
La syntaxe de base de la commande `sort` est la suivante :

```csh
sort [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `sort` :

- `-r` : Trie les lignes dans l'ordre inverse.
- `-n` : Trie les lignes numériquement.
- `-k` : Spécifie une clé de tri, permettant de trier selon une colonne spécifique.
- `-u` : Supprime les doublons après le tri.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `sort` :

1. Trier un fichier texte par ordre alphabétique :
   ```csh
   sort fichier.txt
   ```

2. Trier un fichier texte en ordre inverse :
   ```csh
   sort -r fichier.txt
   ```

3. Trier numériquement un fichier contenant des nombres :
   ```csh
   sort -n nombres.txt
   ```

4. Trier un fichier selon la deuxième colonne :
   ```csh
   sort -k 2 fichier.txt
   ```

5. Trier un fichier et supprimer les doublons :
   ```csh
   sort -u fichier.txt
   ```

## Tips
- Utilisez `-o` pour rediriger la sortie triée vers un fichier, par exemple :
  ```csh
  sort fichier.txt -o fichier_trie.txt
  ```
- Pour trier des données en temps réel, vous pouvez combiner `sort` avec d'autres commandes via un pipe :
  ```csh
  cat fichier.txt | sort
  ```
- Pensez à utiliser `man sort` pour consulter la page de manuel et découvrir d'autres options et fonctionnalités.