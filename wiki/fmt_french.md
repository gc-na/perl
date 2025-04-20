# [Linux] C Shell (csh) fmt : [formater le texte]

## Overview
La commande `fmt` est utilisée pour formater le texte en ajustant la largeur des lignes. Elle est particulièrement utile pour rendre le texte plus lisible en réorganisant les lignes pour qu'elles aient une longueur uniforme.

## Usage
La syntaxe de base de la commande `fmt` est la suivante :

```
fmt [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `fmt` :

- `-w <largeur>` : Définit la largeur maximale des lignes formatées. Par défaut, cette largeur est de 75 caractères.
- `-s` : Supprime les lignes vides consécutives pour éviter les espaces inutiles.
- `-u` : Formate le texte en justifiant les lignes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `fmt` :

1. **Formater un fichier texte avec la largeur par défaut :**
   ```csh
   fmt mon_fichier.txt
   ```

2. **Formater un fichier texte avec une largeur de 50 caractères :**
   ```csh
   fmt -w 50 mon_fichier.txt
   ```

3. **Supprimer les lignes vides consécutives lors du formatage :**
   ```csh
   fmt -s mon_fichier.txt
   ```

4. **Justifier le texte d'un fichier :**
   ```csh
   fmt -u mon_fichier.txt
   ```

## Tips
- Utilisez l'option `-w` pour adapter la largeur des lignes à vos besoins spécifiques, surtout si vous préparez du texte pour des affichages limités.
- Pensez à combiner l'option `-s` avec d'autres options pour obtenir un texte plus propre et mieux organisé.
- Testez toujours la commande sur un fichier de sauvegarde pour éviter de perdre des informations importantes lors du formatage.