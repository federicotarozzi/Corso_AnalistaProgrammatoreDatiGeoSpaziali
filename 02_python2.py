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






