def merge_sort(liste):
    if len(liste) <=1:
        return liste
    
    # Liste in zwei Hälften teilen, mit Ganzzahl Divisions-Operator
    mitte = len(liste) // 2
    linke_haelfte = liste[:mitte]
    rechte_haelfte = liste[mitte:]
    
    sortiert_links = merge_sort(linke_haelfte)
    sortiert_rechts = merge_sort(rechte_haelfte)
    
    return merge(sortiert_links, sortiert_rechts)

def merge(liste1, liste2):
    ergebnis = []
    i = 0 # Zeiger für liste1
    j = 0 # Zeiger für liste2
    
    # Solange beide Liste noch nicht vollständig durchlaufen sind
    while i<len(liste1) and j<len(liste2):
        if liste1[i] <= liste2[j]:
            ergebnis.append(liste1[i])
            i += 1
        else:
            ergebnis.append(liste2[j])
            j += 1
    
    # Restliche Elemente anhängen (nur eine der Listen hat hier noch Elemente)        
    ergebnis.extend(liste1[i:])
    ergebnis.extend(liste2[j:])
    
    return ergebnis

unsortierte_liste = [5, 3, 8, 4, 2, 7, 1, 6]
sortierte_liste = merge_sort(unsortierte_liste)
print(sortierte_liste)