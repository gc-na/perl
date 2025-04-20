# [Linux] C Shell (csh) mtr Utilisation : Outil de diagnostic de réseau

## Overview
La commande `mtr` (My Traceroute) est un outil de diagnostic réseau qui combine les fonctionnalités de `ping` et de `traceroute`. Elle permet d'analyser la route prise par les paquets de données pour atteindre une destination spécifique et de mesurer la latence à chaque saut.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
mtr [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `mtr` :

- `-r` : Exécute `mtr` en mode rapport, affichant les résultats à la fin.
- `-c <count>` : Définit le nombre de paquets à envoyer.
- `-i <interval>` : Définit l'intervalle entre les paquets envoyés.
- `-p` : Affiche les numéros de port utilisés pour chaque saut.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `mtr` :

1. **Exécuter un mtr vers un hôte :**
   ```csh
   mtr example.com
   ```

2. **Exécuter un rapport mtr avec un nombre défini de paquets :**
   ```csh
   mtr -r -c 10 example.com
   ```

3. **Définir un intervalle de 2 secondes entre les paquets :**
   ```csh
   mtr -i 2 example.com
   ```

4. **Afficher les numéros de port :**
   ```csh
   mtr -p example.com
   ```

## Tips
- Utilisez l'option `-r` pour obtenir un rapport rapide après un nombre défini de paquets, ce qui est utile pour des diagnostics ponctuels.
- Pour une analyse continue, exécutez `mtr` sans l'option `-r` et laissez-le fonctionner jusqu'à ce que vous décidiez de l'arrêter.
- Vérifiez les résultats pour identifier les sauts avec une latence élevée, ce qui peut indiquer des problèmes de réseau.