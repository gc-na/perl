# [Linux] C Shell (csh) hexdump : Afficher les données en hexadécimal

## Overview
La commande `hexdump` permet de visualiser le contenu binaire d'un fichier sous forme hexadécimale. Elle est particulièrement utile pour l'analyse de fichiers non textuels, permettant aux utilisateurs de voir les données brutes.

## Usage
La syntaxe de base de la commande `hexdump` est la suivante :

```csh
hexdump [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `hexdump` :

- `-C` : Affiche le contenu en hexadécimal et en ASCII.
- `-n N` : Limite la sortie aux premiers N octets.
- `-v` : Affiche tous les octets, y compris les répétitions.
- `-e FORMAT` : Définit un format de sortie personnalisé.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `hexdump` :

1. Afficher le contenu hexadécimal d'un fichier :
   ```csh
   hexdump fichier.bin
   ```

2. Afficher les 16 premiers octets d'un fichier :
   ```csh
   hexdump -n 16 fichier.bin
   ```

3. Afficher le contenu en hexadécimal et en ASCII :
   ```csh
   hexdump -C fichier.bin
   ```

4. Utiliser un format de sortie personnalisé :
   ```csh
   hexdump -e '16/1 "%02x " "\n"' fichier.bin
   ```

## Tips
- Utilisez l'option `-C` pour une vue plus lisible qui combine l'hexadécimal et l'ASCII.
- Limitez la sortie avec `-n` pour éviter d'être submergé par trop d'informations.
- Pensez à rediriger la sortie vers un fichier si vous analysez de gros fichiers :
  ```csh
  hexdump fichier.bin > sortie.txt
  ```