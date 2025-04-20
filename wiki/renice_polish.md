# [Linux] C Shell (csh) renice: Zmiana priorytetu procesów

## Overview
Polecenie `renice` w systemie C Shell (csh) służy do zmiany priorytetu już działających procesów. Umożliwia to użytkownikom dostosowanie, które procesy powinny mieć pierwszeństwo w przydzielaniu zasobów systemowych, co może być przydatne w zarządzaniu wydajnością systemu.

## Usage
Podstawowa składnia polecenia `renice` jest następująca:

```csh
renice [opcje] [argumenty]
```

## Common Options
- `-n <wartość>`: Ustala nowy priorytet dla procesów. Wartość może być dodatnia (zmniejsza priorytet) lub ujemna (zwiększa priorytet).
- `-p <PID>`: Określa identyfikator procesu (PID), dla którego ma być zmieniony priorytet.
- `-g <PGID>`: Określa identyfikator grupy procesów, dla której ma być zmieniony priorytet.

## Common Examples
1. Zmiana priorytetu pojedynczego procesu:
   ```csh
   renice -n 10 -p 1234
   ```
   W tym przykładzie priorytet procesu o PID 1234 zostanie zmniejszony.

2. Zmiana priorytetu grupy procesów:
   ```csh
   renice -n -5 -g 5678
   ```
   Tutaj priorytet wszystkich procesów w grupie o PGID 5678 zostanie zwiększony.

3. Zmiana priorytetu wielu procesów jednocześnie:
   ```csh
   renice -n 15 -p 1234 -p 5678
   ```
   W tym przypadku priorytet procesów o PID 1234 i 5678 zostanie zmniejszony.

## Tips
- Zawsze sprawdzaj aktualny priorytet procesów przed ich zmianą, aby uniknąć niezamierzonych skutków.
- Używaj wartości ujemnych ostrożnie, ponieważ mogą one spowodować, że procesy będą dominować w przydzielaniu zasobów systemowych.
- Możesz użyć polecenia `ps` do monitorowania procesów i ich priorytetów przed i po użyciu `renice`.