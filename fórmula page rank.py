import pandas as pd
import numpy as np

r = np.array([1/4, 1/4, 1/4, 1/4])
A = (np.array([[0 ,1/3, 1/3, 1/3], [1/2, 0, 0, 1/2], [0, 0, 0, 1], [1/3, 1/2, 1, 0]]).transpose())

#print (r)
#print(A)

def formula():
    i = 0
    lista = []
    while i < 5:
        equacao = (A*r**i)
        lista.append(equacao)
        i+=1
    return lista

#print(formula())