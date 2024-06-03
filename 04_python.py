# sturtture dati: LIST , SET
# ORA DIZIONARI --> SALVARE DATI IN CAPPIE CHIAVE-VALORE.


#### NUOVA STRUTTURA DATI ####

"""
# K --> chiavi che mi indentificano un valore associato. 
# V --> valore che volgio salvare 

chiavi: 
nome: MARIO 
cognome: ROSSI
tel: 3356622784

nota la chiave recupero il valore associato

"""
# come definisco un dizionario, {K:V , chiave:valore, chiave:valore}
d1 = {"nome":"MARIO", "cognome":"ROSSI", "tel":"3356622784"}
# le chiavi sono stringe
# i valori possono essere int o string

print(type(d1)) # tipo : dict


print (d1.keys()) # riporta chiavi 
print (d1.values()) # riporta valori
print (d1.items()) # riporta tutte le coppie chiave-valore


for v in d1.keys():
    print(v)

for v in d1.values():
    print(v)

for v in d1.items():
    print(v)


# struuttura per immagazzianre informazioni in cui il valore nonè una stringa e un numero ma è una lista o un altro dizionario 
d2 = {"a":{"aa":1, "aaa": 2, "aaaa": 3}}

print (d2.keys()) 
d2["a"]
print (d2.values())



# nelle liste

[x for x in range(10)]
d3 = ({x:x**2 for x in range(10)}) # la chiave è la x del ciclo for da 1 a 10, e il valore è la potenza di 2 dello stesso. 
print(d3)
print(d3[9]) # richiamando la chiave [9] --> mi ritorna il valore associato 81



for i in d3.items(): # riporta la coppia chiave valore della posizione --> 10 items == 10 coppie 
    print(i)

"""
(0, 0)
(1, 1)
(2, 4)
(3, 9)
(4, 16)
(5, 25)
(6, 36)
(7, 49)
(8, 64)
(9, 81)
"""
for k,v in d3.items(): # riporta il singolo valore dove k è la chiave e v e il valore. 10 valori di K associati ai 10 valori di V 
    print(k,v)
"""
0 0
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81
"""

test_list =[
    {"course": "pyhton", "Author":"Jerry"},
    {"course": "C++", "Author":"Mark"},
    {"course": "Java", "Author":"Carlo"}
    ]



