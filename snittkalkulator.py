from tabulate import tabulate

# ----------------------------------------------------------------------------------------- #
# Legg til karakterene dine her
# Eksempel ('FAGXXXX', 7.5, 'C')
# Ved bestått/ikke bestått fag skal rubriken med fag stå tom
# Eksempel ('FAGXXXX', 7.5, '')

fag_data = [
    ('DCST1001', 7.5, 'C'),
    ('DCST1002', 7.5, ''),
    ('DCST1003', 7.5, 'C'),
    ('DCST1004', 7.5, 'C'),
    ('DCST1005', 7.5, 'B'),
    ('DCST1006', 7.5, 'C'),
    ('DCST1007', 7.5, 'D'),
    ('IDATT2002', 7.5, 'B'),
    ('DCST2001', 7.5, 'D'),
    ('DCST2002', 7.5, 'A'),
    ('IDATT2202', 7.5, 'D'),
    ('EXPH0300', 7.5, 'C'),
]











# ----------------------------------------------------------------------------------------- #
# ----------------- Selve koden ---------------------- #

def beregn_snittkarakter(fag_data):
    """
    Beregner gjennomsnittskarakter for et studieprogram basert på karakterer og studiepoeng.
    
    :param fag_data: Liste av tuples, hvor hver tuple inneholder (fagkode, studiepoeng, karakter).
                     Eksempel: [('FAG101', 7.5, 'A'), ('FAG102', 10, 'B')]
    :return: Tuple med bokstavkarakter som representerer gjennomsnittskarakteren, gjennomsnittet som desimaltall, og totalt studiepoeng inkludert fag uten karakter.
    """
    # Karakterens tallekvivalent
    karakter_tall = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}
    
    # Summering av produktene av karakterens tallekvivalent og studiepoeng
    total_poeng = 0
    total_vridd_poeng = 0
    total_studiepoeng = 0  # Totalt antall studiepoeng (inkludert fag uten karakter)
    
    for fag in fag_data:
        fagkode, studiepoeng, karakter = fag
        total_studiepoeng += studiepoeng  # Legger til studiepoeng uavhengig av karakter
        
        if karakter in karakter_tall:  # Bare fag med karakter skal brukes til beregning
            tallekvivalent = karakter_tall[karakter]
            total_vridd_poeng += tallekvivalent * studiepoeng
            total_poeng += studiepoeng
    
    # Beregning av gjennomsnittet (veid gjennomsnitt)
    if total_poeng == 0:
        return "Ingen gyldige data", 0, total_studiepoeng
    
    gjennomsnitt = total_vridd_poeng / total_poeng
    
    # Beregning av gjennomsnittskarakteren
    # Vi runder av til to desimaler
    gjennomsnitt_rundet = round(gjennomsnitt, 2)
    
    # Bestemmer bokstavkarakter basert på gjennomsnitt
    if gjennomsnitt_rundet >= 4.5:
        snittkarakter = 'A'
    elif gjennomsnitt_rundet >= 3.5:
        snittkarakter = 'B'
    elif gjennomsnitt_rundet >= 2.5:
        snittkarakter = 'C'
    elif gjennomsnitt_rundet >= 1.5:
        snittkarakter = 'D'
    else:
        snittkarakter = 'E'
    
    return snittkarakter, gjennomsnitt_rundet, total_studiepoeng



snittkarakter, gjennomsnitt, total_poeng = beregn_snittkarakter(fag_data)

# Lage en tabell med python tabulate for å vise karaktersnitt, snittkarakter og antall studiepoeng
result_table = [
    ["Snittkarakter", snittkarakter],
    ["Gjennomsnitt (desimaltall)", f"{gjennomsnitt:.2f}"],
    ["Totalt antall studiepoeng (inkludert fag med bestått/ikke bestått)", total_poeng]
]

# Printe tabellen til terminal
print(f"Hei Sebastian , Dette er ditt karaktersnitt, basert på karakterinfo")
print(tabulate(result_table, headers=["Kategori", "Verdi"], tablefmt="fancy_grid"))
