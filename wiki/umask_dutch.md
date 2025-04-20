# [Linux] C Shell (csh) umask gebruik: Beheer van bestandspermissies

## Overzicht
De `umask`-opdracht in C Shell (csh) wordt gebruikt om de standaard bestandspermissies in te stellen voor nieuwe bestanden en mappen. Het bepaalt welke rechten niet worden verleend aan nieuwe bestanden die door een gebruiker worden aangemaakt.

## Gebruik
De basis syntaxis van de `umask`-opdracht is als volgt:

```
umask [opties] [argumenten]
```

## Veelvoorkomende opties
- `-S`: Toont de huidige umask in symbolische vorm.
- `-p`: Toont de huidige umask zonder deze te wijzigen.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `umask`-opdracht:

1. **Bekijk de huidige umask-waarde:**
   ```csh
   umask
   ```

2. **Stel de umask in op 022 (schrijfrechten voor de eigenaar, lees- en uitvoerrechten voor anderen):**
   ```csh
   umask 022
   ```

3. **Stel de umask in op 007 (alleen de eigenaar heeft lees-, schrijf- en uitvoerrechten):**
   ```csh
   umask 007
   ```

4. **Toon de huidige umask in symbolische vorm:**
   ```csh
   umask -S
   ```

5. **Toon de huidige umask zonder deze te wijzigen:**
   ```csh
   umask -p
   ```

## Tips
- Het is een goede gewoonte om de umask in je shell-configuratiebestand (zoals `.cshrc`) in te stellen, zodat deze automatisch wordt toegepast bij het starten van een nieuwe shell.
- Controleer regelmatig je umask-instellingen om ervoor te zorgen dat je de juiste bestandspermissies toepast, vooral op gedeelde systemen.
- Wees voorzichtig met het instellen van een te permissieve umask, omdat dit kan leiden tot beveiligingsrisico's.