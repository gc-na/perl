# [Linux] C Shell (csh) hostname Utilisation : Afficher ou définir le nom d'hôte du système

## Overview
La commande `hostname` dans C Shell (csh) est utilisée pour afficher ou définir le nom d'hôte du système. Le nom d'hôte est un identifiant unique qui permet de reconnaître un ordinateur sur un réseau.

## Usage
La syntaxe de base de la commande `hostname` est la suivante :

```csh
hostname [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `hostname` :

- `-s` : Affiche uniquement le nom d'hôte court.
- `-f` : Affiche le nom d'hôte complet (FQDN).
- `-i` : Affiche l'adresse IP du nom d'hôte.
- `-d` : Affiche le domaine du nom d'hôte.

## Common Examples

1. **Afficher le nom d'hôte actuel :**
   ```csh
   hostname
   ```

2. **Afficher le nom d'hôte court :**
   ```csh
   hostname -s
   ```

3. **Afficher le nom d'hôte complet :**
   ```csh
   hostname -f
   ```

4. **Afficher l'adresse IP associée au nom d'hôte :**
   ```csh
   hostname -i
   ```

5. **Définir un nouveau nom d'hôte :**
   ```csh
   hostname nouveau_nom
   ```

## Tips
- Assurez-vous d'avoir les privilèges nécessaires pour changer le nom d'hôte, car cela peut nécessiter des droits administratifs.
- Après avoir changé le nom d'hôte, il peut être nécessaire de redémarrer le système ou de redémarrer certains services pour que les modifications prennent effet.
- Utilisez `hostname -d` pour vérifier le domaine si vous travaillez dans un environnement réseau complexe.