#!/usr/bin/env python3
import pytest

from os import path
import runpy
import io
import sys
from app import *

class TestAppPy:
    '''app.py'''
    def test_prints_hello_world(self):
        '''prints "Hello Flatiron! Class is in session!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello Flatiron! Class is in session!\n")

    def test_add(self):
        '''add() adds two input args and returns the sum.'''
        assert(add(7, 14) == 21)
        assert(add(3.4, 5.2) == 8.6)

    def test_validates_add(self):
        '''the two input args for add() are both numbers (integers or floats).'''
        with pytest.raises(Exception):
            add("hello", 2)

        with pytest.raises(Exception):
            add(1, "flatiron")

        with pytest.raises(Exception):
            add("hello", "flatiron")

    def test_subtract(self):
        '''subtract() subtracts two input args and returns the difference.'''
        assert(subtract(28, 21) == 7)
        assert(subtract(7.2, 2.3) == 4.9)

    def test_validates_subtract(self):
        '''the two input args for subtract() are both numbers (integers or floats).'''
        with pytest.raises(Exception):
            subtract("hello", 2)

        with pytest.raises(Exception):
            subtract(1, "flatiron")

        with pytest.raises(Exception):
            subtract("hello", "flatiron")

    def test_multiply(self):
        '''multiply() multiplies two input args and returns the product.'''
        assert(multiply(7, 7) == 49)
        assert(multiply(4.5, 2) == 9.0)

    def test_validates_multiply(self):
        '''the two input args for multiply() are both numbers (integers or floats).'''
        with pytest.raises(Exception):
            multiply("hello", 2)

        with pytest.raises(Exception):
            multiply(1, "flatiron")

        with pytest.raises(Exception):
            multiply("hello", "flatiron")

    def test_divide(self):
        '''divide() divides two input args and returns the quotient.'''
        assert(divide(70, 7) == 10.0)
        assert(divide(3.2, 2) == 1.6)

    def test_validates_divide(self):
        '''the two input args for divide() are both numbers (integers or floats). The second input cannot be equal to 0'''
        with pytest.raises(Exception):
            divide("hello", 2)

        with pytest.raises(Exception):
            divide(1, "flatiron")

        with pytest.raises(Exception):
            divide("hello", "flatiron")

        with pytest.raises(Exception):
            divide(3, 0)

    def test_calculator(self):
        '''calculator() performs the operation (+, -, *, or /) specified by the first input arg on the second and third input args and returns the result.'''
        assert(calculator('+', 10, 5) == 15)
        assert(calculator('-', 20, 15) == 5)
        assert(calculator('*', 30, 3) == 90)
        assert(calculator('/', 100, 4) == 25.0)
    
    def test_validates_calculator(self):
        '''operation is +, -, *, or /. raises Exception if any other value is passed into calculator as the input arg for operation.'''
        with pytest.raises(Exception):
            calculator('$', 1, 2)

    def test_print_greeting_loop(self):
        '''print_greeting_loop() prints each character of a string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_greeting_loop("greetings")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "g\nr\ne\ne\nt\ni\nn\ng\ns\n")
