# [Linux] C Shell (csh) df Verwendung: Zeigt den verfügbaren Speicherplatz auf Dateisystemen an

## Übersicht
Der Befehl `df` (disk free) wird verwendet, um Informationen über den verfügbaren und verwendeten Speicherplatz auf Dateisystemen anzuzeigen. Er gibt eine Übersicht über die Speicherkapazität und hilft Benutzern, den Status ihrer Festplatten zu überwachen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
df [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`: Zeigt die Größen in menschenlesbarem Format (z. B. KB, MB, GB) an.
- `-T`: Zeigt den Typ des Dateisystems an.
- `-i`: Zeigt Informationen über inodes an, einschließlich der Anzahl der verwendeten und verfügbaren inodes.
- `-a`: Zeigt auch die Dateisysteme an, die 0 Blöcke haben.

## Häufige Beispiele
1. **Standardnutzung von df**:
   ```csh
   df
   ```
   Dieser Befehl zeigt eine Übersicht über alle gemounteten Dateisysteme und deren Speicherplatznutzung.

2. **Menschenlesbare Ausgabe**:
   ```csh
   df -h
   ```
   Mit dieser Option werden die Größen in einem leicht verständlichen Format angezeigt.

3. **Dateisystemtyp anzeigen**:
   ```csh
   df -T
   ```
   Dieser Befehl zeigt zusätzlich den Typ jedes Dateisystems an.

4. **Inode-Nutzung anzeigen**:
   ```csh
   df -i
   ```
   Hiermit erhalten Sie Informationen über die Verwendung von inodes auf den Dateisystemen.

5. **Alle Dateisysteme anzeigen**:
   ```csh
   df -a
   ```
   Dieser Befehl zeigt auch Dateisysteme an, die keinen Speicherplatz belegen.

## Tipps
- Verwenden Sie die Option `-h`, um die Ausgabe einfacher zu lesen, insbesondere wenn Sie mit großen Datenmengen arbeiten.
- Überprüfen Sie regelmäßig den Speicherplatz, um sicherzustellen, dass Ihr System nicht voll wird, was zu Leistungsproblemen führen kann.
- Kombinieren Sie `df` mit anderen Befehlen wie `grep`, um spezifische Informationen zu filtern, z. B. nur für ein bestimmtes Dateisystem.