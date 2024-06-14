

# DEFINISCI UNA CLASSE:
"""


"""
class Persona:
    def __init__(self, nome, cognome, eta, indirizzo): 
        self.nome = nome # richiamo gli elementi dell'oggetto
        self.cognome = cognome
        self.eta = eta 
        self.indirizzo = indirizzo

    
    def modifica_indirizzo(self):
          print("il nuovo indirizzo è: ")
    
    def aggiorna_eta(self):
          print("la nuova eta è: ")



persona1 = Persona("Federico", "Tarozzi", "23", "via san carlo 45")
persona1.modifica_indirizzo()
persona1.aggiorna_eta()
print("eta nuova: ", persona1.eta)
print("nuovo indirizzo modificato: ", persona1.indirizzo)




       