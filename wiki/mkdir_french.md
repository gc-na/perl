# [Linux] C Shell (csh) mkdir Utilisation : Créer des répertoires

## Overview
La commande `mkdir` est utilisée pour créer de nouveaux répertoires dans le système de fichiers. C'est un outil essentiel pour organiser vos fichiers et dossiers.

## Usage
La syntaxe de base de la commande `mkdir` est la suivante :

```csh
mkdir [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `mkdir` :

- `-p` : Crée des répertoires parents si nécessaire. Si le répertoire parent n'existe pas, il sera créé.
- `-m` : Définit les permissions du répertoire créé. Vous pouvez spécifier les permissions en utilisant le format octal.
- `-v` : Affiche un message pour chaque répertoire créé, ce qui peut être utile pour le débogage.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mkdir` :

1. Créer un répertoire simple :
   ```csh
   mkdir mon_dossier
   ```

2. Créer plusieurs répertoires à la fois :
   ```csh
   mkdir dossier1 dossier2 dossier3
   ```

3. Créer un répertoire avec des répertoires parents :
   ```csh
   mkdir -p parent/enfant
   ```

4. Créer un répertoire avec des permissions spécifiques :
   ```csh
   mkdir -m 755 mon_dossier
   ```

5. Créer un répertoire et afficher un message :
   ```csh
   mkdir -v mon_dossier
   ```

## Tips
- Utilisez l'option `-p` lorsque vous n'êtes pas sûr que le répertoire parent existe déjà, cela évite les erreurs.
- Pensez à définir les permissions appropriées lors de la création de répertoires sensibles pour garantir la sécurité de vos fichiers.
- Utilisez l'option `-v` pour vérifier que vos répertoires sont créés correctement, surtout lors de la création de plusieurs répertoires.