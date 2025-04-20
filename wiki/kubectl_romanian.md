# [Linux] C Shell (csh) kubectl utilizare: Comandă pentru gestionarea clusterelor Kubernetes

## Overview
Comanda `kubectl` este un instrument esențial pentru interacțiunea cu clusterele Kubernetes. Aceasta permite utilizatorilor să efectueze diverse operațiuni, cum ar fi gestionarea aplicațiilor, inspectarea resurselor și efectuarea modificărilor în configurațiile clusterului.

## Usage
Sintaxa de bază a comenzii `kubectl` este următoarea:

```
kubectl [opțiuni] [argumente]
```

## Common Options
- `get`: Afișează informații despre resursele din cluster.
- `describe`: Oferă detalii despre o resursă specifică.
- `apply`: Aplică modificări la resursele din cluster pe baza unui fișier de configurare.
- `delete`: Șterge resursele specificate din cluster.
- `logs`: Afișează jurnalele unui pod specific.

## Common Examples
1. **Afișarea tuturor podurilor dintr-un namespace:**
   ```bash
   kubectl get pods -n nume-namespace
   ```

2. **Descrierea unui pod specific:**
   ```bash
   kubectl describe pod nume-pod -n nume-namespace
   ```

3. **Aplicarea unui fișier de configurare:**
   ```bash
   kubectl apply -f cale/catre/fișier.yaml
   ```

4. **Ștergerea unui serviciu:**
   ```bash
   kubectl delete service nume-serviciu -n nume-namespace
   ```

5. **Vizualizarea jurnalele unui pod:**
   ```bash
   kubectl logs nume-pod -n nume-namespace
   ```

## Tips
- Folosește opțiunea `-o wide` cu comanda `get` pentru a obține informații suplimentare despre resurse.
- Verifică întotdeauna starea resurselor după aplicarea modificărilor pentru a te asigura că totul funcționează corect.
- Utilizează aliasuri pentru comenzi frecvent utilizate pentru a economisi timp.