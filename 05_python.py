
### ULTIMA STRUTTURA DATI -- LE TUPLE ###
# elementi non modificabili una volta definiti. 
my_tuple = ("Mario", "rossi", "051_6611067")
print(type(my_tuple))

#my_tuple[1] = "Rossi" # mi da errore non posso sovrascrivere un elemento.

my_tuple = (1,2,3) # se la riinizializzo posso modificarla per intero
print(my_tuple)
my_tuple = ("Mario", "rossi", "051_6611067")
# posso anche inserire elementi disomogenei (interi, sting, list ecc...)

# oggetto reiterabile 
# uso le tuple quano volgio processare una lista di valori ma mi serve che la rigidità di non poterla modificare

for i in my_tuple:
    print(i)

print(len(my_tuple)) # 3
print(my_tuple.count("Mario"))


