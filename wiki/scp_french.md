# [Linux] C Shell (csh) scp : [transférer des fichiers sécurisés]

## Overview
La commande `scp` (Secure Copy Protocol) permet de transférer des fichiers de manière sécurisée entre un ordinateur local et un ordinateur distant, ou entre deux ordinateurs distants. Elle utilise le protocole SSH pour garantir la sécurité des données pendant le transfert.

## Usage
La syntaxe de base de la commande `scp` est la suivante :

```csh
scp [options] [source] [destination]
```

## Common Options
Voici quelques options courantes pour la commande `scp` :

- `-r` : Copie récursivement des répertoires.
- `-P` : Spécifie le port à utiliser pour la connexion SSH.
- `-i` : Indique un fichier de clé d'identification à utiliser pour l'authentification.
- `-v` : Active le mode verbeux pour afficher des informations détaillées sur le transfert.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `scp` :

1. **Transférer un fichier local vers un serveur distant :**
   ```csh
   scp fichier.txt utilisateur@serveur:/chemin/destination/
   ```

2. **Transférer un fichier d'un serveur distant vers l'ordinateur local :**
   ```csh
   scp utilisateur@serveur:/chemin/source/fichier.txt /chemin/local/
   ```

3. **Copier un répertoire entier vers un serveur distant :**
   ```csh
   scp -r mon_repertoire utilisateur@serveur:/chemin/destination/
   ```

4. **Utiliser un port spécifique pour la connexion :**
   ```csh
   scp -P 2222 fichier.txt utilisateur@serveur:/chemin/destination/
   ```

## Tips
- Assurez-vous que le service SSH est en cours d'exécution sur le serveur distant avant d'utiliser `scp`.
- Utilisez l'option `-v` pour le débogage si vous rencontrez des problèmes de connexion.
- Pour des transferts fréquents, envisagez d'utiliser des clés SSH pour éviter de saisir votre mot de passe à chaque fois.