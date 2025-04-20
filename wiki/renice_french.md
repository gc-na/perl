# [Linux] C Shell (csh) renice : Modifier la priorité d'un processus

## Overview
La commande `renice` permet de modifier la priorité d'exécution d'un ou plusieurs processus en cours sur un système Unix. En ajustant la priorité, vous pouvez influencer la quantité de temps processeur qu'un processus reçoit par rapport aux autres.

## Usage
La syntaxe de base de la commande `renice` est la suivante :

```csh
renice [options] [arguments]
```

## Common Options
- `-n` : Spécifie la nouvelle valeur de priorité à appliquer. La valeur peut être positive (pour diminuer la priorité) ou négative (pour l'augmenter).
- `-p` : Permet de spécifier le PID (identifiant de processus) du processus dont vous souhaitez modifier la priorité.
- `-g` : Utilisé pour modifier la priorité de tous les processus d'un groupe de processus donné.
- `-u` : Modifie la priorité de tous les processus appartenant à un utilisateur spécifique.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `renice` :

1. Modifier la priorité d'un processus avec un PID de 1234 pour qu'elle soit plus élevée (valeur négative) :
   ```csh
   renice -n -5 -p 1234
   ```

2. Diminuer la priorité de tous les processus d'un utilisateur nommé "alice" :
   ```csh
   renice -n 10 -u alice
   ```

3. Modifier la priorité de tous les processus d'un groupe de processus avec un GID de 5678 :
   ```csh
   renice -n 5 -g 5678
   ```

4. Vérifier la priorité actuelle d'un processus avant de le modifier :
   ```csh
   ps -o pid,ni,comm | grep 1234
   ```

## Tips
- Utilisez `ps` pour vérifier les priorités des processus avant de les modifier, afin de prendre des décisions éclairées.
- Soyez prudent lorsque vous augmentez la priorité d'un processus, car cela peut affecter les performances globales du système.
- Les valeurs de priorité vont de -20 (plus haute priorité) à 19 (plus basse priorité).