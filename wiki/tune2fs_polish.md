# [Linux] C Shell (csh) tune2fs użycie: Narzędzie do modyfikacji systemu plików ext2/ext3/ext4

## Przegląd
Polecenie `tune2fs` jest używane do modyfikacji parametrów systemu plików ext2, ext3 i ext4. Umożliwia użytkownikom dostosowanie różnych opcji systemu plików, takich jak zmiana rozmiaru bloków, ustawienia dziennika oraz inne parametry, które mogą wpływać na wydajność i zachowanie systemu plików.

## Użycie
Podstawowa składnia polecenia `tune2fs` jest następująca:

```bash
tune2fs [opcje] [argumenty]
```

## Częste opcje
- `-c <liczba>`: Ustawia maksymalną liczbę montowań przed wymuszeniem sprawdzenia systemu plików.
- `-i <czas>`: Ustawia interwał czasowy między sprawdzeniami systemu plików.
- `-m <procent>`: Ustawia procent miejsca na dysku, który ma być zarezerwowany dla użytkownika root.
- `-O <opcje>`: Włącza określone opcje systemu plików.
- `-L <etykieta>`: Ustawia etykietę systemu plików.

## Przykłady
Oto kilka praktycznych przykładów użycia polecenia `tune2fs`:

1. Ustawienie maksymalnej liczby montowań przed sprawdzeniem systemu plików:

   ```bash
   tune2fs -c 30 /dev/sda1
   ```

2. Ustawienie interwału czasowego na 6 miesięcy między sprawdzeniami:

   ```bash
   tune2fs -i 6m /dev/sda1
   ```

3. Zarezerwowanie 5% miejsca na dysku dla użytkownika root:

   ```bash
   tune2fs -m 5 /dev/sda1
   ```

4. Włączenie opcji "dir_index":

   ```bash
   tune2fs -O dir_index /dev/sda1
   ```

5. Ustawienie etykiety systemu plików na "MojeDane":

   ```bash
   tune2fs -L MojeDane /dev/sda1
   ```

## Wskazówki
- Zawsze wykonuj kopię zapasową danych przed wprowadzeniem zmian w systemie plików.
- Używaj polecenia `tune2fs` z ostrożnością, aby uniknąć usunięcia lub uszkodzenia danych.
- Regularnie sprawdzaj stan swojego systemu plików za pomocą polecenia `fsck`, aby zapewnić jego integralność.