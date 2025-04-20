# [Linux] C Shell (csh) rsync użycie: Synchronizacja plików i katalogów

## Przegląd
Polecenie `rsync` służy do synchronizacji plików i katalogów między lokalnym systemem a zdalnym serwerem lub między dwoma lokalnymi lokalizacjami. Jest to bardzo wydajne narzędzie, które minimalizuje ilość przesyłanych danych, kopiując tylko zmienione części plików.

## Użycie
Podstawowa składnia polecenia `rsync` jest następująca:

```csh
rsync [opcje] [argumenty]
```

## Często używane opcje
- `-a` : Archiwizuje pliki, zachowując uprawnienia, daty i inne atrybuty.
- `-v` : Włącza tryb szczegółowy, wyświetlając postęp operacji.
- `-z` : Kompresuje dane podczas przesyłania, co przyspiesza transfer.
- `-r` : Rekurencyjnie kopiuje katalogi.
- `--delete` : Usuwa pliki w docelowej lokalizacji, które nie istnieją w źródłowej.

## Przykłady
Oto kilka praktycznych przykładów użycia `rsync`:

1. Synchronizacja lokalnego katalogu z zdalnym serwerem:
   ```csh
   rsync -avz /lokalny/katalog/ użytkownik@serwer:/zdalny/katalog/
   ```

2. Kopiowanie plików z jednego lokalnego katalogu do drugiego:
   ```csh
   rsync -av /źródło/katalog/ /cel/katalog/
   ```

3. Synchronizacja z usunięciem plików, które nie istnieją w źródle:
   ```csh
   rsync -av --delete /lokalny/katalog/ użytkownik@serwer:/zdalny/katalog/
   ```

4. Synchronizacja z kompresją:
   ```csh
   rsync -avz /lokalny/katalog/ użytkownik@serwer:/zdalny/katalog/
   ```

## Wskazówki
- Zawsze testuj polecenie `rsync` z opcją `-n` (dry run), aby zobaczyć, co zostanie zrobione, zanim faktycznie wykonasz synchronizację.
- Używaj opcji `-e` do określenia, jakiego protokołu SSH użyć, jeśli łączysz się z zdalnym serwerem.
- Regularnie twórz kopie zapasowe ważnych danych, korzystając z `rsync`, aby uniknąć utraty informacji.