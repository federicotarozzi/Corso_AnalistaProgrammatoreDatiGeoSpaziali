
### ULTIMA STRUTTURA DATI -- LE TUPLE ###
# elementi non modificabili una volta definiti. 
my_tuple = ("Mario", "rossi", "051_6611067")
print(type(my_tuple))

#my_tuple[1] = "Rossi" # mi da errore non posso sovrascrivere un elemento.

my_tuple = (1,2,3) # se la riinizializzo posso modificarla per intero
print(my_tuple)

my_tuple = ("Mario", "rossi", "051_6611067")
# posso anche inserire elementi disomogenei (interi, sting, list ecc...)

# oggetto reiterabile 
# uso le tuple quano volgio processare una lista di valori ma mi serve che la rigidità di non poterla modificare

for i in my_tuple:
    print(i)

print(len(my_tuple)) #  numemro di elementi all'intenro della tuple = 3
print(my_tuple.count("Mario")) # numero di occorrenze dell'elemento

print("l' elemento {} compare {} volte".format(my_tuple[0], my_tuple.count(my_tuple[0])))



### FUNZIONI ###
# riutilizzare lo stesso pezzo di codice più volte
# richiamo una funzione che prende delle robe me le elabora e me le restituisce. 

'''
def nome_funzione(<parametri>):  def: definisco -- do un nome alla funzione -- (inseriesco tra parentesi i parametri)
    <istruzioni>  # definisco il corpo della funzione
    return  # dico quello che ritorna

'''
# funzione che esegue una lista di istruzioni, in questo caso non ritorna niente
def saluta():
    print("ciao!")

saluta()


# molto cosigliato inserrie una testo che spiega cosa fa la mia funzione 

def saluta(nome):
    # funzione saluta stampa ciao con il nome inserto dall'utente. 
    print("Ciao", nome)

#input_utente = input("inserisic un nome: ")
#saluta(input_utente)


def saluta(nome):
    stringa_return = "Ciao " + nome # creo una variabile da ritornare
    return stringa_return # ritorno la variabile 

print(saluta("Mario"))



def somma(a, b):
    return a + b

numero1 = 10
numero2 = 3

risultato = somma(numero1, numero2)
print(risultato)

