# [Linux] C Shell (csh) tmux utilizare: Gestionarea sesiunilor terminalului

## Overview
Comanda `tmux` este un multiplexor de terminal care permite utilizatorilor să creeze, să gestioneze și să navigheze între mai multe sesiuni de terminal într-o singură fereastră. Aceasta este extrem de utilă pentru gestionarea mai multor procese simultan și pentru păstrarea sesiunilor active chiar și după deconectare.

## Usage
Sintaxa de bază a comenzii `tmux` este următoarea:

```bash
tmux [opțiuni] [argumente]
```

## Common Options
- `new`: Creează o nouă sesiune tmux.
- `attach`: Se atașează la o sesiune existentă.
- `list-sessions`: Listează toate sesiunile tmux active.
- `kill-session`: Închide o sesiune tmux specificată.
- `detach`: Deconectează sesiunea curentă.

## Common Examples
1. **Crearea unei noi sesiuni tmux:**
   ```bash
   tmux new -s nume_sesiune
   ```

2. **Atașarea la o sesiune existentă:**
   ```bash
   tmux attach -t nume_sesiune
   ```

3. **Listarea sesiunilor active:**
   ```bash
   tmux list-sessions
   ```

4. **Închiderea unei sesiuni tmux:**
   ```bash
   tmux kill-session -t nume_sesiune
   ```

5. **Deconectarea de la sesiunea curentă:**
   ```bash
   Ctrl + b, d
   ```

## Tips
- Folosește combinația de taste `Ctrl + b` urmată de `c` pentru a crea un nou panou în sesiunea curentă.
- Poți împărți fereastra în panouri verticale sau orizontale folosind `Ctrl + b`, apoi `"` pentru panouri orizontale sau `%` pentru panouri verticale.
- Salvează sesiunea ta tmux pentru a o putea relua mai târziu, folosind comanda `tmux attach` după ce te-ai deconectat.