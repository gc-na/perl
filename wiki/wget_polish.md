# [Linux] C Shell (csh) wget użycie: Pobieranie plików z internetu

## Overview
Polecenie `wget` jest narzędziem do pobierania plików z internetu. Obsługuje różne protokoły, takie jak HTTP, HTTPS i FTP, co czyni go bardzo wszechstronnym narzędziem do ściągania zasobów z sieci.

## Usage
Podstawowa składnia polecenia `wget` jest następująca:

```bash
wget [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `wget`:

- `-O <plik>`: Zapisuje pobrany plik pod określoną nazwą.
- `-c`: Wznawia przerwane pobieranie.
- `-q`: Włącza tryb cichy, aby nie wyświetlać informacji o postępie.
- `--limit-rate=<prędkość>`: Ogranicza prędkość pobierania do określonej wartości.
- `-r`: Włącza rekurencyjne pobieranie, co pozwala na pobieranie całych stron internetowych.

## Common Examples
Oto kilka praktycznych przykładów użycia `wget`:

1. Pobieranie pliku z określonym adresem URL:
   ```bash
   wget https://example.com/plik.txt
   ```

2. Zapisanie pliku pod inną nazwą:
   ```bash
   wget -O nowy_plik.txt https://example.com/plik.txt
   ```

3. Wznawianie przerwanego pobierania:
   ```bash
   wget -c https://example.com/plik.txt
   ```

4. Ograniczenie prędkości pobierania do 100 KB/s:
   ```bash
   wget --limit-rate=100k https://example.com/plik.txt
   ```

5. Rekurencyjne pobieranie całej strony internetowej:
   ```bash
   wget -r https://example.com/
   ```

## Tips
- Używaj opcji `-q`, aby uniknąć zbyt wielu informacji w terminalu, zwłaszcza przy dużych pobraniach.
- Zawsze sprawdzaj, czy masz wystarczająco dużo miejsca na dysku przed rozpoczęciem pobierania dużych plików.
- Jeśli pobierasz wiele plików, rozważ użycie opcji `-i`, aby wskazać plik z listą URL-i do pobrania.