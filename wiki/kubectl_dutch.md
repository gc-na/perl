# [Linux] C Shell (csh) kubectl gebruik: Beheer Kubernetes-clusters

## Overzicht
De `kubectl`-opdracht is een commandoregeltool die wordt gebruikt om met Kubernetes-clusters te communiceren. Het stelt gebruikers in staat om verschillende taken uit te voeren, zoals het beheren van applicaties, het bekijken van clusterstatussen en het uitvoeren van configuraties.

## Gebruik
De basis syntaxis van de `kubectl`-opdracht is als volgt:

```csh
kubectl [opties] [argumenten]
```

## Veelvoorkomende opties
- `get`: Haal informatie op over Kubernetes-objecten.
- `apply`: Pas configuraties toe op de objecten in het cluster.
- `delete`: Verwijder objecten uit het cluster.
- `describe`: Geef gedetailleerde informatie over een specifiek object.
- `logs`: Bekijk de logs van een specifieke pod.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `kubectl`:

1. **Lijst alle pods in de huidige namespace:**
   ```csh
   kubectl get pods
   ```

2. **Toepassen van een configuratiebestand:**
   ```csh
   kubectl apply -f configuratie.yaml
   ```

3. **Verwijder een specifieke pod:**
   ```csh
   kubectl delete pod naam-van-pod
   ```

4. **Bekijk de logs van een pod:**
   ```csh
   kubectl logs naam-van-pod
   ```

5. **Geef gedetailleerde informatie over een service:**
   ```csh
   kubectl describe service naam-van-service
   ```

## Tips
- Gebruik de `--namespace` optie om te werken in een specifieke namespace.
- Combineer `kubectl` met `grep` om snel informatie te filteren.
- Maak gebruik van `kubectl get all` om een overzicht van alle objecten in de huidige namespace te krijgen.
- Zorg ervoor dat je altijd de laatste versie van `kubectl` gebruikt voor de beste compatibiliteit met je cluster.