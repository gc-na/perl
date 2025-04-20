# [Linux] C Shell (csh) fc <Użycie: edytowanie i ponowne wykonywanie poleceń>

## Przegląd
Polecenie `fc` w C Shell (csh) służy do edytowania i ponownego wykonywania wcześniejszych poleceń z historii. Umożliwia użytkownikom przeglądanie, modyfikowanie i uruchamianie poleceń, co ułatwia pracę w terminalu.

## Użycie
Podstawowa składnia polecenia `fc` jest następująca:

```csh
fc [opcje] [argumenty]
```

## Częste opcje
- `-l` - Wyświetla listę poleceń z historii.
- `-n` - Nie wyświetla numerów poleceń w liście.
- `-r` - Odwraca kolejność poleceń w historii.
- `-s` - Wykonuje polecenie bez edytowania.

## Częste przykłady

### Wyświetlenie ostatnich poleceń
Aby wyświetlić ostatnie polecenia z historii, użyj:

```csh
fc -l
```

### Edytowanie konkretnego polecenia
Aby edytować konkretne polecenie z historii, użyj:

```csh
fc 10
```
gdzie `10` to numer polecenia w historii.

### Wykonanie polecenia bez edytowania
Aby wykonać ostatnie polecenie bez edytowania, użyj:

```csh
fc -s
```

### Odwrócenie kolejności poleceń
Aby wyświetlić polecenia w odwrotnej kolejności, użyj:

```csh
fc -r -l
```

## Wskazówki
- Regularnie przeglądaj historię poleceń, aby szybko odnaleźć i ponownie wykonać często używane komendy.
- Używaj opcji `-n`, aby uprościć wyświetlanie poleceń, gdy nie potrzebujesz numerów.
- Pamiętaj, że edytowanie poleceń za pomocą `fc` otworzy je w domyślnym edytorze tekstu, co może być przydatne do wprowadzania bardziej złożonych zmian.