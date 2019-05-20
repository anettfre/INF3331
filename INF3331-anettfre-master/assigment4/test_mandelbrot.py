#!/usr/bin/python3

import numpy as np
import sys

def test_plane_outside():
    """Test if some plane is entirely outside the Mandelbrot set
    Assumes that the wish is for the tests to fail
    Tests for [3, 4] × [3, 4] which is entirely outside the set so it should raise AssertionError
    """
    try:
        min1 = min2 = 3
        max1 = max2 = 4
        z1 = z2 = 5
        a = np.linspace(min1, max1, z1) #real
        b = np.linspace(min2, max2, z2) #imaginary
        set = np.zeros((len(a), len(b)))
        for i in range(z1):
            for j in range(z2):
                x = a[i]
                y = b[j]
                c = complex(x, y)
                if abs(c) < 2:
                    assert(True)
                    return 0
        assert(False)
    except AssertionError:
        print("The whole plane choosen is outside the Mandelbrot set")

def test_plane_inside():
    """Test if some plane is entirely inside the Mandelbrot set
    Tests for [-0.5, 0] × [-0.5, 0] which is entirely inside the set so it should raise AssertionError
    """
    try:
        min1 = min2 = -0.5
        max1 = max2 = 0
        z1 = z2 = 5
        a = np.linspace(min1, max1, z1) #real
        b = np.linspace(min2, max2, z2) #imaginary
        set = np.zeros((len(a), len(b)))
        for i in range(z1):
            for j in range(z2):
                x = a[i]
                y = b[j]
                c = complex(x, y)
                if abs(c) > 2:
                    assert(True)
                    return 0
        assert(False)
    except AssertionError:
        print("The whole plane choosen is inside the Mandelbrot set")


test_plane_outside()
test_plane_inside()
