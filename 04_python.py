# scrivi un programma che genera una lista l3 che contenga nella posizione i.esima la somma degli i.esimi elementi di l1 e l2 
# l1 e l2 sono di uguale lunghezza variabile e valori varaibili 

l1 = [10, 20, 30, 20]
l2 = [3, 2, 1, 1]
l3 = []
i = 0
while i < len(l1):
    l3.append(l1[i] + l2[i])
    i += 1

print(l3)




