# [Linux] C Shell (csh) grep Utilisation : Recherche de texte dans des fichiers

## Overview
La commande `grep` est utilisée pour rechercher des motifs spécifiques dans des fichiers ou des flux de texte. Elle permet d'extraire des lignes qui correspondent à un motif donné, facilitant ainsi l'analyse et le filtrage de données.

## Usage
La syntaxe de base de la commande `grep` est la suivante :

```csh
grep [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `grep` :

- `-i` : Ignore la casse lors de la recherche.
- `-v` : Inverse la recherche, affichant les lignes qui ne correspondent pas au motif.
- `-r` : Recherche récursive dans les sous-répertoires.
- `-n` : Affiche les numéros de ligne des correspondances trouvées.
- `-l` : Affiche uniquement les noms de fichiers contenant des correspondances.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `grep` :

1. **Recherche d'un mot dans un fichier :**
   ```csh
   grep "mot" fichier.txt
   ```

2. **Recherche insensible à la casse :**
   ```csh
   grep -i "mot" fichier.txt
   ```

3. **Recherche dans plusieurs fichiers :**
   ```csh
   grep "mot" *.txt
   ```

4. **Recherche récursive dans un répertoire :**
   ```csh
   grep -r "mot" /chemin/vers/répertoire
   ```

5. **Afficher les numéros de ligne :**
   ```csh
   grep -n "mot" fichier.txt
   ```

## Tips
- Utilisez `grep -v` pour filtrer les résultats et ne montrer que les lignes qui ne contiennent pas le motif recherché.
- Combinez `grep` avec d'autres commandes en utilisant des pipes pour des analyses plus complexes, par exemple : `cat fichier.txt | grep "mot"`.
- Pour des motifs plus complexes, envisagez d'utiliser des expressions régulières avec `grep`, ce qui vous permettra de rechercher des motifs plus variés.