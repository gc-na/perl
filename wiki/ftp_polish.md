# [Linux] C Shell (csh) ftp użycie: Przesyłanie plików przez protokół FTP

## Przegląd
Polecenie `ftp` w C Shell (csh) służy do przesyłania plików między komputerem lokalnym a serwerem FTP. Umożliwia użytkownikom łączenie się z serwerami FTP, pobieranie i wysyłanie plików oraz zarządzanie plikami na serwerze.

## Użycie
Podstawowa składnia polecenia `ftp` wygląda następująco:

```csh
ftp [opcje] [argumenty]
```

## Częste opcje
- `-v`: Włącza tryb szczegółowy, wyświetlając więcej informacji o połączeniu.
- `-n`: Nie nawiązuje automatycznie połączenia z serwerem po uruchomieniu.
- `-i`: Wyłącza tryb interaktywny, co jest przydatne przy przesyłaniu wielu plików.
- `-g`: Wyłącza globbing, co pozwala na przesyłanie plików z nazwami zawierającymi znaki specjalne.

## Częste przykłady
### Połączenie z serwerem FTP
Aby połączyć się z serwerem FTP, użyj polecenia:

```csh
ftp ftp.example.com
```

### Pobieranie pliku
Aby pobrać plik z serwera FTP, po nawiązaniu połączenia użyj polecenia `get`:

```csh
get plik.txt
```

### Wysyłanie pliku
Aby wysłać plik na serwer FTP, użyj polecenia `put`:

```csh
put plik.txt
```

### Pobieranie wielu plików
Aby pobrać wiele plików, najpierw włącz tryb interaktywny:

```csh
ftp -i ftp.example.com
mget *.txt
```

## Wskazówki
- Zawsze sprawdzaj, czy masz odpowiednie uprawnienia do przesyłania lub pobierania plików z serwera.
- Używaj trybu szczegółowego (`-v`), aby uzyskać więcej informacji o błędach podczas połączenia.
- Pamiętaj o bezpiecznym przechowywaniu danych logowania do serwera FTP, aby uniknąć nieautoryzowanego dostępu.