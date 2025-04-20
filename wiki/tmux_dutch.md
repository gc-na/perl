# [Linux] C Shell (csh) tmux gebruik: Beheer van terminalvensters

## Overzicht
De `tmux`-opdracht is een terminalmultiplexer die gebruikers in staat stelt om meerdere terminalsessies binnen één venster te beheren. Het biedt de mogelijkheid om sessies te splitsen, vensters te maken en te navigeren tussen verschillende opdrachten zonder dat je de terminal hoeft te sluiten.

## Gebruik
De basis syntaxis van de `tmux`-opdracht is als volgt:

```bash
tmux [opties] [argumenten]
```

## Veelvoorkomende Opties
- `new`: Start een nieuwe tmux-sessie.
- `attach`: Verbind met een bestaande tmux-sessie.
- `detach`: Koppel de huidige sessie los.
- `list-sessions`: Toon een lijst van actieve tmux-sessies.
- `kill-session`: Sluit een specifieke tmux-sessie.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `tmux`:

1. **Een nieuwe tmux-sessie starten**:
   ```bash
   tmux new -s mijnsessie
   ```

2. **Verbinding maken met een bestaande sessie**:
   ```bash
   tmux attach -t mijnsessie
   ```

3. **Een sessie loskoppelen**:
   Druk op `Ctrl + b`, gevolgd door `d`.

4. **Lijst van actieve sessies weergeven**:
   ```bash
   tmux list-sessions
   ```

5. **Een specifieke sessie beëindigen**:
   ```bash
   tmux kill-session -t mijnsessie
   ```

## Tips
- Gebruik `Ctrl + b` gevolgd door een toets om snel te navigeren tussen vensters en splitsingen.
- Geef je sessies duidelijke namen om ze gemakkelijker te kunnen identificeren.
- Maak gebruik van splitscreen-functionaliteit om meerdere opdrachten tegelijkertijd te monitoren en uit te voeren.