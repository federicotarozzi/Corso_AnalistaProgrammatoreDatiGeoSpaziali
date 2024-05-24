# ESERCIZIO: scrivere un piccolo programma che verifichi se una varaibile "numero intero" sia pari o dispari

numero_int = int(input("Inserisci un numero: "))
#numero_int = 22
prova = (numero_int % 2)
if prova == 0:
    print("il tuo numero è PARI!")
else: 
    print("il tuo numero è DISPARI!")

