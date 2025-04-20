# [Linux] C Shell (csh) nslookup Utilisation : Interroger des serveurs DNS

## Overview
La commande `nslookup` est utilisée pour interroger les serveurs DNS afin de récupérer des informations sur les noms de domaine, comme les adresses IP associées. Elle est utile pour diagnostiquer des problèmes de réseau et vérifier la configuration DNS.

## Usage
La syntaxe de base de la commande `nslookup` est la suivante :

```
nslookup [options] [arguments]
```

## Common Options
- `-type=TYPE` : Spécifie le type d'enregistrement DNS à rechercher (ex. A, AAAA, MX).
- `-timeout=SECONDS` : Définit le délai d'attente pour la réponse du serveur DNS.
- `-retry=NUMBER` : Indique le nombre de tentatives en cas d'échec de la requête.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `nslookup` :

1. **Obtenir l'adresse IP d'un domaine :**
   ```bash
   nslookup example.com
   ```

2. **Rechercher un enregistrement de type MX :**
   ```bash
   nslookup -type=MX example.com
   ```

3. **Spécifier un serveur DNS lors de la requête :**
   ```bash
   nslookup example.com 8.8.8.8
   ```

4. **Vérifier un enregistrement de type AAAA (IPv6) :**
   ```bash
   nslookup -type=AAAA example.com
   ```

## Tips
- Utilisez `nslookup` avec un serveur DNS public comme 8.8.8.8 pour tester la résolution de noms en dehors de votre réseau local.
- Pensez à vérifier différents types d'enregistrements pour obtenir des informations complètes sur un domaine.
- En cas de problème de résolution, essayez de redémarrer votre connexion réseau ou de vérifier la configuration DNS de votre système.