# [Linux] C Shell (csh) traceroute6 : tracer le chemin des paquets IPv6

## Overview
La commande `traceroute6` est utilisée pour déterminer le chemin emprunté par les paquets IPv6 à travers un réseau. Elle permet d'identifier les différents nœuds (routeurs) que les paquets traversent pour atteindre une destination spécifique, ce qui est utile pour le diagnostic des problèmes de réseau.

## Usage
La syntaxe de base de la commande `traceroute6` est la suivante :

```csh
traceroute6 [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `traceroute6` :

- `-m <max_ttl>` : Définit le nombre maximum de sauts (Time To Live) à suivre.
- `-p <port>` : Spécifie le port à utiliser pour les requêtes UDP.
- `-w <timeout>` : Définit le délai d'attente pour chaque réponse, en secondes.
- `-n` : N'affiche pas les noms d'hôtes, mais seulement les adresses IP.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `traceroute6` :

1. **Traceroute vers une adresse IPv6 spécifique :**

   ```csh
   traceroute6 2001:db8::1
   ```

2. **Traceroute avec un nombre maximum de sauts :**

   ```csh
   traceroute6 -m 15 2001:db8::1
   ```

3. **Utiliser un port spécifique :**

   ```csh
   traceroute6 -p 80 2001:db8::1
   ```

4. **Désactiver la résolution des noms d'hôtes :**

   ```csh
   traceroute6 -n 2001:db8::1
   ```

## Tips
- Assurez-vous que votre système prend en charge IPv6 avant d'utiliser `traceroute6`.
- Utilisez l'option `-n` si vous souhaitez des résultats plus rapides sans la résolution des noms d'hôtes.
- Vérifiez les règles de pare-feu qui pourraient bloquer les paquets ICMP, car cela peut affecter les résultats de votre traceroute.