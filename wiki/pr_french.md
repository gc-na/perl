# [Linux] C Shell (csh) pr : formater des fichiers texte

## Overview
La commande `pr` est utilisée pour formater des fichiers texte afin de les rendre plus lisibles. Elle permet de paginer le contenu d'un fichier, d'ajouter des en-têtes et de gérer la mise en forme pour l'impression.

## Usage
La syntaxe de base de la commande `pr` est la suivante :

```csh
pr [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `pr` :

- `-h` : Spécifie un en-tête personnalisé pour la sortie.
- `-l` : Définit le nombre de lignes par page.
- `-n` : Numérote les pages.
- `-s` : Définit le caractère de séparation entre les colonnes.
- `-t` : Supprime les en-têtes et les pieds de page.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `pr` :

1. **Formater un fichier texte avec des en-têtes :**
   ```csh
   pr -h "Mon Document" mon_fichier.txt
   ```

2. **Afficher le contenu d'un fichier avec une pagination de 50 lignes par page :**
   ```csh
   pr -l 50 mon_fichier.txt
   ```

3. **Numéroter les pages d'un fichier texte :**
   ```csh
   pr -n mon_fichier.txt
   ```

4. **Utiliser un caractère de séparation personnalisé :**
   ```csh
   pr -s " | " mon_fichier.txt
   ```

5. **Supprimer les en-têtes et les pieds de page :**
   ```csh
   pr -t mon_fichier.txt
   ```

## Tips
- Utilisez l'option `-h` pour ajouter des titres significatifs qui aident à identifier le contenu lors de l'impression.
- Ajustez le nombre de lignes par page avec l'option `-l` pour mieux s'adapter à votre format d'impression.
- Pensez à rediriger la sortie vers un fichier si vous souhaitez conserver le formatage pour une utilisation ultérieure :
  ```csh
  pr mon_fichier.txt > fichier_formate.txt
  ```