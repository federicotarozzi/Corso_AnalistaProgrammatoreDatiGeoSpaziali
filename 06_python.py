# per effettuare le funzioni di INPUT e OUTPUT
# I/O 
import os # è il modulo che contiene le funzioni relative a input e output

"""
file = open("file.txt", "r")

# un file può essere aperto in fomrato: write(sovrascrivere), append(aggiungere), read (modalità di lettura)

contenuto = file.read()
print(contenuto)
file.close
"""


file = open('file.txt', "r")
for riga in file.readlines:
    print(riga)
file.close