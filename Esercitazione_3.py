# scrivere un programma per aprire una porta: chiedi di inserire una chiave e assicurati che sia corretta per dare accesso alla porta. 
# dai accesso se il codice inserito corrisponde alla chiave
# il pin deve essere lungo 4 caratteri 
# fai in modo che la chiave inserita dall'utente sia esclusivamente una serie di numeri 

code = input("inserisci il codice di accesso a 4 cifre: ")
cifre="0123456789"
key = "1234" # chiave di accesso 
# if ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0") in code: # non andava bene perchè l'in va a guardare solo la prima cifra in questo caso. 
if code[0] in cifre and code[1] in cifre and code[2] in cifre and code[3] in cifre:  # se il primo carattere in cifre e così via... allora mi conferma che tutte le 4 cifre sono cifre
    if len(code)== 4: # verifico che la lunghezza della chiave sia 4
        if code == key: # mi assicuro che il codice inseriro dall'utente sia uguale alla mia chiave 
            print("Codice esatto, Accesso Consentito")
        else:
            print("Accesso Negato!")
    else:
        print("la chiave deve avere 4 cifre") 
else:
    print("la chiave inserita non è composta da cifre")

'''
altro modo per scrivere le cose: 
if (code[0] in cifre and
    code[1] in cifre and
    code[2] in cifre and
    code[3] in cifre):
posso scriverlo ancge così usando le parentei per avere tutto un po' più ordinato. 
'''