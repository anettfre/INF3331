#!/usr/bin/python3
from math import sqrt
class Complex():


    def __init__(self, real, imag):
        """takes in self, a real part, and a imaginery part"""
        self.real = real
        self.imag = imag



    # Assignment 3.3

    def conjugate(self):
        """this function takes in one argument, that is self, and self has a real part and imagenary part.
        Returns a new instanse of a complex number, that is the conjugate og self that was given as argument"""
        return Complex(self.real, -self.imag)

    def modulus(self):
        """takes in self, calculates the modulus, returns an int or float"""
        mod = sqrt(self.real**2 + self.imag**2)
        return mod

    def __add__(self, other):
        """takes in self and other, that can be to complex numbers with real and imag.
        Calculates the real part of self and other, by adding them.
        Calculates the imaginery part of self and other, by adding them. Makes a new complex number with the new calculated values and returns it"""
        addedreal = self.real + other.real
        addedim = self.imag + other.imag
        return Complex(addedreal, addedim)

    def __sub__(self, other):
        """Takes in self and other that can be complex mumber, subtract the real and imagenary parts from each other and returns a new complex number"""
        subreal = self.real - other.real
        subim = self.imag - other.imag
        return Complex(subreal, subim)

    def __mul__(self, other):
        """The formula: (a+bi)(c+di) = (ac + adi + bci + bd(i^2)) = (ac - bd) + (ad + bc)i.
        Calculates, then makes a new complex number with the new calculated values and returns it"""
        mulreal = self.real * other.real #ac
        mulim = self.imag * other.imag #bd
        mulmix1 = self.real * other.imag #ad
        mulmix2 = self.imag * other.real #bc
        return Complex((mulreal - mulim), (mulmix1 + mulmix2))

    def __eq__(self, other):
        """takes in self and other, if the statment is true the numbers are equal then it returns ture.
        It returns false if the numbers imagenary or/and real part is different"""
        if self.real == other.real and self.imag==other.imag:
            return True
        else:
            return False

    # Assignment 3.4
    def __radd__(self, other):
        """takes in self and other, makes a new complex number with the new calculated values and returns it"""
        addedreal = self.real + other.real
        addedim = self.imag + other.imag
        return Complex(addedreal, addedim)

    def __rsub__(self, other):
        """takes in self and other, makes a new complex number with the new calculated values and returns it"""
        subreal = self.real - other.real
        subim = self.imag - other.imag
        return Complex(subreal, subim)

    def __rmul__(self, other):
        """takes in self and other, the formula: (a+bi)(c+di) = (ac + adi + bci + bd(i^2)) = (ac - bd) + (ad + bc)i.
        Calculates, then makes a new complex number with the new calculated values and returns it"""
        mulreal = self.real * other.real #ac
        mulim = self.imag * other.imag #bd
        mulmix1 = self.real * other.imag #ad
        mulmix2 = self.imag * other.real #bc
        return Complex((mulreal - mulim), (mulmix1 + mulmix2))


    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        """takes in self, that is a complex number, then returns pythons version of complex number"""
        return complex(self.real, self.imag)
