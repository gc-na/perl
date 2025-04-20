# [Linux] C Shell (csh) yum Verwendung: Paketverwaltung und -installation

## Übersicht
Der `yum`-Befehl (Yellowdog Updater, Modified) ist ein Paketverwaltungstool für Linux-Distributionen, das auf RPM-Paketen basiert. Es ermöglicht Benutzern, Softwarepakete zu installieren, zu aktualisieren und zu entfernen, sowie Abhängigkeiten automatisch zu verwalten.

## Verwendung
Die grundlegende Syntax des `yum`-Befehls lautet:

```
yum [Optionen] [Argumente]
```

## Häufige Optionen
- `install`: Installiert ein oder mehrere Pakete.
- `remove`: Entfernt ein oder mehrere Pakete.
- `update`: Aktualisiert alle installierten Pakete auf die neueste Version.
- `list`: Listet verfügbare oder installierte Pakete auf.
- `search`: Sucht nach Paketen, die einem bestimmten Namen oder einer Beschreibung entsprechen.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `yum`-Befehls:

1. **Ein Paket installieren:**
   ```bash
   yum install paketname
   ```

2. **Ein Paket entfernen:**
   ```bash
   yum remove paketname
   ```

3. **Alle installierten Pakete aktualisieren:**
   ```bash
   yum update
   ```

4. **Verfügbare Pakete auflisten:**
   ```bash
   yum list available
   ```

5. **Nach einem Paket suchen:**
   ```bash
   yum search suchbegriff
   ```

## Tipps
- Verwenden Sie `yum clean all`, um den Cache zu leeren und Speicherplatz freizugeben.
- Überprüfen Sie regelmäßig auf Updates, um sicherzustellen, dass Ihre Software auf dem neuesten Stand ist.
- Nutzen Sie `yum info paketname`, um detaillierte Informationen über ein bestimmtes Paket zu erhalten, bevor Sie es installieren.