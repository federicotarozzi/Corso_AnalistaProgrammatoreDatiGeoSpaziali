# import this funzione interna a Python che contiene le fondamenta ideologiche del linguaggio.
'''
# PROVA PRIMO CODICE PRIMO GIORNO # 
nome = "Federico"
print(nome)

print("Hello world!")

a = 1
b = 2
c = a + b 

print(c) 
'''
### COME SI SCRIVONO I COMMENTI ###

# commento su singola riga

'''
commento
su multi-riga
'''


### I TIPI ###

# variabile con valore int 5
numero_intero = 5

# come verifico il tipo di X? funz type
print(type(numero_intero))

# variabile con valore float 5.2
numero_decimale = 5.2
print(type(numero_decimale))

# variabile con valore str
stringa = "federico"
print(type(stringa))

# variabile ccon valore bool
booleano = True # False
print(type(booleano))


# se non conosco il tipo di una varaibile e voglio testare se è quello che volgio io posso...
x = 4.7 
print(x.is_integer()) # valuta per capire se la varaibile è un int dando un True o False 
# operatore "." richiama una funzione per una variabile 


# non conviene fare questo tipo di assegnazione su una riga ma si può volendo fare. 
numero1, numero2, numero3 =1, 2, 3
print(numero1, numero2, numero3)


### OPERATORI ###
n1 = 3
n2 = 2

# operatore somma
nsomma = n1 + n2
print(nsomma)

# operatore differenza
ndiff = n1 - n2
print(ndiff)

# operatore divisione
ndiv = n1 / n2
print(ndiv) # nota che anche se sono due interi n1 e n2 il risultato ndiv è un float, non è scontato, nelle vecchie versioni non era cosi
print(type(ndiv)) # divisione intera si fa con //

# operatore prodotto
nprod = n1 * n2
print(nprod)

# operatore potenza 
npotenza = n1 ** n2
print(npotenza)

# operatore modulo = ti ritorna il resto della divisione 
nmodulo = n1 % n2
print(nmodulo) # mi ritorna il testo della divisione. 



# assegnamento e addizione
numero_n = 5
# numero_n + 1 --> serve se volgio aggiungere 1 a la variabile numero_n che è 5. ma posso anche fare... 
numero_n += 1
print(numero_n)

# si può fare anche per gli altri operatori 
numero_n -= 1
numero_n /= 1
numero_n *= 1


### OPERATORI DI CONFRONTO ###
# mi fonrisce un valore boolean True o False relativo a come percepisce il mio calcolo. 
5 == 5 # uguale 
n1 = 5
n2 = 5
n1 < n2
n1 > n2
n1 >= n2
n1 <= n2


### OPERATORI LOGICI - tabelle di verità ###


# AND logico --> operatore che ritorna VERO se e solo se entrambe sono vere, in tutti gli altri casi ritorna False. 
# V and V == V
# V and F == F
# F and F == F 

ex1 = (5 == 2) # vale False
a = 15
b = 10
ex2 = (a <= b) # vale False

print (ex1, ex2)
print(ex1 and ex2)


ex3 = (5 == 5) # vale vero
a = 10
b = 10
ex4 = (a <= b) # vale vero

print(ex3 and ex4) # in questo caso da VERO perchè le condizioni sono entrambe vere


# OR logico --> operatore che ritorna FALSO se e solo se entrambe sono false, in tutti gli altri casi ritorna Vere. 
# V or V == V
# V or F == V
# F or V == V
# F or F == F 
print(ex1 or ex2)


# NOT logico --> operatore che ritorna l'opposto di ciò che segue il NOT. 
# not V == F
# not F == V


### CONTROLLO DI FLUSSO CON IF ###
# uso all'interno del controllo di flusso, sulla base del verificarsi di dati condizioni, determino se posso far avverare date condizioni oppure no
# uso i blocchi if, se uno condizione è valutata vera allora segue le istruzioni altrimenti altro...


'''
# struttura
if <condizione>: 
    <istruzioni>
... '''

n1 = 10 
n2 = 8
if n1 > n2:
    print("n1 è maggiore di n2")
elif (n1 == n2): # valuto anche la condizione legata al if, comodo per aggiungere
    print("n1 è uguale a n2")
else: # valuta l'opposto rispetto alla condizione di if
    print("n1 è minore di b")


# valuto la condizione, se la condizione posta dopo l'if è TRUE, eseguo il contenuto dopo l'indentazione. 




### note sul tipo STINGA e modalità di visualizzazione  ###

# è una sequenza di caratteri
s1 = "Python"
print(s1)

# posso accedere al livello posizionele del carattere della strainga da 0 a n inserendo le []
# char   P y t h o n 
# index  0 1 2 3 4 5 
print(s1[1])

# con la funzione len() scopro il numero dei caratteri della varaibile 
print(len(s1))


s2 = "Python per tutti"
print(s2[0:6]) # stampa i caratteri da 0 incluso a 6 ESCLUSO (escludo quindi lo spazio che è il sesto carattere)
print(s2[6:]) # stampo dal sesto carattere in avanti 


# verificare se una lettera è presente nella stringa
print("y" in s1) # TRUE
print("a" in s1) # FALSE


print(s1[-1]) # valore negativo, mi indica i caratteri da destra verso sinistra

s3 = "per tutti"

print(s1 + " " + s3)
print(s1, s3)
# python per tutti
print(s1 + "_" + s3[0:3] + "_" +s3 [4:])

# sfrutto la funzione print a pieno
print(s1, s3, sep="_", end="!") # aggiungo il carattere di separazione con sep= e il carattere da aggiungere alla fine con end=
# se sostituisco l'end di defoult con il !, non mi andrà a una nuova righa \n

print("Stiamo usando al versione {}" .format(s2)) # valutazione puntata 

# conoscere la posizione di una determinata parola
msg = "Ciao sono Python, Python è un linguaggio di programmazione"
print(msg.find("Python")) # uso la funz find, mi ritorna la posizione dell'indice della prima lettera della parola che sto cercando 
print(msg.rfind("Python")) # rfind cerco la parola python dalla fine della stringa, mi da l'index quando incontra la fine 

### COSTANTE ###
# in python non esiste il concetto di costante, ovvero una varaibile che rimanse sempre fissa, ma per convenzione si utilizza il nome della variabile TUTTO MAIUSCOLO

COSTANTE = 100



### print con le strutture comuni ###
print("regola n.1")
print("regola n.2")
print("regola n.3")

### CICLI ### CON WHILE E FOR ###
# un ciclo mi consente di eseguire un tot di volte la porzione di codice al suo interno. 


### CICLO WHILE ### 

numero_regola = 1
# fintanto che la regola è <= a 3 stampa il testo e aggiorna il valore del mio contatore (numero_regola).
# ciclo del quile torna e va avanti fintanto che è compresa nella condizione espressa dal while (in questo caso <=3)
# poi aggiungo il contatore che da 1 passa a + 1== 2 ecc ecc.. fino a quanto non arriva a colmare le condizioni dello while 
while (numero_regola <= 3): # mi pone le condizioni tale per cui il loop può andare avanti ma anche FERMARSI
    print("regola n.", numero_regola)
    numero_regola += 1 # è il mio contatore, fa si che si increamenti di 1 prima di ricomincaire il loop


### CICLO FOR ###
# prendo una serie di valori e faccio un loop legandolo a una varaibie temporale espresso da i --> acquisisce valore sulla base del range che ho assengato
for i in range(1,4): # i varrà al primo giro 1, al secondo 2, al terzo 3
    print("Regola n.", i)


s = "python"
for c in s:
    print(c)