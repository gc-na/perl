# [Linux] C Shell (csh) kubectl użycie: zarządzanie klastrami Kubernetes

## Overview
`kubectl` to narzędzie wiersza poleceń, które umożliwia interakcję z klastrami Kubernetes. Umożliwia użytkownikom zarządzanie aplikacjami uruchomionymi w klastrze, a także monitorowanie i rozwiązywanie problemów z zasobami.

## Usage
Podstawowa składnia polecenia `kubectl` jest następująca:

```bash
kubectl [opcje] [argumenty]
```

## Common Options
- `get`: Pobiera informacje o zasobach.
- `describe`: Wyświetla szczegółowe informacje o zasobach.
- `apply`: Zastosowuje zmiany z pliku konfiguracyjnego do zasobów.
- `delete`: Usuwa zasoby z klastra.
- `logs`: Wyświetla logi kontenera.

## Common Examples
1. **Pobieranie listy podów:**
   ```bash
   kubectl get pods
   ```

2. **Wyświetlanie szczegółów podu:**
   ```bash
   kubectl describe pod <nazwa-podu>
   ```

3. **Zastosowanie zmian z pliku YAML:**
   ```bash
   kubectl apply -f <plik.yaml>
   ```

4. **Usuwanie podu:**
   ```bash
   kubectl delete pod <nazwa-podu>
   ```

5. **Wyświetlanie logów kontenera:**
   ```bash
   kubectl logs <nazwa-podu>
   ```

## Tips
- Używaj opcji `--namespace` do zarządzania zasobami w określonym namespace.
- Regularnie aktualizuj `kubectl`, aby korzystać z najnowszych funkcji i poprawek.
- Wykorzystuj aliasy dla często używanych poleceń, aby przyspieszyć pracę.