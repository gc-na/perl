# [Linux] C Shell (csh) tmux Verwendung: Terminal-Multiplexer

## Übersicht
Der Befehl `tmux` ist ein Terminal-Multiplexer, der es ermöglicht, mehrere Terminal-Sitzungen innerhalb eines einzigen Fensters zu verwalten. Mit tmux können Benutzer zwischen verschiedenen Sitzungen wechseln, Fenster teilen und ihre Arbeit effizient organisieren.

## Verwendung
Die grundlegende Syntax des tmux-Befehls lautet:

```bash
tmux [Optionen] [Argumente]
```

## Häufige Optionen
- `new`: Erstellt eine neue tmux-Sitzung.
- `attach`: Verbindet sich mit einer bestehenden tmux-Sitzung.
- `list-sessions`: Listet alle aktiven tmux-Sitzungen auf.
- `kill-session`: Beendet eine tmux-Sitzung.
- `detach`: Trennt die aktuelle tmux-Sitzung.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von tmux:

### Neue tmux-Sitzung erstellen
```bash
tmux new -s meine_sitzung
```

### Mit einer bestehenden Sitzung verbinden
```bash
tmux attach -t meine_sitzung
```

### Alle aktiven Sitzungen auflisten
```bash
tmux list-sessions
```

### Eine Sitzung beenden
```bash
tmux kill-session -t meine_sitzung
```

### Sitzung trennen
```bash
tmux detach
```

## Tipps
- Verwenden Sie `Ctrl + b` gefolgt von `%`, um das aktuelle Fenster vertikal zu teilen.
- Nutzen Sie `Ctrl + b` gefolgt von `"` für eine horizontale Teilung des Fensters.
- Speichern Sie Ihre tmux-Konfiguration in der Datei `~/.tmux.conf`, um Ihre Einstellungen anzupassen und zu speichern.