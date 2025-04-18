import random
import time

# Definition der Funktion quicksort, die eine Liste "arr" als Parameter nimmt.
def quicksort(liste):
    # Wenn die Länge der Liste kleiner oder gleich 1 ist, ist die Liste bereits sortiert.
    if len(liste) <= 1:
        return liste
    # Wähle ein Pivot-Element aus der Mitte der Liste.
    pivot = liste[len(liste) // 2]
    # Erstelle eine Liste "left", die alle Elemente enthält, die kleiner als das Pivot sind.
    left = [x for x in liste if x < pivot]
    # Erstelle eine Liste "middle", die alle Elemente enthält, die gleich dem Pivot sind.
    middle = [x for x in liste if x == pivot]
    # Erstelle eine Liste "right", die alle Elemente enthält, die größer als das Pivot sind.
    right = [x for x in liste if x > pivot]
    # Rufe die Funktion rekursiv auf die Listen "left" und "right" auf,
    # und füge die Ergebnisse zusammen mit der Liste "middle" zusammen.
    return quicksort(left) + middle + quicksort(right)

amount = 10000 
liste = [random.randint(0,100) for _ in range(amount)] 

start = time.process_time()
quicksort(liste)
end = time.process_time()
print('Benötigte Zeit des BubbleSort für '+str(amount)+' Elemente: ' + str((end - start)) + ' Sekunden' )  