
### RIASSUNTAZZO ###

# due strutture: 1) controlli condizionali 2) cicli while e for
# break --> blocca il ciclo. 
# continue --> a una certa condizione salta e va avanti


### CICLI ANNIDATI ###
# i cicli annidati possono servire per esempio, per costruire delle matrici
# tabelline del 10 - frutto il valore del contatore 
for i in range(1,11): # mi definisce il moltiplicando 
    for j in range (1,11):  # mi definsice il moltiplicatore 
        print(i * j, end=" ") # vado a stampare il prodotto di i * j, stampa il carattere di new line con l'istruzione end. 
    print() # per averle in colonna
