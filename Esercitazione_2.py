# Esercizio 2:
'''
scrivi un programma che: 
1) chieda all'utente di inserire un valore da salvare nella varaibile "operatore1"
2) chieda all'utente di inserire l'operazione (+,-,*,/)
3) chieda all'utente di inderire un valore da salvare nella varaibile operatore2
4) stampi il risultato di: operatore1 <operazione> operatore 2 '''

operatore1 = int(input("inserisci il primo numero: "))
operazione = input("inserisci il tipo di operazione che vuoi compiere (+, -, /, *): ")
operatore2 = int(input("inseriere il secondo nuemro: "))

if operazione == "+" or operazione == "-" or operazione == "/" or operazione == "*":
    if operazione == "+":
        print(operatore1 + operatore2)
    elif operazione == "-":
        print(operatore1 - operatore2)
    elif operazione == "*":
        print(operatore1 * operatore2)
    elif operazione == "/":
        print(operatore1 / operatore2)
else:
    print("inserisci un operazione tra quelle proposte")
