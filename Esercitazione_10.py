
def somma(a, b):
    risultato = a + b
    return risultato

def differenza(a, b):
    risultato = a - b
    return risultato

def moltiplicazione(a, b):
    risultato = a * b
    return risultato

def divisione(a, b):
    if b == 0:
        print("Dividere un numero per zero non si può fare")
    risultato = a / b
    return risultato


def calcola (num1,num2,operazione):
    if type(num_1) == int and type(num_2) == int:
        if operazione == "somma":
            return somma(num_1,num_2)
        elif operazione == "differenza":
                return differenza(num_1,num_2)
        elif operazione == "moltiplicazione":
                return moltiplicazione(num_1,num_2)
        elif operazione == "divisione":
                return divisione(num_1,num_2)
        else:
            print("l'operazione da te inserrita non è stata riconosciuta dal programma")
    else:
        print("non hai inserito un numero intero")

num_1 = int(input("Forniscimi un nuemro: "))
operazione = input("inserisci l'operatore ")
num_2 = int(input("Forniscimi un nuemro: "))

print(calcola(num_1,num_2,operazione))



"""
operazione = input("inserisci l'operazione: somma, differenza, moltiplicazione, divisione\n ")
if type(num_1) == int and type(num_2) == int:
    if operazione == "somma":
        print(somma(num_1,num_2))
    elif operazione == "differenza":
        print(differenza(num_1,num_2))
    elif operazione == "moltiplicazione":
        print(moltiplicazione(num_1,num_2))
    elif operazione == "divisione":
        print(divisione(num_1,num_2))
    else:
        print("l'operazione da te inserrita non è stata riconosciuta dal programma")
else:
    print("non hai inserito un numero intero")
"""