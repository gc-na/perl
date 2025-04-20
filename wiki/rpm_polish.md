# [Linux] C Shell (csh) rpm użycie: zarządzanie pakietami RPM

## Overview
Polecenie `rpm` jest narzędziem do zarządzania pakietami w systemach operacyjnych opartych na Red Hat. Umożliwia instalację, usuwanie, aktualizację oraz zarządzanie pakietami oprogramowania w formacie RPM (Red Hat Package Manager).

## Usage
Podstawowa składnia polecenia `rpm` jest następująca:

```bash
rpm [options] [arguments]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `rpm`:

- `-i`: Instalacja nowego pakietu.
- `-e`: Usunięcie zainstalowanego pakietu.
- `-U`: Aktualizacja zainstalowanego pakietu do nowszej wersji.
- `-q`: Zapytanie o zainstalowane pakiety.
- `-v`: Włączenie trybu szczegółowego (verbose).
- `-h`: Wyświetlenie postępu instalacji w formie pasków.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `rpm`:

1. **Instalacja pakietu:**
   ```bash
   rpm -i nazwa_pakietu.rpm
   ```

2. **Usunięcie pakietu:**
   ```bash
   rpm -e nazwa_pakietu
   ```

3. **Aktualizacja pakietu:**
   ```bash
   rpm -U nazwa_pakietu.rpm
   ```

4. **Zapytanie o zainstalowane pakiety:**
   ```bash
   rpm -q nazwa_pakietu
   ```

5. **Wyświetlenie szczegółowych informacji o pakiecie:**
   ```bash
   rpm -qi nazwa_pakietu
   ```

## Tips
- Zawsze sprawdzaj zależności pakietów przed ich instalacją, aby uniknąć problemów z brakującymi bibliotekami.
- Używaj opcji `-v` i `-h` podczas instalacji, aby uzyskać więcej informacji o postępie instalacji.
- Regularnie aktualizuj swoje pakiety, aby zapewnić bezpieczeństwo i stabilność systemu.