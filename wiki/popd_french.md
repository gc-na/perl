# [Linux] C Shell (csh) popd Utilisation : Gérer la pile de répertoires

## Overview
La commande `popd` dans le C Shell (csh) est utilisée pour supprimer le répertoire supérieur de la pile de répertoires et changer le répertoire de travail courant pour ce répertoire. Cela permet de naviguer facilement entre plusieurs répertoires sans avoir à saisir les chemins complets.

## Usage
La syntaxe de base de la commande `popd` est la suivante :

```
popd [options] [arguments]
```

## Common Options
- `-n` : Ne change pas le répertoire courant, mais affiche le répertoire qui serait supprimé.
- `+n` : Supprime le n-ième répertoire de la pile, en commençant par 0 pour le plus récent.

## Common Examples

### Exemple 1 : Utiliser popd pour revenir au répertoire précédent
```csh
pushd /chemin/vers/repertoire1
pushd /chemin/vers/repertoire2
popd
```
Dans cet exemple, après avoir exécuté `popd`, vous serez de retour dans `/chemin/vers/repertoire1`.

### Exemple 2 : Utiliser popd avec l'option -n
```csh
pushd /chemin/vers/repertoire1
pushd /chemin/vers/repertoire2
popd -n
```
Ici, `popd -n` affichera le répertoire qui serait supprimé sans changer le répertoire courant.

### Exemple 3 : Utiliser popd avec l'option +n
```csh
pushd /chemin/vers/repertoire1
pushd /chemin/vers/repertoire2
pushd /chemin/vers/repertoire3
popd +1
```
Dans cet exemple, `popd +1` supprimera `/chemin/vers/repertoire2` de la pile et vous resterez dans `/chemin/vers/repertoire3`.

## Tips
- Utilisez `pushd` avant `popd` pour ajouter des répertoires à la pile de manière organisée.
- Vérifiez la pile de répertoires actuelle avec la commande `dirs` avant d'utiliser `popd` pour savoir quel répertoire sera supprimé.
- Combinez `popd` avec des scripts pour automatiser la navigation dans des répertoires complexes.