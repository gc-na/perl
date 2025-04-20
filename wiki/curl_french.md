# [Linux] C Shell (csh) curl Utilisation : Récupérer des données à partir d'URL

## Overview
La commande `curl` est un outil en ligne de commande utilisé pour transférer des données vers ou depuis un serveur. Elle prend en charge divers protocoles, notamment HTTP, HTTPS, FTP et bien d'autres. `curl` est particulièrement utile pour tester des API ou télécharger des fichiers.

## Usage
La syntaxe de base de la commande `curl` est la suivante :

```csh
curl [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `curl` :

- `-O` : Télécharge un fichier et le sauvegarde avec le même nom que celui du serveur.
- `-L` : Suit les redirections.
- `-I` : Récupère uniquement les en-têtes de la réponse.
- `-d` : Envoie des données dans une requête POST.
- `-H` : Ajoute un en-tête HTTP personnalisé.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `curl` :

1. **Télécharger un fichier :**
   ```csh
   curl -O http://example.com/fichier.txt
   ```

2. **Faire une requête GET :**
   ```csh
   curl http://example.com/api/v1/ressource
   ```

3. **Faire une requête POST avec des données :**
   ```csh
   curl -d "nom=John&age=30" http://example.com/api/v1/ajouter
   ```

4. **Récupérer uniquement les en-têtes d'une réponse :**
   ```csh
   curl -I http://example.com
   ```

5. **Suivre les redirections :**
   ```csh
   curl -L http://example.com/ancienne-url
   ```

## Tips
- Utilisez l'option `-v` pour activer le mode verbeux, ce qui vous permet de voir les détails de la requête et de la réponse.
- Pour tester des API, envisagez d'utiliser des outils comme Postman, mais `curl` est idéal pour des tests rapides en ligne de commande.
- Pensez à consulter la documentation de `curl` en utilisant `man curl` pour explorer toutes les options disponibles.