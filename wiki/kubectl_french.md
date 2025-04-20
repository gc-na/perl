# [Linux] C Shell (csh) kubectl : Commande pour interagir avec Kubernetes

## Overview
La commande `kubectl` est un outil en ligne de commande qui permet d'interagir avec les clusters Kubernetes. Elle vous permet de déployer des applications, de gérer les ressources et d'obtenir des informations sur l'état de votre cluster.

## Usage
La syntaxe de base de la commande `kubectl` est la suivante :

```bash
kubectl [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `kubectl` :

- `get` : Récupère des informations sur les ressources.
- `apply` : Applique des modifications à des ressources à partir d'un fichier de configuration.
- `delete` : Supprime des ressources spécifiées.
- `describe` : Affiche des détails sur une ressource spécifique.
- `logs` : Affiche les logs d'un pod.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `kubectl` :

- Pour obtenir la liste des pods dans le namespace par défaut :

```bash
kubectl get pods
```

- Pour appliquer un fichier de configuration YAML :

```bash
kubectl apply -f mon-fichier.yaml
```

- Pour supprimer un pod spécifique :

```bash
kubectl delete pod mon-pod
```

- Pour afficher les détails d'un déploiement :

```bash
kubectl describe deployment mon-deploiement
```

- Pour voir les logs d'un pod :

```bash
kubectl logs mon-pod
```

## Tips
- Utilisez `kubectl get all` pour obtenir un aperçu rapide de toutes les ressources dans le namespace actuel.
- Ajoutez l'option `-n` pour spécifier un namespace si vous travaillez avec plusieurs namespaces.
- Utilisez `kubectl --help` pour obtenir de l'aide sur les commandes et options disponibles.