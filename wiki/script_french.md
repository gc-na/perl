# [Linux] C Shell (csh) script : Enregistrer une session de terminal

## Overview
La commande `script` permet d'enregistrer une session de terminal dans un fichier. Cela est utile pour capturer les entrées et sorties d'une session, ce qui peut être précieux pour la documentation ou le partage d'informations.

## Usage
La syntaxe de base de la commande `script` est la suivante :

```csh
script [options] [arguments]
```

## Common Options
- `-a` : Ajoute la sortie à un fichier existant au lieu de le remplacer.
- `-f` : Écrit la sortie immédiatement dans le fichier, plutôt que de la mettre en mémoire tampon.
- `-q` : Exécute la commande en mode silencieux, sans afficher le message de démarrage.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `script` :

1. **Enregistrer une session dans un fichier :**
   ```csh
   script session.txt
   ```
   Cela démarre l'enregistrement de la session dans le fichier `session.txt`.

2. **Ajouter à un fichier existant :**
   ```csh
   script -a session.txt
   ```
   Cela ajoute la sortie de la session actuelle à `session.txt` sans effacer le contenu précédent.

3. **Écrire la sortie immédiatement :**
   ```csh
   script -f session.txt
   ```
   Cela enregistre la session dans `session.txt` en écrivant immédiatement chaque ligne.

4. **Exécuter en mode silencieux :**
   ```csh
   script -q session.txt
   ```
   Cela enregistre la session sans afficher le message de démarrage.

## Tips
- Pensez à utiliser `exit` pour terminer l'enregistrement de la session proprement.
- Vérifiez régulièrement le fichier de sortie pour vous assurer que l'enregistrement fonctionne comme prévu.
- Utilisez des noms de fichiers descriptifs pour faciliter la recherche de sessions enregistrées plus tard.