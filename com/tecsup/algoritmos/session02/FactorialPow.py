'''
Created on Mar 5, 2019

@author: jgomezm
'''

import sys
import numpy as np

# custom
from com.tecsup.algoritmos.session02 import Graph
    
from timeit import default_timer as timer

# funcion factorial
def factorial(n):
    if n == 0: 
        return 1
    else:
        return n*factorial(n-1)

# Cantidad maxima de recursion definido para 128

MAX_NRO = 12
x = np.arange(MAX_NRO)
y = np.arange(MAX_NRO, dtype='float')

#sys.setrecursionlimit(1027)
sys.setrecursionlimit(pow(2,MAX_NRO+1)+3)

# 
for i in range(MAX_NRO) :
    start = timer()
    nro = pow(2,i)    
    x[i] = nro
    fact = factorial(nro)
    end = timer()
    delay = end - start
    y[i] = delay
    print(i)
    print(nro)
    print(fact)
    print(delay)
    print(y[i])
    print("----------------------")

#print(x)
#print(y)

Graph.draw(x,y,'g.','Factorial vs Processing Time', 'Number', 'Time(s)')

