#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import time


def mandelbrot(c, numberOfIerations):
    '''Method computes mandelbrot and returns value
    Loops over to see which number that is in the mandelbrot set
    '''
    z = complex(0,0)
    for i in range(numberOfIerations):
        if abs(z) > 2: #no mandelbrot, tends towards infinity
            return i
        z = z*z + c
    return 0

def make_set(min1, min2, max1, max2, z1=1000, z2=1000, numberOfIerations=1000):
    """Makes points and calls mandelbrot and color function, returns values
    Calls mandelbrot function with eatch point in a and b, where b is the imaginary numbers
    Calls the color function after creating the set
    z1 and z2 is resolution
    """
    a = np.linspace(min1, max1, z1) #real
    b = np.linspace(min2, max2, z2) #imaginary
    set = np.zeros((len(a), len(b)))
    for i in range(z1):
        for j in range(z2):
            x = a[i]
            y = b[j]
            c = complex(x, y)
            set[j,i] = mandelbrot(c, numberOfIerations) #since python has x as y axses

    return set

def color(set):
    '''Takes in argument that is what i want to plot and create a image of it
    Saves the image as a jpg and shows the image.
    If the numbers is in mandelbrot they will be colored black
    '''
    m = plt.cm.magma_r
    m.set_under(color='black')
    plt.imshow(set, cmap=m, origin="lower", vmin=0.1)
    plt.savefig("mandelbrot_1.jpg")
    plt.show()

if __name__ == "__main__":
    t0 = time.clock()
    set = make_set(-1.5,-1.25,0.5,1.25)
    color(set)
    t1 = time.clock()
    print('{:.3f} sec'.format(t1-t0))
