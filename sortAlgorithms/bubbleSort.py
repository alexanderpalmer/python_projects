import random 
import time

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
                    
    
amount = 10000 
liste = [random.randint(0,100) for _ in range(amount)] 

start = time.process_time()
bubbleSort(liste)
end = time.process_time()
print('Benötigte Zeit des BubbleSort für '+str(amount)+' Elemente: ' + str((end - start)) + ' Sekunden' )                