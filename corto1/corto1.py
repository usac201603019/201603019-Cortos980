#Carnet 201603019, usare 019
import os

N = 19
collatz = [] #creo la lista donde guardar los numeros
for i in range(2, N):#que repita desde 2 hasta N que es mi carnet
    
    while i != 1: # Que siga hasta que sea 1 como dice el algoritmo
        if i % 2 == 0:
            collatz.append(i)    #agrego a collatz        
            i = i / 2
        else:
            collatz.append(i)            
            i = (i * 3) + 1

        if i == 1:
            collatz.append(i)
            
            print(" \n ",collatz) #imprimo collatz
            