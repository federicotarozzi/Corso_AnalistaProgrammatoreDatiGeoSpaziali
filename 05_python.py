
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

print("La somma di {} + {} è uguale a {}".format(numero1,numero2,risultato))





def somma(a,b=1,*argument): # di base posso mettere sta cosa del valore di defult di b=1 # *argument --> n valori possibili
    if len(argument) == 0:
        return(a+b)
    else:
        res = a+b
        for i in argument:
            res += i
        return res
    


# altra possoibilità
# funzione che accetta un certo tipo di parametri
# mi generra una stringa con le informazioni relative a un ipotetico prodotto

def stampaInfo(nome, prezzo, **kwargs): # **kwrgs passo una serei di parametri attraverso una notazione chiavi valori grazie ai due asterischi ** uso robe di dizionari 
    stringainfo = "Nome prodotto: " + nome + "Prezzo: " + prezzo
    for k,v in kwargs.items(): # itero su un dizionario
        print(k,":", v) 
    return stringainfo

s = stampaInfo("xbox", "100", peso = "1.4", anno = "2015") # due parametri + altri elementi come coppie chiave valore. 
print(s)
    



# *prova --> per n valori pero singoli
# **prova --> per n valori in formato CHIAVE-VALORE quindi sempre a coppie (dizionario)


# caso generale

def function1(*args):
    if(len(args) == 0):
        print("nessun argomento passato alla funzione")
    else:
        print("passati {} argomenti alla funzione".format(len(args)))


print(function1(1,2,3,4,5,6))
print(function1())





