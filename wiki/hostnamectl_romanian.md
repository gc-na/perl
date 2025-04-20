# [Linux] C Shell (csh) hostnamectl utilizare: Afișează și modifică informațiile despre gazdă

## Overview
Comanda `hostnamectl` este utilizată pentru a afișa și a modifica informațiile despre gazda sistemului, cum ar fi numele gazdei, tipul de sistem și alte detalii relevante. Aceasta este o unealtă utilă pentru administrarea sistemului, oferind o interfață simplă pentru gestionarea configurației gazdelor.

## Usage
Sintaxa de bază a comenzii `hostnamectl` este următoarea:

```csh
hostnamectl [options] [arguments]
```

## Common Options
- `set-hostname`: Schimbă numele gazdei.
- `status`: Afișează informații detaliate despre gazdă.
- `set-icon-name`: Setează numele pictogramei asociate cu gazda.
- `set-chassis`: Specifică tipul de carcasă (ex: desktop, laptop).
- `help`: Afișează ajutorul pentru utilizarea comenzii.

## Common Examples
### Afișarea informațiilor despre gazdă
Pentru a vizualiza informațiile curente despre gazdă, folosiți:

```csh
hostnamectl status
```

### Schimbarea numelui gazdei
Pentru a schimba numele gazdei la „noul-nume”, utilizați:

```csh
hostnamectl set-hostname noul-nume
```

### Setarea tipului de carcasă
Dacă doriți să specificați tipul de carcasă ca „laptop”, rulați:

```csh
hostnamectl set-chassis laptop
```

### Afișarea ajutorului
Pentru a obține informații despre opțiunile disponibile, folosiți:

```csh
hostnamectl help
```

## Tips
- Asigurați-vă că aveți permisiuni de administrator pentru a modifica numele gazdei.
- Verificați întotdeauna informațiile curente înainte de a face modificări, pentru a evita confuziile.
- Folosiți `hostnamectl status` după modificări pentru a confirma că schimbările au fost aplicate corect.