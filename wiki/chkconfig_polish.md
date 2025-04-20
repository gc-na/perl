# [Linux] C Shell (csh) chkconfig użycie: Zarządzanie usługami systemowymi

## Przegląd
Polecenie `chkconfig` służy do zarządzania usługami systemowymi w systemach opartych na Linuxie. Umożliwia włączanie, wyłączanie oraz sprawdzanie statusu usług, które są uruchamiane podczas startu systemu.

## Użycie
Podstawowa składnia polecenia `chkconfig` jest następująca:

```bash
chkconfig [opcje] [argumenty]
```

## Częste opcje
- `--list` - wyświetla listę wszystkich usług oraz ich status (włączone/wyłączone).
- `--add <usługa>` - dodaje nową usługę do zarządzania przez chkconfig.
- `--del <usługa>` - usuwa usługę z zarządzania przez chkconfig.
- `--level <poziom>` - ustawia poziom uruchamiania dla określonej usługi.

## Przykłady
1. Aby wyświetlić status wszystkich usług:
   ```bash
   chkconfig --list
   ```

2. Aby dodać nową usługę:
   ```bash
   chkconfig --add myservice
   ```

3. Aby usunąć usługę:
   ```bash
   chkconfig --del myservice
   ```

4. Aby włączyć usługę na poziomie uruchamiania 3:
   ```bash
   chkconfig myservice on --level 3
   ```

5. Aby wyłączyć usługę na poziomie uruchamiania 5:
   ```bash
   chkconfig myservice off --level 5
   ```

## Wskazówki
- Zawsze sprawdzaj status usług po ich dodaniu lub usunięciu, aby upewnić się, że zmiany zostały zastosowane.
- Używaj opcji `--level`, aby precyzyjnie kontrolować, na jakich poziomach uruchamiania usługi mają być włączone lub wyłączone.
- Pamiętaj, że zmiany wprowadzone przez `chkconfig` mogą wymagać ponownego uruchomienia systemu, aby zaczęły obowiązywać.