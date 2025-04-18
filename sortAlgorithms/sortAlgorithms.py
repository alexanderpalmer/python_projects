def insertion_sort(liste):
    # Wir gehen davon aus, dass das erste Element (Index 0) bereits "sortiert" ist.
    # Daher starten wir mit dem zweiten Element (Index 1).
    for i in range(1, len(liste)):
        aktuelles_element = liste[i]  # Das Element, das in den sortierten Bereich eingefügt werden soll
        j = i - 1  # Index des letzten Elements im aktuell sortierten Bereich

        # Solange wir im Bereich der Liste bleiben (j >= 0) und das Element an Stelle j
        # größer ist als das aktuelle Element, verschieben wir es eine Position nach rechts.
        while j >= 0 and liste[j] > aktuelles_element:
            liste[j + 1] = liste[j]  # Das größere Element wird nach rechts geschoben
            j -= 1  # Wir gehen ein Element weiter nach links

        # Jetzt haben wir die richtige Position für das aktuelle Element gefunden (j + 1)
        # und fügen es dort ein.
        liste[j + 1] = aktuelles_element  # Einfügen des aktuellen Elements an der richtigen Stelle

    # Hinweis: Die Funktion verändert die ursprüngliche Liste direkt (in-place).
    
def bubbleSort(liste):
    swapped = True
    while swapped:
        swapped=False
        for x in range(len(liste)-1):
            if liste[x]>liste[x+1]:
                temp=liste[x]
                liste[x]=liste[x+1]
                liste[x+1]=temp
                swapped=True