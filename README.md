# Kalkulator for å beregne karaktersnitt / GPA ECTS credits calculator 


## Norsk
Dette python programmet kan du bruke til å beregne din snittkarakter, karaktersnitt med desimal samt se antall studiepoeng
Kalkulatoren baserer seg på NTNU og FS sitt beregningssytem: https://i.ntnu.no/wiki/-/wiki/Norsk/FS+-+Beregne+snittkarakter

NB: Programmet stemmer bra, men mindre feil kan oppstå så informasjon fra kalkultoren er på eget ansvar!

### Avhengigheter 
1) Installer Python versjon 3 eller nyere
   https://www.python.org/downloads/
2) Installer tabulate fra PyPI biblioteket
```
pip install tabulate
```
Eller på Unix/Zsh - Macbook 
```
TABULATE_INSTALL=lib-only pip install tabulate
```
Info om tabulate: https://pypi.org/project/tabulate/

### Hvordan bruke kalkulatoren
Sett inn karakterene dine i listen på toppen
```py
fag_data = [
    ('DCST1001', 7.5, 'C'),
    ('DCST1002', 7.5, ''),
    ('DCST1003', 7.5, 'C'),
    ('DCST1004', 7.5, 'C'),
]
```

For fag med karakter:
```py
('FAGXXXX', 7.5, 'A')
```

For fag uten karakter (Bestått / Ikke Bestått):
```py
('FAGXXXX', 7.5, '')
```

## English
This Python program can be used to calculate your average grade, grade point average (GPA) with decimals, and see the total number of study credits.
The calculator is based on the calculation system of NTNU and FS: https://i.ntnu.no/wiki/-/wiki/Norsk/FS+-+Beregne+snittkarakter

Note: The program is generally accurate, but minor errors may occur, so information from the calculator is at your own risk!

### Dependencies

1) Install Python version 3 or newer  
   https://www.python.org/downloads/

2) Install tabulate from the PyPI library:

```
pip install tabulate
```
Or on Unix/Zsh - Macbook 
```
TABULATE_INSTALL=lib-only pip install tabulate
```
Information about tabulate: https://pypi.org/project/tabulate/

### How to Use the Calculator

Enter your grades into the list at the top:

```py
fag_data = [
    ('DCST1001', 7.5, 'C'),
    ('DCST1002', 7.5, ''),
    ('DCST1003', 7.5, 'C'),
    ('DCST1004', 7.5, 'C'),
]
```

For courses with a letter grade:
```py
('FAGXXXX', 7.5, 'A')
```

For courses without a letter grade (Pass / Fail):
```py
('FAGXXXX', 7.5, '')
```
