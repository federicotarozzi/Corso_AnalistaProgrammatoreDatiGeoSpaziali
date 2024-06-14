#### OGGETTI ####

# DEFINIRE ENTITà GENERICA
# CARATTERISTICHE DIVERSE
# AZIONI E COMPORTAMENTI SIMILI 


# creo un oggetto carlcolatrice
# chiedo a questo oggetto di fare qualcosa

# concetti alla base della programmazione ad oggetti: 
# CLASSE --> rappresenta l'entità astratta (la generica automobile, caratteristiche (varibili) e funzioni)
# OGGETTO --> istanza di una classe. rappresenta la specificità degli elementi descritti dalla calsse

# ES: classe = biscotto 
# stampino a forma di stella --> classe
# creo i biscotti con la fomra della classe --> il biscotto che ottengo creo un oggetto. 
# tutti gli oggetti sono distinti tra loro come entità separate ma con caratteristiche simili perchè derivanti dalla medesima classe


# in python --> 1) definico una classe: entità generica che volgio definire


class Automobile:  # convenzione INIZIALE MAIUSCOLA PER LE CLASSI # associo ora caratteristiche (variabili) e funzioni (metodi)
    # attributi (variabili)
    # metodi (funzioni)


    # attrivuto di classe
    nruote = 4 # caratteristica condivisa trasversalmente da tutti gli elementi della classe. 

    #   METODO COSTUTTORE --> funziona richiamata per creare un oggetto di quella specifica classe. 
    def __init__(self, brand, model, color, velocita): # self rappresenta un istanza della classe, a questo aggiungo diversi attributi.
        self.brand = brand # richiamo gli elementi dell'oggetto
        self.model = model
        self.color = color
        self.velocita = velocita 
        # in questo esempio il metodo costrutture si usa tutte le volte che volgio costruire un'automobile 

    def accellera(self, val=0): # metodo 1 della classe automobile
        print("Sto accellerando")
        self.velocita += val 
    
    def decellera(self, val=0): # metodo 2 della classe automobile
        print ("Sto decelerando")
        self.velocita += val


fiat500 = Automobile("Fiat", "500", "Rosso", 0)
fiat500.accellera()
print("colore: ", fiat500.color)
print("velocità: ", fiat500.velocita)
fiat500.accellera(500)
print("velocità: ", fiat500.velocita)

bmw = Automobile("BMW","M3","Blue", 100)
print("colore: ",bmw.color)
print("velocità: ",bmw.velocita)
bmw.accellera(100)
print("velocità: ",bmw.velocita)


# vedo come andare a richiamare l'attributo di classe. 
print(fiat500.__class__.nruote)
print(bmw.__class__.nruote)





