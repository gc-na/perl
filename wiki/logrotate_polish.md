# [Linux] C Shell (csh) logrotate użycie: zarządzanie rotacją plików dziennika

## Przegląd
Polecenie `logrotate` jest używane do zarządzania rotacją plików dziennika. Umożliwia automatyczne archiwizowanie, usuwanie lub kompresowanie starych plików dziennika, co pomaga w zarządzaniu przestrzenią dyskową i utrzymaniu porządku w systemie.

## Użycie
Podstawowa składnia polecenia `logrotate` jest następująca:

```bash
logrotate [opcje] [argumenty]
```

## Typowe opcje
- `-f`: Wymusza rotację plików dziennika, niezależnie od ustawień.
- `-s`: Określa plik stanu, który przechowuje informacje o rotacji.
- `-v`: Włącza tryb szczegółowy, wyświetlając więcej informacji o procesie rotacji.
- `-d`: Uruchamia logrotate w trybie debugowania, bez wprowadzania zmian.

## Przykłady
Przykład 1: Rotacja plików dziennika zgodnie z domyślną konfiguracją.

```bash
logrotate /etc/logrotate.conf
```

Przykład 2: Wymuszenie rotacji plików dziennika.

```bash
logrotate -f /etc/logrotate.conf
```

Przykład 3: Uruchomienie logrotate w trybie szczegółowym.

```bash
logrotate -v /etc/logrotate.conf
```

Przykład 4: Użycie pliku stanu do śledzenia rotacji.

```bash
logrotate -s /var/lib/logrotate/status /etc/logrotate.conf
```

## Wskazówki
- Regularnie przeglądaj konfigurację `logrotate`, aby upewnić się, że pliki dziennika są odpowiednio zarządzane.
- Używaj opcji `-v` podczas testowania nowych konfiguracji, aby zobaczyć, co się dzieje.
- Zautomatyzuj rotację plików dziennika, dodając `logrotate` do crontaba, aby działał w regularnych odstępach czasu.