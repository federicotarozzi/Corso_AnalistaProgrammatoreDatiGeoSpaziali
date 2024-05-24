# ESERCIZIO: scrivere un piccolo programma che verifichi se una varaibile "numero intero" sia pari o dispari

numero_int = int(input("Inserisci un numero: "))
#numero_int = 22
prova = (numero_int % 2)
if prova == 0:
    print("il tuo numero è PARI!")
else: 
    print("il tuo numero è DISPARI!")


# CASTING --> trasformare un tipo a un altro. occhio perchè si perdono infomraizoni. 



# metodo "isinstance" ritorna vero se la varaibile utente è di tipo intero. 
# oggetto è parte della calsse che ho definito

'''
numero = 2 # se io inserissi una string, mi troverebbe un errore nel primo if e quindi mi stamperebbe "effettuo il casting perchè la variabile non è un int"
if (not(isinstance(numero, int))):
    print("effettuo il casting perchè la variabile non è un int")
    numero = int(numero)

if (numero % 2):
    print("Numero disapri")
else:
    print("Numero Pari")

'''