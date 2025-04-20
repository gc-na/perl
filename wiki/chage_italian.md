# [Linux] C Shell (csh) chage <Uso equivalente in italiano>: Gestire le scadenze delle password

## Overview
Il comando `chage` viene utilizzato per modificare le informazioni relative alla scadenza delle password degli utenti in un sistema Linux. Permette di impostare scadenze per la password, avvisi e periodi di inattività.

## Usage
La sintassi di base del comando `chage` è la seguente:

```bash
chage [opzioni] [argomenti]
```

## Common Options
- `-l`: Mostra le informazioni di scadenza della password per un utente specifico.
- `-M <giorni>`: Imposta il numero massimo di giorni prima che la password scada.
- `-m <giorni>`: Imposta il numero minimo di giorni prima che una password possa essere cambiata.
- `-W <giorni>`: Imposta il numero di giorni di preavviso prima della scadenza della password.
- `-I <giorni>`: Imposta il numero di giorni di inattività dopo i quali l'account viene disabilitato.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `chage`:

1. **Visualizzare le informazioni di scadenza della password per un utente:**

   ```bash
   chage -l nome_utente
   ```

2. **Impostare la scadenza della password a 90 giorni:**

   ```bash
   chage -M 90 nome_utente
   ```

3. **Impostare un periodo minimo di 7 giorni prima che la password possa essere cambiata:**

   ```bash
   chage -m 7 nome_utente
   ```

4. **Impostare un avviso di 14 giorni prima della scadenza della password:**

   ```bash
   chage -W 14 nome_utente
   ```

5. **Impostare un periodo di inattività di 30 giorni prima che l'account venga disabilitato:**

   ```bash
   chage -I 30 nome_utente
   ```

## Tips
- Assicurati di avere i privilegi necessari per modificare le impostazioni degli utenti.
- Controlla regolarmente le scadenze delle password per garantire la sicurezza del sistema.
- Utilizza l'opzione `-l` per verificare le impostazioni correnti prima di apportare modifiche.