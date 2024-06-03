#Esercizio con le liste#
# richiedo all'utente l'inserimento di una lista di numeri interi
# stampa la lista di numeri come li ha inserito l'utente 
# stampa la lista di numeri in ordine inverso 

"""
# LA MIA VERSIONE... 

lista_user = []
for i in range (5):
    lista_user.append(input("Inserisci un numero che vuoi faccia parte della tua lista: "))

print("ecco la tua lista", lista_user)
lista_user.reverse() 
print("ecco la tua lista al contrario",lista_user)

"""


user_inputs = []

while(True):
    try:
        numero = input("INSERIRE UN NUMERO: ")
        if(numero == "end"):
            break
        else:
            user_inputs.append(int(numero))
    except ValueError:
        print("nuemro inserito non valido, ti ricordo di interire un intero")
        continue

print("STAMPO LA LISTA IN ORDINE DI INSERIMENTO: ")
print(user_inputs)

user_inputs.reverse()
print("ORA, IN ORDINE INVERSO")
print(user_inputs)

# ORA CHIEDO ALL'UTENTE DI INEREIRE UN ALTRO UMERO E VADO A RICERCARE QUEL NUMERO ALL'INTENRO DELLA LISTA
# DICO ALL'UTENTE LA POSIZIONE SE OCCORRE. 

numerodacercare = int(input("Inserire numero da ricercare"))
if numerodacercare in user_inputs:
     print("numero in lista")
else:
     print("numero non in lista")



"""
# qui ho provato un'altra cosa con il try e except ma non ha senso perchè non si realizza mai l'except dal momento che il numero che chiedo di inseire sarà per forza nella lista !!!!
try:
        elementToFind = (int(input("inserisci un nuovo numero: ")))
        user_inputs.append(elementToFind)
        posizione = user_inputs.index(elementToFind)
except ValueError:
    print("il numero che hai inserito non occorre nella lista da te indicata")

print("la tua nuova lista è: ", user_inputs)
print(posizione)

"""
