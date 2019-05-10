'''
Created on Mar 10, 2019

@author: jgomezm
'''

def isArrayInSortedOrder(A):
    if len(A)==1:
        return True
    
    check = (A[0] <= A[1]) and isArrayInSortedOrder(A[1:])
    
    return check


A= [127, 220, 246, 277, 321, 454, 534, 565, 933]

print(isArrayInSortedOrder(A))