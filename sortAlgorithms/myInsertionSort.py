list = [5,3,1,4,2]

for i in range(1,len(list)):
    aktuelles_element = list[i]
    j = i-1
    
    while j>=0 and list[j]>aktuelles_element:
        list[j+1] = list[j]
        j -= 1
        
    list[j+1]=aktuelles_element

print(list)