# [Système d'exploitation] C Shell (csh) ftp : Transférer des fichiers sur un réseau

## Overview
La commande `ftp` (File Transfer Protocol) permet de transférer des fichiers entre un ordinateur local et un serveur distant via le protocole FTP. Elle est largement utilisée pour télécharger ou téléverser des fichiers sur Internet.

## Usage
La syntaxe de base de la commande `ftp` est la suivante :

```csh
ftp [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `ftp` :

- `-v` : Mode verbeux, affiche des informations détaillées sur le transfert.
- `-n` : Ne pas tenter de se connecter automatiquement à un hôte par défaut.
- `-i` : Désactive le mode interactif, ce qui permet de transférer des fichiers sans confirmation.
- `-g` : Permet d'utiliser des caractères génériques pour les fichiers.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `ftp` :

1. **Se connecter à un serveur FTP :**
   ```csh
   ftp ftp.example.com
   ```

2. **Télécharger un fichier depuis le serveur :**
   ```csh
   ftp> get fichier.txt
   ```

3. **Téléverser un fichier vers le serveur :**
   ```csh
   ftp> put fichier.txt
   ```

4. **Lister les fichiers sur le serveur :**
   ```csh
   ftp> ls
   ```

5. **Quitter la session FTP :**
   ```csh
   ftp> bye
   ```

## Tips
- Assurez-vous d'utiliser un mot de passe fort lors de la connexion à un serveur FTP pour protéger vos données.
- Utilisez l'option `-v` pour obtenir des informations détaillées sur le transfert, ce qui peut aider à diagnostiquer des problèmes.
- Pensez à passer en mode binaire (`binary`) lors du transfert de fichiers non texte pour éviter la corruption des données.