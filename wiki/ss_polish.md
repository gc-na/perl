# [Linux] C Shell (csh) ss użycie: Wyświetlanie informacji o gniazdach sieciowych

## Overview
Polecenie `ss` służy do wyświetlania informacji o gniazdach sieciowych w systemie. Umożliwia użytkownikom monitorowanie połączeń sieciowych, zarówno aktywnych, jak i nasłuchujących, oraz analizowanie stanu gniazd.

## Usage
Podstawowa składnia polecenia `ss` wygląda następująco:

```bash
ss [opcje] [argumenty]
```

## Common Options
- `-t` – wyświetla tylko połączenia TCP.
- `-u` – wyświetla tylko połączenia UDP.
- `-l` – pokazuje tylko gniazda nasłuchujące.
- `-p` – wyświetla procesy powiązane z gniazdami.
- `-n` – wyświetla numery portów i adresy IP w formie numerycznej, zamiast rozwiązywać je na nazwy.

## Common Examples
1. Wyświetlenie wszystkich aktywnych połączeń TCP:
   ```bash
   ss -t
   ```

2. Wyświetlenie wszystkich gniazd nasłuchujących:
   ```bash
   ss -l
   ```

3. Wyświetlenie połączeń UDP:
   ```bash
   ss -u
   ```

4. Wyświetlenie gniazd z informacjami o procesach:
   ```bash
   ss -p
   ```

5. Wyświetlenie wszystkich połączeń w formie numerycznej:
   ```bash
   ss -n
   ```

## Tips
- Używaj opcji `-p`, aby zidentyfikować, które procesy są powiązane z danym gniazdem, co może być pomocne w diagnostyce.
- Kombinuj różne opcje, aby uzyskać bardziej szczegółowe informacje, na przykład `ss -tunlp`, aby zobaczyć wszystkie połączenia TCP i UDP z informacjami o procesach.
- Regularne monitorowanie gniazd sieciowych może pomóc w identyfikacji nieautoryzowanych połączeń lub problemów z wydajnością.