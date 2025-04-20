# [Linux] C Shell (csh) dig <Użycie: zapytania DNS>

## Overview
Polecenie `dig` (Domain Information Groper) jest narzędziem do wykonywania zapytań DNS. Umożliwia użytkownikom uzyskiwanie informacji o rekordach DNS, co jest przydatne w diagnostyce problemów z siecią oraz w zarządzaniu domenami.

## Usage
Podstawowa składnia polecenia `dig` wygląda następująco:

```
dig [opcje] [argumenty]
```

## Common Options
- `@serwer` - Określa serwer DNS, do którego wysyłane jest zapytanie.
- `-t typ` - Umożliwia określenie typu rekordu DNS, np. A, AAAA, MX, itp.
- `+short` - Zwraca skróconą wersję odpowiedzi, co jest przydatne do szybkiego uzyskania informacji.
- `-x adres` - Wykonuje odwrotne zapytanie DNS, przekształcając adres IP na nazwę domeny.

## Common Examples
1. **Podstawowe zapytanie o rekord A:**
   ```bash
   dig example.com
   ```

2. **Zapytanie o rekord MX:**
   ```bash
   dig -t MX example.com
   ```

3. **Użycie konkretnego serwera DNS:**
   ```bash
   dig @8.8.8.8 example.com
   ```

4. **Odwrotne zapytanie DNS:**
   ```bash
   dig -x 8.8.8.8
   ```

5. **Skrócona odpowiedź:**
   ```bash
   dig +short example.com
   ```

## Tips
- Używaj opcji `+trace`, aby zobaczyć, jak zapytanie przechodzi przez różne serwery DNS.
- Regularnie sprawdzaj różne typy rekordów, aby uzyskać pełny obraz konfiguracji DNS danej domeny.
- Zapisuj wyniki zapytań w plikach, aby móc je łatwo analizować później.