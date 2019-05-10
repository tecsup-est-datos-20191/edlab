'''
Created on Mar 9, 2019

@author: jgomezm
'''
import matplotlib.pyplot as plt

def draw(x,y, type = 'b.', title='', label_x='', label_y=''):
    plt.figure()   
    plt.title(title)
    
    plot = plt.subplot()
    plot.set_xlabel(label_x)
    plot.set_ylabel(label_y)
    
    plt.plot(x, y, type)
    plt.show()
