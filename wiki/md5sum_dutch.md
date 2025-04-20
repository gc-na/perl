# [Linux] C Shell (csh) md5sum gebruik: Controleer de integriteit van bestanden

## Overzicht
De `md5sum` opdracht genereert en controleert MD5-hashes van bestanden. Dit is nuttig voor het verifiëren van de integriteit van bestanden door te controleren of ze niet zijn gewijzigd of beschadigd.

## Gebruik
De basis syntaxis van de `md5sum` opdracht is als volgt:

```csh
md5sum [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-b`: Behandel bestanden als binaire bestanden.
- `-c`: Controleer de MD5-hashes van bestanden op basis van een opgegeven bestand.
- `-t`: Behandel bestanden als tekstbestanden.
- `--help`: Toon een helpbericht met informatie over de opdracht.

## Veelvoorkomende Voorbeelden

1. **MD5-hash genereren van een bestand:**
   ```csh
   md5sum bestand.txt
   ```

2. **MD5-hash genereren van meerdere bestanden:**
   ```csh
   md5sum bestand1.txt bestand2.txt
   ```

3. **MD5-hashes controleren met een bestand:**
   Eerst genereer je een bestand met hashes:
   ```csh
   md5sum bestand.txt > hashes.md5
   ```
   Vervolgens controleer je de hashes:
   ```csh
   md5sum -c hashes.md5
   ```

4. **MD5-hash van een binaire bestand genereren:**
   ```csh
   md5sum -b bestand.bin
   ```

## Tips
- Zorg ervoor dat je de hashbestanden veilig opslaat, zodat je ze later kunt gebruiken voor verificatie.
- Gebruik de `-c` optie om snel te controleren of bestanden zijn gewijzigd zonder handmatig de hashes te vergelijken.
- Voor gevoelige gegevens, overweeg om sterkere hash-algoritmen te gebruiken, zoals SHA-256, aangezien MD5 niet meer als veilig wordt beschouwd voor cryptografische doeleinden.