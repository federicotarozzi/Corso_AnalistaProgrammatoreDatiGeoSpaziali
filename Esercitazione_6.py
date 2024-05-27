#Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10. 
# Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.



num_corretto = "7"
counter = False 
while (not counter):
    risposta = input("A che numero sto pensando? inserisci un nuemro da 1 a 10:\n ")
    if risposta == num_corretto:
        print("Bravo ci hai preso!")
        counter = True
    else:
        print("Nop, prova ancora!")