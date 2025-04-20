# [Linux] C Shell (csh) iotop : surveiller l'utilisation des entrées/sorties

## Overview
La commande `iotop` est un outil qui permet de surveiller l'utilisation des entrées/sorties (I/O) des processus en temps réel. Elle affiche les processus qui consomment le plus de bande passante I/O, ce qui est utile pour diagnostiquer les problèmes de performance liés aux disques.

## Usage
La syntaxe de base de la commande `iotop` est la suivante :

```bash
iotop [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `iotop` :

- `-o` : Affiche uniquement les processus qui effectuent des opérations I/O.
- `-b` : Exécute `iotop` en mode batch, utile pour les scripts.
- `-n NUM` : Définit le nombre d'itérations à afficher avant de quitter.
- `-d SECONDS` : Définit l'intervalle de mise à jour en secondes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `iotop` :

1. **Afficher tous les processus I/O en temps réel :**
   ```bash
   iotop
   ```

2. **Afficher uniquement les processus qui effectuent des opérations I/O :**
   ```bash
   iotop -o
   ```

3. **Exécuter iotop en mode batch pour 5 itérations avec un intervalle de 2 secondes :**
   ```bash
   iotop -b -n 5 -d 2
   ```

4. **Surveiller les processus I/O en arrière-plan :**
   ```bash
   iotop -b > iotop_output.txt
   ```

## Tips
- Utilisez l'option `-o` pour filtrer les processus inactifs et vous concentrer sur ceux qui consomment réellement des ressources.
- Si vous surveillez un système pendant une longue période, envisagez d'utiliser le mode batch pour enregistrer les résultats dans un fichier.
- Assurez-vous d'exécuter `iotop` avec des privilèges suffisants (souvent en tant que superutilisateur) pour voir tous les processus.