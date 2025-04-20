# [Linux] C Shell (csh) docker-compose użycie: Zarządzanie aplikacjami w kontenerach

## Overview
Polecenie `docker-compose` służy do definiowania i uruchamiania aplikacji składających się z wielu kontenerów Docker. Umożliwia łatwe zarządzanie konfiguracją oraz uruchamianiem aplikacji w złożonych środowiskach.

## Usage
Podstawowa składnia polecenia `docker-compose` wygląda następująco:

```bash
docker-compose [opcje] [argumenty]
```

## Common Options
- `up`: Uruchamia kontenery zdefiniowane w pliku `docker-compose.yml`.
- `down`: Zatrzymuje i usuwa kontenery, sieci oraz wolumeny utworzone przez `up`.
- `build`: Buduje obrazy kontenerów zgodnie z definicjami w pliku `docker-compose.yml`.
- `logs`: Wyświetla logi dla uruchomionych kontenerów.
- `ps`: Wyświetla listę uruchomionych kontenerów.

## Common Examples
1. **Uruchomienie aplikacji:**
   ```bash
   docker-compose up
   ```

2. **Uruchomienie aplikacji w tle:**
   ```bash
   docker-compose up -d
   ```

3. **Zatrzymanie i usunięcie kontenerów:**
   ```bash
   docker-compose down
   ```

4. **Budowanie obrazów kontenerów:**
   ```bash
   docker-compose build
   ```

5. **Wyświetlenie logów kontenerów:**
   ```bash
   docker-compose logs
   ```

## Tips
- Używaj opcji `-d`, aby uruchomić kontenery w tle, co pozwala na dalszą pracę w terminalu.
- Regularnie przeglądaj logi kontenerów, aby monitorować ich działanie i diagnozować problemy.
- Zawsze twórz plik `docker-compose.yml` w głównym katalogu projektu, aby ułatwić zarządzanie konfiguracją.