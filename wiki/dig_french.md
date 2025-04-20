# [Linux] C Shell (csh) dig <Utilisation équivalente>: Interroger les enregistrements DNS

## Overview
La commande `dig` (Domain Information Groper) est un outil puissant utilisé pour interroger les serveurs DNS. Elle permet d'obtenir des informations sur les enregistrements DNS d'un domaine, tels que les adresses IP, les enregistrements MX, et bien plus encore.

## Usage
La syntaxe de base de la commande `dig` est la suivante :

```csh
dig [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `dig` :

- `@server` : Spécifie un serveur DNS à interroger.
- `-t type` : Définit le type d'enregistrement DNS à interroger (ex. A, MX, TXT).
- `+short` : Affiche une sortie simplifiée, ne montrant que les résultats pertinents.
- `+trace` : Suit la chaîne de résolution DNS jusqu'à la réponse finale.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `dig` :

1. **Interroger un enregistrement A** :
   ```csh
   dig example.com
   ```

2. **Interroger un enregistrement MX** :
   ```csh
   dig -t MX example.com
   ```

3. **Utiliser un serveur DNS spécifique** :
   ```csh
   dig @8.8.8.8 example.com
   ```

4. **Obtenir une sortie courte** :
   ```csh
   dig +short example.com
   ```

5. **Suivre la chaîne de résolution DNS** :
   ```csh
   dig +trace example.com
   ```

## Tips
- Utilisez l'option `+short` pour obtenir des résultats plus lisibles, surtout lorsque vous ne voulez que les adresses IP.
- Pour des diagnostics avancés, l'option `+trace` peut vous aider à comprendre le chemin de résolution DNS.
- Pensez à interroger différents serveurs DNS pour comparer les résultats, surtout si vous suspectez un problème de propagation DNS.