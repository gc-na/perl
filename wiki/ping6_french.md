# [Linux] C Shell (csh) ping6 : Vérifier la connectivité IPv6

## Overview
La commande `ping6` est utilisée pour tester la connectivité réseau entre l'hôte local et un autre hôte sur un réseau utilisant le protocole IPv6. Elle envoie des paquets ICMPv6 Echo Request et attend des réponses Echo Reply, permettant ainsi de diagnostiquer les problèmes de réseau.

## Usage
La syntaxe de base de la commande est la suivante :

```csh
ping6 [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `ping6` :

- `-c <count>` : Spécifie le nombre de paquets à envoyer.
- `-i <interval>` : Définit l'intervalle en secondes entre l'envoi des paquets.
- `-s <size>` : Définit la taille des paquets à envoyer.
- `-W <timeout>` : Définit le délai d'attente pour une réponse, en secondes.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `ping6` :

1. **Pinger un hôte IPv6 :**
   ```csh
   ping6 google.com
   ```

2. **Envoyer un nombre spécifique de paquets :**
   ```csh
   ping6 -c 5 google.com
   ```

3. **Définir un intervalle entre les paquets :**
   ```csh
   ping6 -i 2 google.com
   ```

4. **Changer la taille des paquets :**
   ```csh
   ping6 -s 128 google.com
   ```

5. **Définir un délai d'attente pour les réponses :**
   ```csh
   ping6 -W 2 google.com
   ```

## Tips
- Utilisez l'option `-c` pour limiter le nombre de paquets envoyés, ce qui peut être utile pour des tests rapides.
- L'option `-i` peut aider à éviter une surcharge du réseau en espaçant les paquets.
- Vérifiez toujours que l'hôte cible est accessible avant de procéder à des diagnostics plus approfondis.