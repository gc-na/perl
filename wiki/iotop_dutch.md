# [Linux] C Shell (csh) iotop gebruik: Monitoren van schijfactiviteit

## Overzicht
Het `iotop` commando is een nuttig hulpmiddel voor het monitoren van de schijfactiviteit op een Linux-systeem. Het toont welke processen de meeste I/O-bronnen gebruiken, waardoor je inzicht krijgt in de prestaties van je systeem.

## Gebruik
De basis syntaxis van het `iotop` commando is als volgt:

```bash
iotop [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-o`, `--only`: Toont alleen processen die momenteel I/O-activiteit genereren.
- `-b`, `--batch`: Voert `iotop` uit in batchmodus, wat handig is voor logging.
- `-n NUM`, `--iter NUM`: Specificeert het aantal iteraties dat `iotop` moet uitvoeren voordat het stopt.
- `-d SEC`, `--delay SEC`: Stelt de vertraging in seconden in tussen updates.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `iotop`:

1. **Basis gebruik van iotop**:
   ```bash
   iotop
   ```

2. **Alleen processen met I/O-activiteit tonen**:
   ```bash
   iotop -o
   ```

3. **Uitvoeren in batchmodus voor logging**:
   ```bash
   iotop -b -n 10
   ```

4. **Vertraging van 2 seconden tussen updates**:
   ```bash
   iotop -d 2
   ```

## Tips
- Gebruik `iotop` met root-rechten voor een volledig overzicht van alle processen.
- Combineer `iotop` met andere monitoring tools voor een uitgebreider beeld van systeembronnen.
- Houd rekening met de impact van `iotop` op systeembronnen, vooral bij gebruik in batchmodus.