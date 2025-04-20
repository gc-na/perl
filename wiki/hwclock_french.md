# [Linux] C Shell (csh) hwclock : [afficher l'heure matérielle]

## Overview
La commande `hwclock` est utilisée pour afficher ou modifier l'heure matérielle du système. Cette heure est stockée dans le matériel de l'ordinateur, généralement dans une horloge en temps réel (RTC), et peut être utilisée pour synchroniser l'heure du système d'exploitation.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
hwclock [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `hwclock` :

- `--show` : Affiche l'heure matérielle actuelle.
- `--set` : Définit l'heure matérielle à une heure spécifiée.
- `--hctosys` : Synchronise l'heure du système avec l'heure matérielle.
- `--systohc` : Synchronise l'heure matérielle avec l'heure du système.
- `--utc` : Indique que l'heure matérielle est en temps universel coordonné (UTC).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `hwclock` :

1. **Afficher l'heure matérielle actuelle :**
   ```csh
   hwclock --show
   ```

2. **Synchroniser l'heure du système avec l'heure matérielle :**
   ```csh
   hwclock --hctosys
   ```

3. **Synchroniser l'heure matérielle avec l'heure du système :**
   ```csh
   hwclock --systohc
   ```

4. **Définir l'heure matérielle à une heure spécifique :**
   ```csh
   hwclock --set --date="2023-10-01 12:00:00"
   ```

5. **Afficher l'heure matérielle en UTC :**
   ```csh
   hwclock --show --utc
   ```

## Tips
- Assurez-vous d'avoir les privilèges nécessaires pour modifier l'heure matérielle, car cela peut nécessiter des droits d'administrateur.
- Utilisez l'option `--utc` si vous travaillez sur un système qui utilise UTC pour éviter toute confusion avec les fuseaux horaires.
- Vérifiez régulièrement l'heure matérielle pour vous assurer qu'elle est correcte, surtout après un redémarrage ou une mise à jour du système.