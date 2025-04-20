# [Linux] C Shell (csh) cal <Utilisation équivalente en français> : Afficher un calendrier

## Aperçu
La commande `cal` dans C Shell (csh) permet d'afficher un calendrier pour un mois ou une année spécifiée. Elle est utile pour visualiser rapidement les dates et les jours de la semaine.

## Utilisation
La syntaxe de base de la commande `cal` est la suivante :

```csh
cal [options] [arguments]
```

## Options courantes
- `-1` : Affiche le calendrier d'un mois.
- `-3` : Affiche le calendrier du mois courant, du mois précédent et du mois suivant.
- `-y` : Affiche le calendrier de l'année en cours.
- `-m` : Définit le premier jour de la semaine (0 pour dimanche, 1 pour lundi, etc.).

## Exemples courants
Voici quelques exemples pratiques de l'utilisation de la commande `cal` :

1. Afficher le calendrier du mois courant :
   ```csh
   cal
   ```

2. Afficher le calendrier d'un mois spécifique (par exemple, mars 2023) :
   ```csh
   cal 03 2023
   ```

3. Afficher le calendrier de l'année en cours :
   ```csh
   cal -y
   ```

4. Afficher le calendrier des trois mois (mois précédent, mois courant et mois suivant) :
   ```csh
   cal -3
   ```

5. Afficher le calendrier d'une année spécifique (par exemple, 2024) :
   ```csh
   cal 2024
   ```

## Conseils
- Utilisez l'option `-m` pour personnaliser le premier jour de la semaine selon vos préférences.
- Combinez `cal` avec d'autres commandes pour des scripts plus complexes, par exemple, pour envoyer des rappels de dates importantes.
- N'oubliez pas que `cal` peut être utilisé dans des scripts shell pour automatiser l'affichage de calendriers.