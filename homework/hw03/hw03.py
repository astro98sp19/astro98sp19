"""ASTRONOMY 98/198 SPRING 2019"""
"""HOMEWORK 3"""

# Q00: Import Your Module(s)!
###IMPORT MODULES HERE###
#HINT: YOU NEED TO import TWO MODULES FOR THIS HOMEWORK


# Q01: SUM NUM
def digit_sum(n):
    """
    This function sums the digits of a nonnegative integer.

    Parameters
    --------------
    n (integer): nonnegative whole number

    Returns
    --------------
    integer or exception statement

    Exceptions
    -------------
    Input variable must be a positive integer.

    >>> digit_sum(3579)
    24
    >>> digit_sum(54321)
    15
    >>> digit_sum('abcd')
    Your input variable must be a positive integer.
    """
    ...###YOUR CODE HERE (DELETE THE ...)###


# Q02: QUADRATIC FORMULA
def quadratic_root(a, b, c):
    """
    This function takes in three parameters a, b, c, and returns a list of the real
    roots of the the quadratic polynomial: ax^2 + bx + c.

    Parameters
    --------------
    a (float): quadratic coefficient
    b (float): linear coefficient
    c (float): constant coefficient

    Returns
    -------------
    list of floats listed from least to greatest

    Exceptions
    -------------
    If the discriminant is < 0 (no real roots), a warning is returned

    >>> quadratic_root(1,-2,1)
    [1.0]
    >>> quadratic_root(1, 5, 6)
    [-3.0, -2.0]
    >>> quadratic_root(1,0,1)
    This function returns only real roots, sorry!
    """
    ...###YOUR CODE HERE (DELETE THE ...)###


# Q03: A REVISED NICHOLAS PROBLEM
"""
Suppose you have a string of 400 Christmas lights. At the start, they are all
turned off. After 1 second, every single light turns on. After 2 seconds, every
second light (2nd, 4th, 6th, etc.) turns off. After 3 seconds, every third light
switches (i.e., the 3rd, 9th, 15th, etc. lights turn off and the 6th, 12th, 18th,
etc. lights turn on). After 4 seconds, every fourth light switches. And so on.
Which lights are on after 100000 seconds?

If you're particularly clever, you may be able to see the answer without even
doing any number crunching. However, we are going to solve this problem with
brute force in two different ways: using two for loops and one for loop and
numpy arrays.

Write two functions which return either a list or an array containing only the
numbers of the lights which are on after 100000 seconds.
"""

# PART A
def christmas_lights_with_loops():
    """
    This function takes in no arguments and solves the Christmas lights problem
    described above with two for loops.

    Parameters
    --------------
    None

    Returns
    -------------
    integer

    Exceptions
    -------------
    None

    >>> christmas_lights_with_loops()[0]
    1
    >>> christmas_lights_with_loops()[3]
    16
    """
    ...###YOUR CODE HERE (DELETE THE ...)###

# PART B
def christmas_lights_with_numpy():
    """
    This function takes in no arguments and solves the Christmas lights problem
    described above with numpy arrays.

    Parameters
    --------------
    None

    Returns
    -------------
    integer

    Exceptions
    -------------
    None

    >>> christmas_lights_with_numpy()[0]
    1
    >>> christmas_lights_with_numpy()[5]
    36
    """
    ...###YOUR CODE HERE (DELETE THE ...)###

# PART C
def time_func(func):
    """
    This function takes in a function that requires no arguments and returns whatever
    the function returns, followed by the runtime of the function.

    Parameters
    --------------
    function: this input function must take in no parameters

    Returns
    -------------
    integer: runtime of the input function

    Exceptions
    -------------
    None

    >>> part_a = time_func(christmas_lights_with_loops()
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    >>> part_b = time_func(christmas_lights_with_numpy()
    array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])
    >>> b - a < 0
    True
    """
    start_time = #INSERT YOUR CODE HERE
    #INSERT YOUR CODE HERE (HINT: SIMPLY CALL THE INPUT FUNCTION)
    end_time = #INSERT YOUR CODE HERE
    runtime = #INSERT YOUR CODE HERE
    return runtime


# Q04: A SECOND NICHOLAS PROBLEM
def number_madness():
    """
    NOTE: YOU MUST COMPLETE THE DIGIT SUM FUNCTION BEFORE TESTING THIS FUNCTION.
    NOTE: USE NUMPY ARRAYS. IT'S EASIER AND FASTER THAN LOOPS!

    This function takes in no arguments and returns three numbers:
    (i)the number of numbers from 1 to 100000, inclusive, that are divisible by
    2, 3, 5, and 7.
    (ii) the number of numbers from 1 to 100000, that are perfect squares and
    are also odd numbers.
    (iii) the number of numbers whose last digit is either 3 or 5, but which are
    not divisible by 15.

    Parameters
    --------------
    None

    Returns
    -------------
    list: this list should contain three integers

    Exceptions
    -------------
    None

    >>> a = number_madness()
    >>> digit_sum(a[0])
    24
    >>> a[0] % 2 == 0
    False
    >>> digit_sum(a[1])
    14
    >>> a[1] % 2 == 0
    True
    >>> digit_sum(a[2])
    26
    >>> a[2] % 2 == 0
    False
    """
    # STEP 1
    ... ###CREATE A LIST OR AN ARRAY OF NUMBERS FROM 1 to 100000 (DELETE THE ...)###

    ###HINT: YOU ARE RETURNING A COUNT OF NUMBERS. HOW CAN YOU USE PYTHON TO MEASURE
    ###THE LENGTH OF A LIST?
    # Number (i)
    ... ###HINT: THE MODULO OPERATION MIGHT BE HELPFUL HERE (DELETE THE ...)###


    # Number (ii)
    ... ###HINT: THE SQUARE ROOT OF A PERFECT SQUARE IS AN INTEGER. (DELETE THE ...)###


    # Number (iii)
    ... ###HINT: np.where (DELETE THE ...)###

    return ###YOU ARE RETURNING A LIST OF THREE NUMBERS: [Number (i), Number (ii), Number (iii)]
