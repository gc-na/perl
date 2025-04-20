# [Linux] C Shell (csh) mkfifo użycie: Tworzenie nazwanych potoków

## Overview
Polecenie `mkfifo` w C Shell (csh) służy do tworzenia nazwanych potoków, które umożliwiają komunikację między procesami. Nazwane potoki działają jak pliki, ale zamiast przechowywać dane, pozwalają na przesyłanie danych między różnymi programami.

## Usage
Podstawowa składnia polecenia `mkfifo` jest następująca:

```csh
mkfifo [opcje] [argumenty]
```

## Common Options
- `-m, --mode=MODE` - Ustawia uprawnienia dla nowego potoku, gdzie MODE to wartość w formacie oktalnym.
- `-Z, --context=CONTEXT` - Ustawia kontekst SELinux dla nowego potoku.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `mkfifo`:

1. Tworzenie prostego nazwanego potoku:
   ```csh
   mkfifo mypipe
   ```

2. Tworzenie potoku z określonymi uprawnieniami:
   ```csh
   mkfifo -m 644 mypipe
   ```

3. Użycie potoku do przesyłania danych między dwoma procesami:
   ```csh
   mkfifo mypipe
   cat mypipe &
   echo "Hello, World!" > mypipe
   ```

4. Ustawienie kontekstu SELinux dla potoku:
   ```csh
   mkfifo -Z mypipe
   ```

## Tips
- Upewnij się, że potok jest używany przez dwa różne procesy, aby uniknąć zablokowania.
- Sprawdzaj uprawnienia potoku, aby zapewnić odpowiedni dostęp dla procesów, które będą z niego korzystać.
- Pamiętaj, że potoki są usuwane automatycznie po zamknięciu wszystkich otwartych deskryptorów, więc nie musisz ich ręcznie usuwać.