# [Linux] C Shell (csh) tr <Użycie>: konwertowanie i usuwanie znaków

## Przegląd
Polecenie `tr` w C Shell (csh) służy do translacji, usuwania lub zastępowania znaków w strumieniu tekstowym. Jest to przydatne narzędzie do manipulacji tekstem, które pozwala na łatwe modyfikowanie danych wejściowych.

## Użycie
Podstawowa składnia polecenia `tr` wygląda następująco:

```bash
tr [opcje] [argumenty]
```

## Często używane opcje
- `-d`: Usuwa wskazane znaki z wejścia.
- `-s`: Zmniejsza powtarzające się znaki do jednego wystąpienia.
- `-c`: Używa do translacji znaków, które nie są w podanym zestawie.

## Przykłady
Oto kilka praktycznych przykładów użycia polecenia `tr`:

1. **Zamiana małych liter na wielkie:**
   ```bash
   echo "hello world" | tr 'a-z' 'A-Z'
   ```
   Wynik: `HELLO WORLD`

2. **Usuwanie cyfr z tekstu:**
   ```bash
   echo "abc123def456" | tr -d '0-9'
   ```
   Wynik: `abcdef`

3. **Zmniejszanie powtarzających się spacji:**
   ```bash
   echo "This    is    a    test." | tr -s ' '
   ```
   Wynik: `This is a test.`

4. **Zamiana znaków nowej linii na spacje:**
   ```bash
   echo -e "Line1\nLine2\nLine3" | tr '\n' ' '
   ```
   Wynik: `Line1 Line2 Line3 `

## Wskazówki
- Używaj opcji `-s`, aby uprościć tekst i usunąć nadmiarowe znaki.
- Zawsze testuj polecenie na małych próbkach danych, aby upewnić się, że działa zgodnie z oczekiwaniami.
- Pamiętaj, że `tr` działa tylko na standardowym wejściu, więc często jest używane w połączeniu z innymi poleceniami, takimi jak `echo` czy `cat`.