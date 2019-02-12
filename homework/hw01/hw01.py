"""Homework 1: Trying okpy!!!"""

# Q00: GREETINGS
def hello():
    """
    This function should display the string 'Hello!'

    >>> type(hello()) #Be careful! We're not asking you to print a string!
    <class 'str'>
    >>> hello()
    'Hello!'
    """
    ###YOUR CODE HERE!!!

# Q01: SUM (BUDDY ONCE TOLD ME)
def add(a, b):
    """
    This function takes in two numbers and should return the sum of those two numbers.

    >>> add(18, 27)
    45
    >>> add(-20, 40)
    20
    >>> add(7 + 4, 2 + 2)
    15
    """
    ###YOUR CODE HERE!!!

#Q02: THREE TIMES OVER
def cube(n):
    """
    This function takes in a number and should return that number's third power.

    >>> cube(0)
    0
    >>> cube(2)
    8
    >>> cube(-3)
    -27
    """
    ###YOUR CODE HERE!!!

#Q03: YOU SHOULD NOT USE FUNCTIONS THAT ALREADY EXIST TO REWRITE THOSE FUNCTIONS
#(HINT - except for this problem)
def make_number(s):
    """
    This function takes in a string and should return a floating point number.

    >>> make_number('8.7')
    8.7
    >>> make_number('22.8')
    22.8
    >>> make_number('19')
    19.0
    """
    ###YOUR CODE HERE!!!

#Q04: YOU SHOULD NOT USE FUNCTIONS THAT ALREADY EXIST TO REWRITE THOSE FUNCTIONS (PART 2)
#(HINT - except for this problem)
def true_false(a):
    """
    This function should take in any basic Python data type, a, and return a truth value.
    If you're curious about how Python treats what's true and false, you can feel free to
    Google 'Python Truth Value Testing'!

    >>> true_false(0)
    False
    >>> true_false('A')
    True
    >>> true_false(False)
    False
    >>> true_false('False')
    True
    """
    ###YOUR CODE HERE!!!

#Q05: INDEXING
def retrieve_from_list(l,a):
    """
    This function takes in a list l and an integer a and returns the ath element of l. To
    make sense of the results, recall that Python lists begin at index 0.

    >>> example_list = ['Nicholas', 'Orion', 'Alex']
    >>> retrieve_from_list(example_list, 1)
    'Orion'
    >>> retrieve_from_list([1, 2, 3, 4, 5], 2)
    3
    """
    ###YOUR CODE HERE!!!

#Q06: HARDEST PROBLEM
def add_number(n):
    """
    This function takes in an integer n and returns a function that takes in an integer m. When
    called, this second function will add n to m.

    >>> adding_five = add_number(5)
    >>> adding_five(2)
    7
    """
    ###YOUR CODE HERE!!!
    #HINT: You want to define a function within a function
    return #You want to return a function
