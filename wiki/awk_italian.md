# [Linux] C Shell (csh) awk Uso: Elaborazione di testo e reportistica

## Overview
Il comando `awk` è un potente linguaggio di programmazione per l'elaborazione di testi e la generazione di report. Viene utilizzato principalmente per analizzare e manipolare file di testo, specialmente quelli strutturati in righe e colonne, come i file CSV.

## Usage
La sintassi di base del comando `awk` è la seguente:

```bash
awk [opzioni] [argomenti]
```

## Common Options
- `-F`: Specifica il delimitatore di campo. Ad esempio, `-F,` per i file CSV.
- `-v var=value`: Imposta una variabile `var` con il valore `value`.
- `-f file`: Legge il programma `awk` da un file invece di dalla riga di comando.

## Common Examples

### Esempio 1: Stampa la prima colonna di un file
```bash
awk '{print $1}' file.txt
```
Questo comando stampa la prima colonna di ogni riga nel file `file.txt`.

### Esempio 2: Utilizzo di un delimitatore personalizzato
```bash
awk -F, '{print $2}' file.csv
```
In questo caso, `awk` utilizza la virgola come delimitatore e stampa la seconda colonna del file CSV.

### Esempio 3: Filtrare righe in base a una condizione
```bash
awk '$3 > 50 {print $1, $2}' file.txt
```
Questo comando stampa la prima e la seconda colonna delle righe in cui il valore della terza colonna è maggiore di 50.

### Esempio 4: Somma di una colonna
```bash
awk '{sum += $1} END {print sum}' file.txt
```
Qui, `awk` calcola e stampa la somma di tutti i valori nella prima colonna del file `file.txt`.

## Tips
- Utilizza `-F` per specificare il delimitatore corretto quando lavori con file non standard.
- Sfrutta le variabili per rendere i tuoi script `awk` più leggibili e facili da mantenere.
- Ricorda di utilizzare le espressioni regolari per filtrare righe più complesse.