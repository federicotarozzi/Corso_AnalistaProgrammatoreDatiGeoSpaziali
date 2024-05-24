# prendo l'eserrcizio precedente ma faccio in modo che se sbaglio ad inserire la chiave torna indeitro e mi fa reinserire il code

cifre="0123456789"
key = "1234" # chiave di accesso 
correct_key = False
while(not correct_key): # metto tutto all'interno di un ciclo while 
    code = input("inserisci il codice di accesso a 4 cifre: ")
    if code[0] in cifre and code[1] in cifre and code[2] in cifre and code[3] in cifre:  # se il primo carattere in cifre e così via... allora mi conferma che tutte le 4 cifre sono cifre
        if len(code)== 4: # verifico che la lunghezza della chiave sia 4
            if code == key: # mi assicuro che il codice inseriro dall'utente sia uguale alla mia chiave 
                print("Codice esatto, Accesso Consentito")
                correct_key = True # se arriva a questo punto ed è corretto allora la variabile diventa true
            else:
                print("Accesso Negato!")
        else:
            print("la chiave deve avere 4 cifre") 
    else:
        print("la chiave inserita non è composta da cifre")

# il loop si fa partire all'inizio e si fa finire alla fine fine di ogni condizione. 
