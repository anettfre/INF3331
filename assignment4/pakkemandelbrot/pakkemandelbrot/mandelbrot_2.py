#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import time



def mandelbrot(c, numberOfIerations):
    '''Method computes mandelbrot and returns values
    Loops over to see which number belong to the mandelbrot set
    '''
    set1 = np.zeros((len(c), len(c)))
    z = np.zeros((len(c), len(c)), dtype="complex_")

    for i in range(numberOfIerations):
        tmp = np.less(abs(z), 2.0)
        set1[tmp] = i
        z[tmp] = z[tmp]*z[tmp] + c[tmp]

    set1[set1 == numberOfIerations-1] = 0
    return set1


def make_set(min1, min2, max1, max2, z1=1000, z2=1000, numberOfIerations=1000):
    '''Makes points and calls mandelbrot and color function, returns values
    Since for-loops take time i will try to awoid them since numpy can add array whitout loops
    To create c I make array b imaginary by multiplying b with i
    z1 and z2 is resolution
    '''
    a = np.linspace(min1, max1, z1) #real
    b = np.linspace(min2, max2, z2) #imaginary

    c = a + b[:, None]*1j
    set = mandelbrot(c, numberOfIerations)
    return set

def color(set):
    '''Takes in argument that is what i want to plot and create a image of it
    Saves the image as a jpg and shows the image. Also change colors
    '''
    m = plt.cm.magma_r
    m.set_under(color="black")
    plt.imshow(set, cmap=m, origin="lower", vmin=0.1)
    plt.savefig("mandelbrot_2.jpg")
    plt.show()

if __name__ == "__main__":
    t0 = time.clock()
    set = make_set(-1.5,-1.25,0.5,1.25)
    color(set)
    t1 = time.clock()
    print('{:.3f} sec'.format(t1-t0))
