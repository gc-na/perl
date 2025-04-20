# [Linux] C Shell (csh) wget Utilisation : Téléchargement de fichiers à partir du web

## Overview
La commande `wget` est un outil puissant utilisé pour télécharger des fichiers à partir du web. Elle prend en charge les protocoles HTTP, HTTPS et FTP, ce qui en fait un choix populaire pour récupérer des fichiers de manière non interactive.

## Usage
La syntaxe de base de la commande `wget` est la suivante :

```bash
wget [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `wget` :

- `-O [nom_fichier]` : Spécifie le nom du fichier de sortie.
- `-c` : Reprend un téléchargement interrompu.
- `-q` : Exécute `wget` en mode silencieux, sans afficher de messages.
- `--limit-rate=[vitesse]` : Limite la vitesse de téléchargement à la valeur spécifiée.
- `-r` : Active le téléchargement récursif pour récupérer des fichiers liés.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `wget` :

1. Télécharger un fichier à partir d'une URL :
   ```bash
   wget http://example.com/fichier.zip
   ```

2. Télécharger un fichier et le renommer :
   ```bash
   wget -O nouveau_nom.zip http://example.com/fichier.zip
   ```

3. Reprendre un téléchargement interrompu :
   ```bash
   wget -c http://example.com/fichier.zip
   ```

4. Télécharger un site web de manière récursive :
   ```bash
   wget -r http://example.com
   ```

5. Limiter la vitesse de téléchargement :
   ```bash
   wget --limit-rate=100k http://example.com/fichier.zip
   ```

## Tips
- Utilisez l'option `-q` pour éviter d'encombrer votre terminal avec des messages, surtout lors de téléchargements en arrière-plan.
- Pensez à utiliser `-c` si vous téléchargez de gros fichiers pour éviter de recommencer depuis le début en cas d'interruption.
- Pour les téléchargements récursifs, assurez-vous de respecter les règles du site web pour éviter d'être bloqué pour un comportement abusif.