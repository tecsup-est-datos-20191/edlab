'''
Created on Mar 5, 2019
@author: jgomezm
'''
 
# Print Function
def Print(n):
    if n == 0: # this is the terminating base case
        return 0
    else:
        print(n)
        return Print(n-1)

# Recursive call to itself again    
print(Print(40))
