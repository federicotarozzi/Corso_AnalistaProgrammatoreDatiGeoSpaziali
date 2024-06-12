
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


print(function1(1,2,3,4,5,6)) #passati 6 argomenti alla funzione
print(function1()) # nessun argomento passato alla funzione



# LAMBDA FUNCIONS #
def somma (a, b):
    risultato = a + b
    return risultato

print(somma(3, 4)) # RITORNO IL PARAMETRO QUINDI DEVO METTERE LA VIRGOLA E NON IL SEGNO  DELL'OPERATORE. 

lsomma = lambda a,b : a+b  # è uguale a usare la formula di definizione di funzione con def usata qui sopra ma è scritto con lambda ma in forma più contratta
print(lsomma(4,8))


# le funzioni vengono raccorte all'interno di MODULI (file che contengono codice pronto all'uso)
# importo il modulo e uso le funzioni in esse contentuto
# math --> importo un modulo interno a python con le funzioni matematiche 

import math 
print (max([36,4,2])) # è una funzione definita all'interno del modulo math
print (min([12,3,4,56,7,1]))
print(math.sqrt(2))


#altra libreria random
import random as r
print(r.random())

def random100():
    #ritorna un numero casuale tra 0 e 100
    return int(r.random()*100)
"""
    x = r.random()
    numero_causale = int(0<= x <= 100)
    return numero_causale 
"""

nuemro_casuale = random100()
print("numero casuale generato: ", nuemro_casuale)


print(r.randrange(0,100,1))



# DEFINIRE SOTTOFUNZIONI # 
# funzioni definite all'interno di una funzione

def function1():
    def function2():
        print("Sottofunzione funcion2()")
    def function3():
        print("Sottofunzione funcion3()")
    print("funzione function1")
    function2()
    function3()

print(function1())



# ULTIMA COSA SULLE FUNZIONI #

# una funzione può riportare più di un risultato 

from math import sqrt

def somma_sqrt(a,b):
    risultato = a + b
    return risultato, sqrt(risultato)

print(somma_sqrt(10,6))

somma, radice_quadr = somma_sqrt(10,6)
print("La somma vale:{} \nla radice quadrata di vale:{}".format(somma,radice_quadr))


def padre(n):
    def figlio1():
        print("Ciao sono Mario")
    def figlio2():
        print("Ciao sono Lucia")
    def nofiglio():
        print("Nessun figlio")

    if n==1:
        return figlio1
    elif n==2:
        return figlio2
    else:
        return nofiglio

albero = padre(2)
print(albero()) # la stampa di albero mi spampa la funzione padre al parametro definito dalla funzioen figlio2 --> quindi in questo caso la stampa è essa stessa una funzione
print(padre(2)())
    