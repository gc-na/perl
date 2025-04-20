# [Système d'exploitation] C Shell (csh) sftp : Transférer des fichiers en toute sécurité

## Overview
La commande `sftp` (SSH File Transfer Protocol) permet de transférer des fichiers de manière sécurisée entre un client et un serveur. Elle utilise le protocole SSH pour garantir la sécurité des données pendant le transfert.

## Usage
La syntaxe de base de la commande `sftp` est la suivante :

```csh
sftp [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `sftp` :

- `-o` : Permet de spécifier des options de configuration supplémentaires.
- `-b` : Utilise un fichier de commandes batch pour exécuter plusieurs commandes `sftp`.
- `-P` : Spécifie le port à utiliser pour la connexion au serveur.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `sftp` :

1. **Se connecter à un serveur SFTP :**
   ```csh
   sftp user@hostname
   ```

2. **Transférer un fichier vers le serveur :**
   ```csh
   put localfile.txt
   ```

3. **Télécharger un fichier depuis le serveur :**
   ```csh
   get remotefile.txt
   ```

4. **Transférer un répertoire entier :**
   ```csh
   put -r localdirectory
   ```

5. **Exécuter des commandes à partir d'un fichier batch :**
   ```csh
   sftp -b batchfile.txt user@hostname
   ```

## Tips
- Assurez-vous que le serveur SFTP est configuré pour accepter les connexions SSH.
- Utilisez des clés SSH pour une connexion plus sécurisée et sans mot de passe.
- Vérifiez toujours les permissions des fichiers après le transfert pour garantir leur sécurité.