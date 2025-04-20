# [Linux] C Shell (csh) case <Użycie: dopasowanie wzorców>

## Overview
Polecenie `case` w powłoce C Shell (csh) służy do dopasowywania wzorców i wykonywania różnych poleceń w zależności od wartości zmiennej. Jest to przydatne narzędzie do tworzenia skryptów, które wymagają warunkowego wykonywania kodu.

## Usage
Podstawowa składnia polecenia `case` jest następująca:

```csh
case [zmienna] in
    [wzorzec1]) [polecenie1];;
    [wzorzec2]) [polecenie2];;
    ...
    *) [polecenie_domyslne];;
esac
```

## Common Options
Polecenie `case` nie ma wielu opcji, ale oto kilka istotnych elementów:

- `in`: Rozpoczyna blok wzorców.
- `)`: Zamyka wzorzec.
- `;;`: Kończy dany blok poleceń dla wzorca.
- `*)`: Wzorzec domyślny, który jest wykonywany, gdy żaden z wcześniejszych wzorców nie pasuje.

## Common Examples

### Przykład 1: Prosta struktura `case`
```csh
set zmienna = "jabłko"
case $zmienna in
    jabłko) echo "To jest jabłko";;
    banan) echo "To jest banan";;
    *) echo "Nieznany owoc";;
esac
```

### Przykład 2: Dopasowywanie rozszerzeń plików
```csh
set plik = "dokument.txt"
case $plik in
    *.txt) echo "To jest plik tekstowy";;
    *.jpg) echo "To jest plik obrazu";;
    *) echo "Nieznany typ pliku";;
esac
```

### Przykład 3: Wybór opcji na podstawie zmiennej
```csh
set opcja = "2"
case $opcja in
    1) echo "Wybrano opcję 1";;
    2) echo "Wybrano opcję 2";;
    3) echo "Wybrano opcję 3";;
    *) echo "Nieznana opcja";;
esac
```

## Tips
- Używaj `case` do uproszczenia skomplikowanych struktur warunkowych w skryptach.
- Zawsze pamiętaj o dodaniu wzorca domyślnego (`*`), aby obsłużyć nieoczekiwane wartości.
- Używaj wyrażeń regularnych w wzorcach, aby zwiększyć elastyczność dopasowywania.