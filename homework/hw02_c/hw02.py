"""ASTRONOMY 98/198 SPRING 2019"""
"""HOMEWORK 2"""

# Q01: ABSOLUTELY
def absolute_value(a):
    """
    This function takes in a number and returns its absolute value.

    >>> absolute_value(0)
    0
    >>> absolute_value(100.0)
    100.0
    >>> absolute_value(-100)
    100
    >>> absolute_value('a')
    Your input variable must be a number.
    >>> absolute_value([200])
    Your input variable must be a number.
    """
    ###YOUR CODE HERE!!!

# Q02: POWERFUL LISTS
def power(l,n):
    """
    This function takes in a list of numbers and a number n. It returns a list of those same
    numbers but raised to the power of n.

    >>> my_numbers = [-2, -1, 0, 1, 2, 3]
    >>> power(my_numbers,0)
    [1, 1, 1, 1, 1, 1]
    >>> power(my_numbers,3)
    [-8, -1, 0, 1, 8, 27]
    """
    ###YOUR CODE HERE!!!

#Q03: RECURSION - FACTORIALS
def recursive_factorial(n):
    """
    This function takes in an integer n and uses recursion to returns its factorial n!.

    >>> recursive_factorial(-2)
    Sorry, cannot take the factorial of a negative number!
    >>> recursive_factorial(0)
    1
    >>> recursive_factorial(5)
    120
    """
    #if ###YOUR CODE HERE
        ###YOUR CODE HERE
    #else ###YOUR CODE HERE
        ###YOUR CODE HERE

#Q04: RECURSION - FIBONACCI
def fib(n):
    """
    This function takes in an integer n and returns its Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(9)
    34
    """
    #if ###YOUR CODE HERE
        ###YOUR CODE HERE
    #else ###YOUR CODE HERE
        ###YOUR CODE HERE

#Q05: RECURSIOIN - NEWTON'S METHOD (NICHOLAS)
def newton(start_x, tol):
    """
    Newton's method is a way of approximating zeros for polynomials. This function is an implementation
    of this method for x^2 - x - 1 = 0.

    start_x: a float that is your initial guess.
    tol: a float that is the tolerance on the error in your y-value.

    >>> newton(-0.5, 0.0003)
    -0.6180555555555556
    >>> newton(1.5, 0.0003)
    1.6180555555555556
    """
    #Calculate point and slope
    #YOUR CODE HERE!!!

    #Trace the tangent line back to the x-axis
    #YOUR CODE HERE!!!

    #If the final y-value is below tolerance, return. Otherwise, use Newton's method on the new guess.
    #YOUR CODE HERE!!!
