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
"""
# modalità che prevede di aprire (open) e chiudere (close) un file 

file = open('file.txt', "r") # open() accetta due parametri --> il file, e il fomrato scrittura, append o lettura (r, w, a) (read, write, append)
for riga in file.readlines: # leggo tutta la riga fino a quando non trovo un parametro che indica nuova riga
    print(riga)
file.close() # servere a chiudere la risorsa quando termino l'elaborazione. 



# modalità alternativa --> COSTRUTTO WITH
with open("file.txt", "r") as file:
    for rig in file.readlines():
        print(riga, end=" ")

with open("file.txt", "w") as file:
    file.write("scrivo qualcosa di nuovo nel file") # sovrasccrivo. 

"""
# per settare la directory 
import os
w_dir = "C:/Users/chicc/OneDrive/Desktop"
file_name = "file.txt"
file_path = os.path.join(w_dir, file_name) # unisce le stringhe che passo come argomento
print(file_path)

with open(file_path, "r") as file:
    print(file.read())

with open(file_path, "w") as file:
    file.write("scrivo qualcosa di nuovo nel file") 

with open(file_path, "r") as file:
    print(file.read())