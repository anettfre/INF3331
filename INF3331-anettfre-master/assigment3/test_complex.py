#!/usr/bin/python3
import sys
from complex import *

def test_conjugate():
    """test is for finding out what the conjugate is. This use the __eq__ function,
    here it checks if if the conjugate function from complex.py is giving the correct answer.
    If the test does not work it will raise an AssertionError and then print something and exit the program"""
    try:
        assert Complex(2, 4).conjugate() == Complex(2, -4)
    except AssertionError:
        print("The conjugate test did not go well")
        sys.exit(1)

def test_modulus():
    try:
        """Test if the modulus function from complex.py if giving the number i expect it to give"""
        assert Complex(3, 4).modulus() == 5
    except AssertionError:
        print("The modulus test did not go well")
        sys.exit(1)

def test_add_complex():
    try:
        """Test if the add function works. Does it by writing that if the function gives the expected answer it will not raise an AssertionError"""
        a = Complex(2, 2) + Complex(1, 4)
        b = Complex(3, 6)
        assert a == b
        assert Complex(1, 1) + (1+1j) == Complex(2, 2)
    except AssertionError:
        print("The addition test did not go well")
        sys.exit(1)

def test_sub_complex():
    try:
        """Test if the sub function works"""
        a = Complex(2, 3) - Complex(1, 2)
        b = Complex(1, 1)
        assert a == b
    except AssertionError:
        print("The subtraction test did not go well")
        sys.exit(1)

def test_mul_complex():
    try:
        """Test if the mul function works"""
        a = Complex(1, 1) * Complex(1, 1)
        b = Complex(0, 2)
        assert a == b
    except AssertionError:
        print("The multipication test did not go well")
        sys.exit(1)


def test_eq():
    try:
        """Test if the eq function works, be seeing if the function calculates that to complex numbers that is equal is equal"""
        assert Complex(2, 3) == (2+3j)
        assert Complex(2, 3) ==  Complex(2, 3)
    except AssertionError:
        print("The eq test did not go well")
        sys.exit(1)

def test_radd():
    try:
        """Test if the radd function works"""
        assert (4+4j) + Complex(3, 4) == Complex(7, 8)
        assert Complex(2, 3) + (2+2j) == Complex(4, 5)
        assert Complex(2, 2) + 2 == Complex(4, 2)
    except AssertionError:
       print("The radd test did not go well")
       sys.exit(1)

def test_rsub():
    try:
        """Tests if the rsub function works"""
        assert (4+4j) - Complex(5, 5) == Complex(1, 1)
        assert 4*Complex(3,4) - 2 == Complex(10, 16)
    except AssertionError:
        print("The rsub test did not go well")
        sys.exit(1)

def test_rmul():
    try:
        """Test if the rmul function works"""
        assert (1+1j) * Complex(1, 1) == Complex(0, 2)
    except AssertionError:
        print("The rmul test did not go well")
        sys.exit(1)

"""to run the test when calling the program from teminal they need to be called, this is done here"""
test_conjugate()
test_modulus()
test_add_complex()
test_sub_complex()
test_mul_complex()
test_eq()
test_radd()
test_rsub()
test_rmul()
