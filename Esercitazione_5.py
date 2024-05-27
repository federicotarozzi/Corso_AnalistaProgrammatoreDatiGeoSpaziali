 

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
            print("+", end=" ")
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