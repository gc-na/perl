# [Linux] C Shell (csh) sed Utilisation : Modifier et transformer du texte

## Aperçu
La commande `sed`, qui signifie "stream editor", est un outil puissant utilisé pour manipuler et transformer du texte dans des fichiers ou des flux de données. Elle permet d'effectuer des substitutions, des suppressions et d'autres modifications sur des lignes de texte.

## Utilisation
La syntaxe de base de la commande `sed` est la suivante :

```bash
sed [options] [arguments]
```

## Options courantes
- `-e` : Permet d'exécuter plusieurs expressions `sed`.
- `-i` : Modifie le fichier en place sans créer de fichier temporaire.
- `-n` : Supprime l'affichage automatique des lignes, utile avec `p` pour afficher uniquement les lignes spécifiées.
- `s/pattern/replacement/` : Effectue une substitution de `pattern` par `replacement`.

## Exemples courants
Voici quelques exemples pratiques de l'utilisation de `sed` :

### 1. Remplacer une chaîne de caractères
Pour remplacer "chat" par "chien" dans un fichier :

```bash
sed 's/chat/chien/' fichier.txt
```

### 2. Modifier un fichier en place
Pour remplacer "chat" par "chien" directement dans le fichier :

```bash
sed -i 's/chat/chien/' fichier.txt
```

### 3. Afficher uniquement les lignes contenant un mot spécifique
Pour afficher uniquement les lignes contenant "chien" :

```bash
sed -n '/chien/p' fichier.txt
```

### 4. Supprimer les lignes vides
Pour supprimer toutes les lignes vides d'un fichier :

```bash
sed '/^$/d' fichier.txt
```

## Conseils
- Toujours faire une sauvegarde de vos fichiers avant d'utiliser l'option `-i` pour éviter toute perte de données.
- Utilisez l'option `-n` pour contrôler ce qui est affiché, cela peut rendre vos scripts plus clairs.
- Testez vos commandes `sed` sur un petit échantillon de données avant de les appliquer à des fichiers plus volumineux.