# [Linux] C Shell (csh) write utilisation : envoyer des messages à d'autres utilisateurs

## Overview
La commande `write` dans C Shell (csh) permet d'envoyer des messages instantanés à d'autres utilisateurs connectés sur le même système. Cela peut être utile pour la communication rapide entre utilisateurs sans avoir à utiliser un client de messagerie ou un e-mail.

## Usage
La syntaxe de base de la commande `write` est la suivante :

```csh
write [options] [utilisateur] [terminal]
```

## Common Options
- `-n` : Ne pas afficher le nom de l'expéditeur dans le message.
- `-h` : Afficher un message d'aide sur l'utilisation de la commande.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `write` :

1. **Envoyer un message à un utilisateur spécifique :**

```csh
write alice pts/1
```
Cet exemple envoie un message à l'utilisateur `alice` sur le terminal `pts/1`.

2. **Envoyer un message sans afficher le nom de l'expéditeur :**

```csh
write -n bob pts/2
```
Ici, le message est envoyé à `bob` sur le terminal `pts/2`, sans afficher le nom de l'expéditeur.

3. **Envoyer un message et terminer la session :**

```csh
write charlie pts/3
Bonjour Charlie, comment ça va ?
```
Après avoir tapé le message, appuyez sur `Ctrl+D` pour terminer la session d'écriture.

## Tips
- Assurez-vous que l'utilisateur que vous essayez de joindre est connecté et que son terminal est accessible.
- Utilisez `who` pour voir les utilisateurs connectés et leurs terminaux avant d'envoyer un message.
- Soyez concis dans vos messages pour une communication efficace.