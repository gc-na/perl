# [Linux] C Shell (csh) mtr Użycie: Narzędzie do diagnostyki trasowania pakietów

## Przegląd
Polecenie `mtr` (My Traceroute) jest narzędziem do diagnostyki sieci, które łączy funkcje polecenia `traceroute` i `ping`. Umożliwia użytkownikom monitorowanie ścieżki, jaką pakiety danych pokonują do określonego hosta, a także mierzenie czasu odpowiedzi na każdym etapie trasy.

## Użycie
Podstawowa składnia polecenia `mtr` jest następująca:

```
mtr [opcje] [argumenty]
```

## Często używane opcje
- `-r` – Uruchamia `mtr` w trybie raportu, co oznacza, że po zakończeniu działania wyświetli podsumowanie.
- `-c [liczba]` – Określa liczbę wysyłanych pakietów (domyślnie 10).
- `-i [czas]` – Ustala interwał między wysyłanymi pakietami w sekundach.
- `-p` – Uruchamia `mtr` w trybie tylko ping, bez śledzenia trasy.

## Przykłady
Oto kilka praktycznych przykładów użycia polecenia `mtr`:

1. **Podstawowe użycie mtr do śledzenia trasy do hosta:**
   ```bash
   mtr example.com
   ```

2. **Uruchomienie mtr w trybie raportu:**
   ```bash
   mtr -r example.com
   ```

3. **Określenie liczby wysyłanych pakietów:**
   ```bash
   mtr -c 5 example.com
   ```

4. **Ustalenie interwału między pakietami:**
   ```bash
   mtr -i 1 example.com
   ```

5. **Użycie mtr w trybie tylko ping:**
   ```bash
   mtr -p example.com
   ```

## Wskazówki
- Używaj opcji `-r`, aby uzyskać zwięzłe podsumowanie po zakończeniu testu.
- Zwiększ liczbę pakietów za pomocą opcji `-c`, aby uzyskać dokładniejsze wyniki w przypadku niestabilnych połączeń.
- Regularnie monitoruj różne hosty, aby zidentyfikować problemy z siecią.
- Pamiętaj, że niektóre serwery mogą blokować pakiety ICMP, co może wpłynąć na wyniki `mtr`.