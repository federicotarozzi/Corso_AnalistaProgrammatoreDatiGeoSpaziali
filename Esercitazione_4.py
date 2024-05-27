# prendo l'eserrcizio precedente ma faccio in modo che se sbaglio ad inserire la chiave torna indeitro e mi fa reinserire il code

# METODO 1 MENO CHIARO uso una variabile sentinella correct_key

cifre="0123456789"
key = "1234" # chiave di accesso 
#val_inizio = 1
#val_max = 3 # parte da 0-1-2
# and (val_inizio <= val_max) 
counter = 0 # variabile temporale che inizia da 0
correct_key = False 
while((not correct_key)and(counter <= 2)): # metto tutto all'interno di un ciclo while 
    code = input("inserisci il codice di accesso a 4 cifre: ")
    if len(code)== 4: # verifico che la lunghezza della chiave sia 4
        if code[0] in cifre and code[1] in cifre and code[2] in cifre and code[3] in cifre:  # se il primo carattere in cifre e così via... allora mi conferma che tutte le 4 cifre sono cifre
            if code == key: # mi assicuro che il codice inseriro dall'utente sia uguale alla mia chiave 
                print("Codice esatto, Accesso Consentito")
                correct_key = True # se arriva a questo punto ed è corretto allora la variabile diventa true. !serve a interrompere il ciclo! 
            else:
                print("Accesso Negato!")
        else:
            print("la chiave inserita non è composta da cifre")
    else:
        print("la chiave deve avere 4 cifre")
    counter += 1 # il caounter + uno lo matto alla fine del codice. 
    if (counter == 3) and not correct_key:
        print("Hai esauruto il numero di tentativi a disposizione")

# il loop si fa partire all'inizio e si fa finire alla fine fine di ogni condizione. 



 # METODO 2 PIù CHIARO
'''
cifre="0123456789"
key = "1234" # chiave di accesso 

while(True): # va all'infinito, eseguo queste istruzioni fino a che non trovo il break 
    code = input("inserisci il codice di accesso a 4 cifre: ")
    if code[0] in cifre and code[1] in cifre and code[2] in cifre and code[3] in cifre:  # se il primo carattere in cifre e così via... allora mi conferma che tutte le 4 cifre sono cifre
        if len(code)== 4: # verifico che la lunghezza della chiave sia 4
            if code == key: # mi assicuro che il codice inseriro dall'utente sia uguale alla mia chiave 
                print("Codice esatto, Accesso Consentito")
                break
            else:
                print("Accesso Negato!")
        else:
            print("la chiave deve avere 4 cifre") 
    else:
        print("la chiave inserita non è composta da cifre")


# while = True --> metodo per far partire un ciclo infinito, va poi stoppato nel punto opportuno altrimenti quello va avanti. 

'''



