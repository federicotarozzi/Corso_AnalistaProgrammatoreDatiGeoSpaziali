 

# esercizio di disegno
# disegnare una matriec NxN di caratteri *, dove N = 4
"""
* * * *
* * * *
* * * *
* * * *
"""
counter = 0
for k in range (0,4):
    for i in range(0,4):
        if i == counter:
            print("+", end=" ") # elemento sulla diagonale 
        else:
            print("*", end=" ")
    print()
    counter += 1 
   
"""
+ * * *
* + * *
* * + *
* * * +
"""


# altro modo per scrivere
"""  
for k in range (0,4):
    for counter in range(0,4):
        if i == counter:
            print("+", end=" ") # elemento sulla diagonale 
        else:
            print("*", end=" ")
    print()

"""
# ora la diagonale al contrario 
counter = 3
for k in reversed(range(0,4)):
    for i in range(0,4):
        if i == counter:
            print("+", end=" ") # elemento sulla diagonale 
        else:
            print("*", end=" ")
    print()
    counter -= 1 


"""
* * * + 
* * + *
* + * *
+ * * *
"""
