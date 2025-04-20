# [Linux] C Shell (csh) docker użycie: zarządzanie kontenerami

## Overview
Polecenie `docker` jest używane do zarządzania kontenerami aplikacji. Umożliwia użytkownikom tworzenie, uruchamianie i zarządzanie kontenerami, które są lekkimi, przenośnymi jednostkami oprogramowania.

## Usage
Podstawowa składnia polecenia `docker` jest następująca:

```csh
docker [options] [arguments]
```

## Common Options
- `run`: Uruchamia nowy kontener.
- `ps`: Wyświetla uruchomione kontenery.
- `stop`: Zatrzymuje działający kontener.
- `rm`: Usuwa zatrzymany kontener.
- `images`: Wyświetla listę dostępnych obrazów.

## Common Examples
1. Uruchomienie nowego kontenera z obrazem `nginx`:
   ```csh
   docker run -d -p 80:80 nginx
   ```

2. Wyświetlenie uruchomionych kontenerów:
   ```csh
   docker ps
   ```

3. Zatrzymanie kontenera o identyfikatorze `abc123`:
   ```csh
   docker stop abc123
   ```

4. Usunięcie zatrzymanego kontenera o identyfikatorze `abc123`:
   ```csh
   docker rm abc123
   ```

5. Wyświetlenie dostępnych obrazów:
   ```csh
   docker images
   ```

## Tips
- Zawsze sprawdzaj, czy kontener działa przed próbą jego zatrzymania lub usunięcia.
- Używaj opcji `-d` (detached mode), aby uruchomić kontener w tle.
- Regularnie usuwaj nieużywane obrazy i kontenery, aby zaoszczędzić miejsce na dysku.