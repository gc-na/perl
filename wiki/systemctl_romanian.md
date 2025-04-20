# [Linux] C Shell (csh) systemctl utilizare: Gestionarea serviciilor de sistem

## Overview
Comanda `systemctl` este utilizată pentru a gestiona sistemele de servicii în Linux, permițând utilizatorilor să pornească, să oprească, să repornească sau să verifice starea serviciilor de sistem.

## Usage
Sintaxa de bază a comenzii `systemctl` este următoarea:

```csh
systemctl [opțiuni] [argumente]
```

## Common Options
- `start`: Pornește un serviciu.
- `stop`: Oprește un serviciu.
- `restart`: Reporneste un serviciu.
- `status`: Afișează starea unui serviciu.
- `enable`: Activează un serviciu pentru a porni automat la boot.
- `disable`: Dezactivează un serviciu pentru a nu porni automat la boot.

## Common Examples
1. **Pornirea unui serviciu:**
   ```csh
   systemctl start nume_serviciu
   ```

2. **Oprirea unui serviciu:**
   ```csh
   systemctl stop nume_serviciu
   ```

3. **Repornirea unui serviciu:**
   ```csh
   systemctl restart nume_serviciu
   ```

4. **Verificarea stării unui serviciu:**
   ```csh
   systemctl status nume_serviciu
   ```

5. **Activarea unui serviciu la boot:**
   ```csh
   systemctl enable nume_serviciu
   ```

6. **Dezactivarea unui serviciu la boot:**
   ```csh
   systemctl disable nume_serviciu
   ```

## Tips
- Asigurați-vă că aveți permisiuni de administrator (root) pentru a gestiona serviciile.
- Utilizați `systemctl list-units --type=service` pentru a vizualiza toate serviciile active și inactive.
- Verificați jurnalele de sistem cu `journalctl` pentru a obține informații suplimentare despre serviciile gestionate.