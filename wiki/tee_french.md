# [Linux] C Shell (csh) tee : [rediriger et afficher la sortie]

## Overview
La commande `tee` dans C Shell (csh) permet de lire l'entrée standard et de la rediriger à la fois vers la sortie standard et vers un ou plusieurs fichiers. Cela est particulièrement utile pour enregistrer des données tout en les affichant à l'écran.

## Usage
La syntaxe de base de la commande `tee` est la suivante :

```csh
tee [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `tee` :

- `-a` : Ajoute la sortie à la fin du fichier au lieu de l'écraser.
- `-i` : Ignore les signaux d'interruption.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `tee` :

1. **Rediriger la sortie d'une commande vers un fichier :**

   ```csh
   ls -l | tee fichier.txt
   ```

   Cela affichera la liste des fichiers dans le répertoire courant et l'enregistrera dans `fichier.txt`.

2. **Ajouter la sortie à un fichier existant :**

   ```csh
   echo "Nouvelle ligne" | tee -a fichier.txt
   ```

   Cela ajoutera "Nouvelle ligne" à la fin de `fichier.txt` tout en l'affichant à l'écran.

3. **Utiliser tee avec plusieurs fichiers :**

   ```csh
   echo "Données importantes" | tee fichier1.txt fichier2.txt
   ```

   Cela enverra "Données importantes" à la fois à `fichier1.txt` et `fichier2.txt`, tout en l'affichant à l'écran.

## Tips
- Utilisez l'option `-a` lorsque vous souhaitez conserver le contenu existant d'un fichier et ajouter de nouvelles données.
- Combinez `tee` avec d'autres commandes pour créer des pipelines efficaces, par exemple, pour surveiller les logs tout en les sauvegardant.
- Soyez conscient des permissions des fichiers lorsque vous utilisez `tee`, car vous pourriez ne pas avoir les droits nécessaires pour écrire dans certains fichiers.