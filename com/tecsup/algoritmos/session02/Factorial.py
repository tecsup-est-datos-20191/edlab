'''
Created on Mar 5, 2019
@author: jgomezm
'''
    
# Factorial function
def factorial(n):
    if n == 0: 
        return 1
    else:
        return n*factorial(n-1)

# Using
print(factorial(3))