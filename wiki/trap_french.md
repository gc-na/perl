# [Linux] C Shell (csh) trap : Gérer les signaux et les événements

## Overview
La commande `trap` dans C Shell (csh) est utilisée pour intercepter et gérer les signaux et les événements dans un script. Elle permet d'exécuter des commandes spécifiques lorsqu'un signal particulier est reçu, ce qui est utile pour le nettoyage ou la gestion des erreurs.

## Usage
La syntaxe de base de la commande `trap` est la suivante :

```csh
trap [options] [arguments]
```

## Common Options
- `signal`: Le signal à intercepter (par exemple, `INT` pour une interruption).
- `command`: La commande à exécuter lorsque le signal est reçu.
- `-l`: Liste tous les signaux disponibles.

## Common Examples

### Exemple 1 : Intercepter un signal d'interruption
Ce script intercepte le signal d'interruption (CTRL+C) et affiche un message avant de quitter.

```csh
#!/bin/csh
trap 'echo "Interruption reçue, sortie du script."' INT
while (1)
    echo "Exécution en cours..."
    sleep 1
end
```

### Exemple 2 : Nettoyage avant la sortie
Ce script utilise `trap` pour supprimer un fichier temporaire avant de quitter.

```csh
#!/bin/csh
trap 'rm -f /tmp/tempfile' EXIT
echo "Création d'un fichier temporaire..."
touch /tmp/tempfile
# Autres opérations
```

### Exemple 3 : Gérer plusieurs signaux
Ce script gère à la fois les signaux d'interruption et de terminaison.

```csh
#!/bin/csh
trap 'echo "Signal d'interruption reçu."' INT
trap 'echo "Signal de terminaison reçu."' TERM
while (1)
    echo "Exécution en cours..."
    sleep 1
end
```

## Tips
- Utilisez `trap` pour garantir que les ressources sont libérées correctement, même en cas d'erreur.
- Testez toujours vos scripts avec des signaux pour vous assurer que le comportement est celui attendu.
- Pensez à documenter les signaux que vous interceptez pour faciliter la maintenance de vos scripts.