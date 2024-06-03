
# ESERCIZIO #

l1 = [1,2,3,4,3,3,7,8,3]
elementToFind = 3
indexOf = -1

while(indexOf < len(l1)-1): # lunghezza degli elementi della lista meno uno test per vedere se sta nella lunghezza della mia lista. 
  try:
    print('finestra di ricerca: ', l1[indexOf+1])
    indexOf += l1[indexOf+1:].index(elementToFind)+1
    print("il numero {} è in posizione:{} ".format(elementToFind, indexOf,'\n'))
  except:
    print("non ci sono altre occorrenze del numero {}".format(elementToFind))
    break
# utilizzo operatore di increamento
# slicing sulle liste, sposto la finestra di ricerca dell'elemento dalla posizione dell'ultimo elemento trovato + 1
# operatore index che mi trova solo il primo in ordine. 

# USO LA FUNZIONE TRY & EXCEPT--> mi permettono di gestire un codice contenente un errore nel try e nel momento che lo incontra ed è reversibile allora mi riposta all'exept
# in questo caso nell'ultima porzione di lista non è presente un 3 pertanto mi dice che la funzione index non può essere usato per ricercare il 3 in una lista che non lo contiene. 
'''
list_1 = ['a', 'b', 'c', 'd']
list_1[1:3] # slicing prendo solo un pezzo della lista in modo da prendere solo una porzione della lista, quella compresa in questo caso dall'intervallo di posizione 1:3
'''
