# scrivere un programma per aprire una porta: chiedi di inserire una chiave e assicurati che sia corretta per dare accesso alla porta. 
# dai accesso se il codice inserito corrisponde alla chiave
# il pin deve essere lungo 4 caratteri 

code = input("inserisci il codice di accesso a 4 cifre: ")
key = "1234"
if len(code)== 4:
    if code == key:
        print("Codice esatto, Accesso Consentito")
    else:
        print("Accesso Negato!")
else:
    print("la chiave deve avere 4 cifre")

