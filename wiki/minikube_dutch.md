# [Nederlandse] C Shell (csh) minikube gebruik: Beheer lokale Kubernetes-clusters

## Overzicht
De `minikube`-opdracht is een hulpmiddel waarmee je een lokale Kubernetes-cluster kunt opzetten en beheren. Het is een handige manier om Kubernetes te leren en te experimenteren zonder een volledige cloudomgeving te hoeven gebruiken.

## Gebruik
De basis syntaxis van de `minikube`-opdracht is als volgt:

```
minikube [opties] [argumenten]
```

## Veelvoorkomende opties
- `start`: Start een nieuwe Minikube-cluster.
- `stop`: Stop de huidige Minikube-cluster.
- `delete`: Verwijder de huidige Minikube-cluster.
- `status`: Toon de status van de Minikube-cluster.
- `dashboard`: Start het Kubernetes-dashboard in de browser.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `minikube`-opdracht:

### Start een nieuwe Minikube-cluster
```csh
minikube start
```

### Stop de huidige Minikube-cluster
```csh
minikube stop
```

### Verwijder de huidige Minikube-cluster
```csh
minikube delete
```

### Controleer de status van de cluster
```csh
minikube status
```

### Open het Kubernetes-dashboard
```csh
minikube dashboard
```

## Tips
- Zorg ervoor dat je voldoende systeembronnen hebt voordat je Minikube start, zoals RAM en CPU.
- Gebruik de `--driver` optie om de gewenste virtualisatie-driver te specificeren, zoals `virtualbox` of `docker`.
- Vergeet niet om regelmatig je cluster op te schonen met `minikube delete` om ongebruikte resources te verwijderen.