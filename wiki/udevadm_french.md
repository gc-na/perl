# [Linux] C Shell (csh) udevadm : Gestion des périphériques

## Overview
La commande `udevadm` est utilisée pour interagir avec le gestionnaire de périphériques `udev` sous Linux. Elle permet de gérer les événements liés aux périphériques, d'interroger des informations sur les périphériques et de contrôler le comportement de `udev`.

## Usage
La syntaxe de base de la commande `udevadm` est la suivante :

```csh
udevadm [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `udevadm` :

- `info` : Affiche des informations sur un périphérique spécifique.
- `trigger` : Déclenche des événements pour les périphériques.
- `settle` : Attend que tous les événements de périphériques soient traités.
- `control` : Contrôle le fonctionnement du démon `udevd`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `udevadm` :

1. **Afficher des informations sur un périphérique spécifique :**
   ```csh
   udevadm info --query=all --name=/dev/sda
   ```

2. **Déclencher des événements pour les périphériques :**
   ```csh
   udevadm trigger
   ```

3. **Attendre que tous les événements soient traités :**
   ```csh
   udevadm settle
   ```

4. **Contrôler le démon `udevd` :**
   ```csh
   udevadm control --reload-rules
   ```

## Tips
- Utilisez `udevadm info` pour obtenir des détails sur un périphérique avant de modifier ses règles.
- Soyez prudent lors de l'utilisation de `udevadm trigger`, car cela peut affecter tous les périphériques connectés.
- Vérifiez toujours les règles `udev` après avoir utilisé `udevadm control --reload-rules` pour vous assurer qu'elles sont appliquées correctement.