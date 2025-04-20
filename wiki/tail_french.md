# [Linux] C Shell (csh) tail Utilisation : Afficher les dernières lignes d'un fichier

## Overview
La commande `tail` est utilisée pour afficher les dernières lignes d'un fichier. Elle est particulièrement utile pour surveiller les fichiers journaux ou pour voir les dernières entrées d'un fichier texte.

## Usage
La syntaxe de base de la commande `tail` est la suivante :

```csh
tail [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `tail` :

- `-n [nombre]` : Affiche les dernières [nombre] lignes du fichier spécifié.
- `-f` : Suivre le fichier en temps réel, affichant les nouvelles lignes au fur et à mesure qu'elles sont ajoutées.
- `-q` : Ne pas afficher le nom des fichiers lors de l'affichage de plusieurs fichiers.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `tail` :

1. Afficher les 10 dernières lignes d'un fichier :
   ```csh
   tail mon_fichier.txt
   ```

2. Afficher les 20 dernières lignes d'un fichier :
   ```csh
   tail -n 20 mon_fichier.txt
   ```

3. Suivre un fichier en temps réel (par exemple, un fichier journal) :
   ```csh
   tail -f mon_fichier.log
   ```

4. Afficher les dernières lignes de plusieurs fichiers :
   ```csh
   tail -q mon_fichier1.txt mon_fichier2.txt
   ```

## Tips
- Utilisez l'option `-f` pour surveiller les fichiers journaux en temps réel, ce qui est très utile pour le débogage.
- Combinez `tail` avec d'autres commandes comme `grep` pour filtrer les résultats. Par exemple :
  ```csh
  tail -f mon_fichier.log | grep "Erreur"
  ```
- Pensez à rediriger la sortie de `tail` vers un fichier si vous souhaitez conserver les résultats pour une consultation ultérieure :
  ```csh
  tail mon_fichier.txt > dernieres_lignes.txt
  ```