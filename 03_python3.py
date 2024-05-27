
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


### SEQUENZE IN PYTHON ###

# è UNA STRUTTURA DATI
# la stringa è una sequenza 
# array == vettore --> in python non esiste, ma esistono le liste
# liste--> insieme ordinata di elementi che possono anche essere diversi tra di loro. 


lista_spesa = [1,2,3]
print(lista_spesa)
print(lista_spesa[1])
print(lista_spesa[-1])
print(lista_spesa[1:])
lista_spesa[1] ="due"
print(lista_spesa[1])# aggiungere o modificare un elemento 
l1 = lista_spesa*2
print(l1)
print(type(lista_spesa[0]))
for prodott in lista_spesa:
    print(prodott)

lista_spesa2 = lista_spesa
print(lista_spesa)
lista_spesa[0] = "latte" # la modifica coinvolgerà anche la lista_spesa2?
print(lista_spesa)
print(lista_spesa2) # risposta: SI perchè???? --> non sto creando una nuova variabile ma sto cambiando solo nome. sono la stessa cosa. sto modificando lo stesso oggetto a cui puntano entrambe le varaibili
if lista_spesa == lista_spesa2:
    print("le liste sono uguali")
else: 
    print("le liste sono differenti")

x = 1 # x punta a 1
x = lista_spesa 
print(lista_spesa)

cont = 0
for prodott in lista_spesa:
    lista_spesa2[cont] = prodott # in questo modo ho due copie della lista: ma ora posso modificarle separatamente. 
    cont += 1
print(lista_spesa2)

lista_spesa2 [2] = "biscotti"
print(lista_spesa2)
if lista_spesa == lista_spesa2: # ritesto l'uguaglianza 
    print("le liste sono uguali")
else: 
    print("le liste sono differenti")