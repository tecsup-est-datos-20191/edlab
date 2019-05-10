'''
Created on Mar 10, 2019
@author: jgomezm
'''
# Hanoi Function 
def TowersOfHanoi(numberOfDisks, src=1, 
                  dest=3, tmp=2):
    if numberOfDisks:
        TowersOfHanoi(numberOfDisks-1, src = src, 
                      dest = tmp, tmp = dest)
        print("Move disk %d from peg %d to peg %d" 
               % (numberOfDisks, src, dest))
        TowersOfHanoi(numberOfDisks-1, src = tmp, 
                      dest = dest, tmp = src)
# Execute
TowersOfHanoi(numberOfDisks=3)
