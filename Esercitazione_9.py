# date 2 liste 

"""
k = []
v = []

k deve diventare le chiavi del dizionario
v devono essere le chiavi del dizionario 
elemento posizionale è l'indicatore di associazione
"""


k = [1, 2, 3, 4]
v = [10, 20, 30, 40]
diz_num = {}
#for i in range(len(k)):
for j in range(len(k)):
    diz_num[k[j]] = v[j]
    

print(diz_num.items())
"""
diz_num = {}
index = 0
for i in k:
    diz_num[i] = v[index]
    index += 1

print(diz_num)
"""

