
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
# la lista non ha un numero definito di elementi e non è vincolato a un tipo 
# tipo lista in python segue le dinamiche dell'array però in forma DINAMICA sia nel tipo che nella dimensione. 
# tipo list
lista_spesa = [1,2,3]
print(lista_spesa)
# Accedere alla lista in modo posizionale
print(lista_spesa[1])
print(lista_spesa[-1]) # indice negativo va da destra verso sinistra
print(lista_spesa[1:]) # vale lo slice partendo dalla posizione x:y
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




 
lista_spesa2 [2] = "biscotti"
print(lista_spesa2)
if lista_spesa == lista_spesa2: # ritesto l'uguaglianza 
    print("le liste sono uguali")
else: 
    print("le liste sono differenti")


################ questa parte che segue cerca di dimostrare un qualcosa che non serve dimostrare #############################
cont = 0
for prodotto in lista_spesa:
    lista_spesa2[cont] = prodotto # in questo modo ho due copie della lista: ma ora posso modificarle separatamente. 
    cont += 1
print(lista_spesa2)

lista_spesa3 = list("mele") # la lista della spesa 3 è una lista che ha come elementi una sringa, scomposta dai suoi elementi. ogni elemento contiene un carattere 
print(lista_spesa3)

# in questo momento definisco due liste uguali 
s1 = [100,200,300]
s2 = [100,200,300]
#s1 = s2  
# se mantenessi questo assegnamento allora le lego per sempre queste due liste insime


# modifico un elemento in s1
s1[2] = 310 #  accedo al terzo elemento e lo modifico. questa modifica è riguarda sia s1 che s2 periche entrambi gli oggetti puntano alla stessa lista quindi la varaizione di una corrisponde anche alla variazione dell'altro
print('s1 = {}'.format(s1))
# print('s2 = {}'.format(s2))
print(s1)
print(s2)

# VOLGIO FARE UNA COPIA IN MODO DA DIVIDERE LE DUE LISTE S1 E S2
contatore = 0
for numero in s1:
    s2[contatore] = numero*2 # faccio in modo che il contatore sia uguale agli elementi della lista
    contatore += 1 # incremento il contatore prima di reiniziare il ciclo

s1 [2] = 10
print(s1)
print(s2) # ora sono separate...


# funzione .format quando e come usarlo

x = 9.476452874
print('x={:.2f}'.format(x)) # per la formattazione in modo da avere 2 numeri dopo la virgola 
print('x={:.4f}'.format(x)) # questo per avere 4 numeri dopo la virgola 





# METODI PER MANIPOLARE DELLE LISTE

abc = [1,2,3,4,5]
abc.insert(2, "albero") # scelgo la posizione e metto tra virgolette quello che voglio inserire 
print(abc)
abc.append(6) # aggiunge alla fine un elemento 
print(abc)
abc.remove("albero") # rimuove la prima occorrenza del valore espresso tra parentesi.
print(abc)
abc.pop(5) # toglie l'elemento indicato nella posizione tra parentezi, 
# se messo .pop() toglie l'elemento finale 
print(abc)

# conosco l'elemento ma non conosco dove si rova all'interno della lista (posizione non nota)
index = abc.index(2)
print(index) # dice che è alla posizione 1


# conosco la posizione ma non conosco l'elemento 
posizione = abc[1]
print(posizione ) #l'elemento è "2"

abc.reverse() # inverte l'ordine della lista
print(abc)


abc.append(2) # ho aggiunto un 2 alla fine  # LA lista ammette elementi duplicati 
print(abc.count(2)) # numero di occorrenze di un deteminato elemento all'interno della lista 

abc = [2,5,6,9,6,5,3,0]
abc.sort() # organizza tutti gli elementi in ordine crescente NB: GLI ELEMENTI DELLA LISTA IN QUESTO CASO DEVONO ESSERE TUTTI DELLO STESSO TIPO  
print(abc)

print(sorted(abc, reverse=True)) # ALTRO MODO PER SCRIVERE 


# lista che non contiene elementi ripetuti. USO IL SET--> struttura dati che non comprende elementi ripetuti. 

abc = [1,2,3,3,3,4,5,6,6,6,7,7,8,9]
abc = set(abc) # converto la mia lista in un set
print("abc = ", abc)

# utilizzando le parentesi graffe {} creo direttamente un SET
abb = {11,2,2,4,5,6,6,7,8,9,0} # creo direttamente un set e mi elimina le ripetizioni
print("abb = ", abb)

# set per operazioni di tipo insiemistiche 

### OPERAZIONE DI UNIONE ###
acc = abc | abb # | è il simbolo di UNIONE 
print (acc) # unione degli elementi delle due liste senza duplicati. 

### OPERAZIOEN DI INTERSEZIONE ###
acc = abc & abb # & il simbolo di INTERSEZIONE --> CONTENUTI SIA IN UNA LISTA CHE IN UN ALTRA 
print (acc)

### OPERAZIONE DI DIFFERENZA ###

acc = abc - abb # riporto solo gli elementi contentui in ABC 
print ("acc =", acc)

