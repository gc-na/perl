# [Linux] C Shell (csh) xz : Compresser des fichiers

## Overview
La commande `xz` est utilisée pour compresser et décompresser des fichiers en utilisant l'algorithme de compression LZMA. Elle est particulièrement efficace pour réduire la taille des fichiers, ce qui facilite le stockage et le transfert.

## Usage
La syntaxe de base de la commande `xz` est la suivante :

```csh
xz [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `xz` :

- `-d` ou `--decompress` : Décompresse un fichier.
- `-k` ou `--keep` : Garde le fichier original après compression.
- `-f` ou `--force` : Force la compression même si le fichier de destination existe déjà.
- `-9` : Utilise le niveau de compression maximum.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `xz` :

1. **Compresser un fichier :**
   ```csh
   xz fichier.txt
   ```

2. **Décompresser un fichier :**
   ```csh
   xz -d fichier.txt.xz
   ```

3. **Compresser un fichier tout en gardant l'original :**
   ```csh
   xz -k fichier.txt
   ```

4. **Forcer la compression d'un fichier existant :**
   ```csh
   xz -f fichier.txt
   ```

5. **Compresser avec le niveau de compression maximum :**
   ```csh
   xz -9 fichier.txt
   ```

## Tips
- Utilisez l'option `-k` si vous souhaitez conserver le fichier original après compression.
- Pour des fichiers très volumineux, envisagez d'utiliser le niveau de compression maximum (`-9`), mais sachez que cela peut augmenter le temps de compression.
- Vérifiez toujours l'espace disque disponible avant de compresser des fichiers, surtout si vous ne conservez pas les originaux.