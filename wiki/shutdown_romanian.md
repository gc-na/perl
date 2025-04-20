# [Linux] C Shell (csh) shutdown utilizare: Oprirea sistemului

## Overview
Comanda `shutdown` este utilizată pentru a opri sau reporni sistemul de operare. Aceasta permite administratorilor să planifice închiderea sistemului într-un mod controlat, asigurându-se că toate procesele sunt terminate corespunzător și că utilizatorii sunt avertizați înainte de oprire.

## Usage
Sintaxa de bază a comenzii `shutdown` este următoarea:

```
shutdown [options] [arguments]
```

## Common Options
- `-h`: Oprește sistemul.
- `-r`: Repornește sistemul.
- `-k`: Trimite un mesaj de avertizare, dar nu oprește sistemul.
- `time`: Specifică timpul la care se va efectua oprirea (de exemplu, `now` pentru imediat sau `+5` pentru în 5 minute).
- `message`: Un mesaj opțional care va fi trimis utilizatorilor conectați.

## Common Examples
1. Oprirea imediată a sistemului:
   ```bash
   shutdown -h now
   ```

2. Repornirea sistemului după 10 minute:
   ```bash
   shutdown -r +10
   ```

3. Oprirea sistemului la o oră specifică (de exemplu, 22:30):
   ```bash
   shutdown -h 22:30
   ```

4. Avertizarea utilizatorilor fără a opri sistemul:
   ```bash
   shutdown -k now "Sistemul va fi oprit în 5 minute!"
   ```

## Tips
- Asigurați-vă că ați salvat toate lucrările înainte de a executa comanda `shutdown`, deoarece aceasta va închide toate aplicațiile deschise.
- Utilizați opțiunea `-k` pentru a trimite un mesaj de avertizare înainte de a efectua o oprire reală, astfel încât utilizatorii să fie informați.
- Verificați întotdeauna dacă aveți permisiunile necesare pentru a utiliza comanda `shutdown`, deoarece aceasta este de obicei restricționată la utilizatorii cu privilegii de administrator.