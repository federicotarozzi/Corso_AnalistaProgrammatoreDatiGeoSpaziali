

# DEFINISCI UNA CLASSE:
"""


"""
class Persona:
    def __init__(self, nome, cognome, eta, indirizzo): 
        self.nome = nome # richiamo gli elementi dell'oggetto
        self.cognome = cognome
        self.eta = eta 
        self.indirizzo = indirizzo

    
    def modifica_indirizzo(self, nuovo_indirizzo):
          print("il nuovo indirizzo è: ",nuovo_indirizzo)
    
    def aggiorna_eta(self, nuova_eta):
          if(self.eta > 0 or self.eta < 120):
               self.eta = nuova_eta 
          print("la nuova eta è: ", nuova_eta)
    
    def stampaInfo():
         print("nome")



Fede = Persona("Federico", "Tarozzi", 23, "via san carlo 45")
Fede.aggiorna_eta(24)
Fede.modifica_indirizzo("Via fratelli Rosselli 15")



Agu = Persona("Agustin", "Lopez", 28, "Da qualche parte a Mendoza")
Agu.aggiorna_eta(32)
Agu.modifica_indirizzo("via del football 29")
