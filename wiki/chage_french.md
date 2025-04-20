# [Linux] C Shell (csh) chage : Gestion des informations de changement de mot de passe

## Overview
La commande `chage` est utilisée pour modifier les informations relatives aux changements de mot de passe d'un utilisateur sur un système Linux. Elle permet de définir des politiques de mot de passe, comme la durée de validité, la période d'avertissement avant expiration, et d'autres paramètres de sécurité.

## Usage
La syntaxe de base de la commande `chage` est la suivante :

```csh
chage [options] [arguments]
```

## Common Options
- `-l` : Affiche les informations de changement de mot de passe pour un utilisateur spécifié.
- `-m` : Définit le nombre minimum de jours entre les changements de mot de passe.
- `-M` : Définit le nombre maximum de jours pendant lesquels un mot de passe est valide.
- `-I` : Définit le nombre de jours d'inactivité avant que le compte soit désactivé.
- `-W` : Définit le nombre de jours d'avertissement avant l'expiration du mot de passe.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `chage` :

1. **Afficher les informations de changement de mot de passe pour un utilisateur :**
   ```csh
   chage -l username
   ```

2. **Définir un minimum de 7 jours entre les changements de mot de passe :**
   ```csh
   chage -m 7 username
   ```

3. **Définir un maximum de 90 jours de validité pour le mot de passe :**
   ```csh
   chage -M 90 username
   ```

4. **Configurer une période d'avertissement de 14 jours avant l'expiration :**
   ```csh
   chage -W 14 username
   ```

5. **Désactiver le compte après 30 jours d'inactivité :**
   ```csh
   chage -I 30 username
   ```

## Tips
- Assurez-vous d'utiliser `chage` avec les privilèges appropriés, généralement en tant que superutilisateur.
- Vérifiez régulièrement les politiques de mot de passe pour vous assurer qu'elles répondent aux exigences de sécurité de votre organisation.
- Utilisez l'option `-l` pour vérifier les paramètres actuels avant de faire des modifications.