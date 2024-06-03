#Esercizio con le liste#
# richiedo all'utente l'inserimento di una lista di numeri interi
# stampa la lista di numeri come li ha inserito l'utente 
# stampa la lista di numeri in ordine inverso 


lista_user = []
for i in range (5):
    lista_user.append(input("Inserisci un numero che vuoi faccia parte della tua lista: "))

print("ecco la tua lista", lista_user)
lista_user.reverse() 
print("ecco la tua lista al contrario",lista_user)


