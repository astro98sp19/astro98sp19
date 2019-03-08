"""ASTRONOMY 98/198 SPRING 2019"""
"""MIDTERM PART 1: REVIEW"""

"""
Hey everyone, Alex here. This week's "homework" (midterm part 1) is going to be a review.
It's come to my attention that the lectures have not been fully in line with the homework,
so this week I'm going to try to write something that is hopefully a lot more clear
with its directions. I will also include descriptions/reviews of concepts that
should have been covered in lecture. Ideally, you will find this homework at once
rewarding and manageable. Unlike other homeworks, there will be a lot more reading
involved in this document.
"""

"""
Firstly, a review of how to do the assignments. Recall that in lecture you learned
what functions were (at least you should have learned).

So suppose I'm in my terminal, in a Python environment. I should see this:

[Below is a Terminal Display - I'm writing this just for clarity, you will
not see these bracketed things in your terminal window.]

>>>

[End of Terminal Display]

The three arrows indicate user input. Once a user writes something, and then presses
the "Enter/Return" key on their keyboard, Python will interpret what was written
and "return" a result. For instance,

[Below is a Terminal Display]

>>> 2
2
>>> 3.14159
3.14159
>>> "Alex"
'Alex'
>>> Alex
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Alex' is not defined

[End of Terminal Display]

Woah, what happened there? Well, any set of characters that is not a number or not
enclosed in quotes is considered a variable. With the exception of certain built-in
Python functions or key words, such as True, False, and type, the onus is on you
to define these variables. If you do not, you will get the error you see above.
In this case, the error is quite clear; "name 'Alex' is not defined". We haven't
defined a variable named 'Alex' yet! Let's do just that:

[Below is a Terminal Display]

>>> Alex = 'Alex'
>>> Alex
'Alex'
>>> Alex = 2
>>> Alex
2

[End of Terminal Display]

You can redefine your variables, as I did up there. I first defined Alex to be a string,
'Alex', before redefining Alex to be the integer 2. When you call a variable in Python,
Python will attempt to retrieve the most recently defined variable.

Now you've also learned about functions. Functions make it easy to generalize a procedure.
For instance, suppose Nicholas asked you to find the powers of many numbers. He says,
"Find the 5th power of 2, the 8th power of 4, and the 3rd power of 9." You can certainly
input these things manually into Python like so:

[Below is a Terminal Display]

>>> 2 * 2 * 2 * 2 * 2
32
>>> 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4
65536
>>> 9 * 9 * 9
729

[End of Terminal Display]

But it's more convenient to use a function to do the above:

[Below is a Terminal Display]

>>> def exp(num, pow):
...     result = num**pow
...     return result
...
>>> exp(2, 5)
32
>>> exp(4,8)
65536
>>> exp(9,3)
729

[End of Terminal Display]

Of course, you could have just typed 2**5 to begin with, but when it comes to more
complex operations, functions are the way to go. That said, what happens if I set
variables equal to functions? Well, let's find out! Suppose I implemented the exp
function shown above.

[Below is a Terminal Display]

>>> my_var = exp
>>> my_var           #The portion after 'at' will vary from user/computer to user/computer
<function exp at 0x1047921e0>
>>> my_var = exp(1, 1)
>>> my_var
1

[End of Terminal Display]

***IMPORANT:
If you set a variable equal to the function without calling it - without parenthesis () -
then the variable will be equal to the function. If you set a variable equal to the
function call, then the variable will be equal to that function's return value.
^^^THIS IS SUPER IMPORTANT. REREAD IF YOU MUST.^^^

For fun, let's further investigate setting a variable equal to a function without
calling it:

[Below is a Terminal Display]

>>> my_var = exp
>>> my_var(1, 1)
1

[End of Terminal Display]

Neat!

ALL THIS SAID, ALL OF YOUR HOMEWORK PROBLEMS ARE DONE IN THE CONTEXT OF FUNCTIONS JUST
LIKE THE ONE YOU SAW ABOVE. THE DIFFERENCE IS I INCLUDE A DOCTEST. WHAT DOES THAT MEAN?
Well. It means that when I define a function, I don't just implement it, but I also
include a string that documents what it's supposed to do - aptly named a "docstring."
This docstring includes a series of tests to make sure one implements it correctly -
hence the name, "doctest." As an example, the above function would look like this:
"""

#Q00: DOCSTRINGS/DOCTESTS********************************
#Re-implement the function above!
def exp(num, pow):
    """
    This function takes in two numbers and returns the first number to the power
    of the second number. Notice that this docstring explains what I explained above,
    but more concisely.Beneath this description is a docstring that shows how the
    function should behave, once it's implemented. For the sake of clarity and ease,
    the docstest for this function is exactly the same as the examples I used above.

    >>> exp(2, 5)
    32
    >>> exp(4,8)
    65536
    >>> exp(9,3)
    729
    """
    #YOUR CODE HERE
    return

"""
Made it this far? Great! Let's review one of the most important structures in Python:
lists. Lists are an incredibly convenient way to store data, and you will have to
work with them throughout your time as a programmer - especially if you decide to
pursue astronomy. So how do lists work? Let's see!

[Below is a Terminal Display]

>>> [1, 2, 3, 4, 5]                     #This is a list
[1, 2, 3, 4, 5]
>>> []                                  #This is an empty list
>>> new_list = []                       #Let's set a variable equal to an empty list
>>> new_list
[]
>>> type(new_list)                      #Querying the datatype
<class 'list'>
>>> len(new_list)                       #Length of the list
0
>>> new_list.append(10)                 #Appending a value to the list
>>> len(new_list)
1
>>> new_list                            #Appending modifies the original list
[10]
>>> new_list[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> new_list[0]                         #The above error occurs because list-indexing begins at 0
10
>>> new_list.append('Not a Number')
>>> len(new_list)
2
>>> new_list                            #You are allowed to mix datatypes in a list.
[10, 'Not a Number']
>>> new_list[1]
'Not a Number']
>>> print(new_list[1])                  #Printing displays strings without quotes.
Not a Number

[End of Terminal Display]

So those are some of the basics of lists. Let's start with something easy regarding lists.
Finish the function below so that it returns a list of 5 elements.
"""

#Q01: LIST FIVE THINGS
def five_things():
    """
    This function takes in no arguments and returns a list of 5 arbitrary things.

    >>> test = five_things()
    >>> len(test)
    5
    """
    my_list = []
    #YOUR CODE HERE
    #YOU CAN APPEND 5 RANDOM THINGS TO my_list OR RETURN ANOTHER LIST OF 5 RANDOM ITEMS
    return #SOME LIST

"""
Lists often go hand in hand with loops in Python. Lists can be constructed from loops,
or lists can be parsed through with loops. For instance, suppose I have a set of data
that I want to sum. I could do something like this:

[Below is a Terminal Display]

>>> some_data = [2, 4, 6, 8, 10, 3, 3, 3]
>>> sum = 0                               #Why would I set this equal to 0?
>>> for item in some_data:
...     sum += item
...
>>> sum
39

[End of Terminal Display]

Now you try!
"""

#Q02: Multiply List Elements
def list_product(some_list):
    """
    This function takes in a list of numbers and returns the product of the list elements.

    >>> test = [2, 2, 2]
    >>> list_product(test)
    8
    >>> test2 = [10, 20, 30, 0]
    >>> list_product(test2)
    0
    >>> test3 = [1, 1, 1, -1]
    >>> list_product(test3)
    -1
    """
    #YOUR CODE HERE
    return

"""
Sometimes, we have to sift through a list and cut out some elements. How can we do this?
Well, we know how to read a list using a for loop - which goes through list elements one
at a time, in order. But you should have learned about something called a "conditional."
The anatomy of a conditional statement is like so::

if <condition>:
    <code>

Note that <code> will run only if Python evaluates <condition> to be True. For instance,

if x == 1:
    print("Success!")

Here, Python will only display Success! if some variable x is equal to 1. A longer conditional
layout can be as follows:

if <condition>:
    <code>
elif <condition>:
    <code>
else:
    <code>

For if and elif statements, the subsequent indented code will only run if <condition> evaluates
to True. If none of the if statements are True, then the code in the else block will run.

For example,

[Below is a Terminal Display]

>>> def is_positive(num):
...     if num > 0:
...         print("Positive!")
...     else:
...         print("Not positive...")
...
>>> is_positive(20)
Positive!
>>> is_positive(-1)
Not positive...
>>> is_positive(0)
Not positive...

[End of Terminal Display]

Now you try!
"""

#Q03: Number Classifier:
def classify_number(number):
    """
    This function takes in a number and prints whether it is positive, negative, or neither.

    >>> test_numbers = [-100, 0, 100]
    >>> classify_number(1)
    Positive.
    >>> classify_number(-1)
    Negative.
    >>> classify_number(test_numbers[1])
    Zero.
    """
    #YOUR CODE HERE
    return

"""
Now let's combine what you know about iterating through lists and conditional statements.
"""

#Q04: Greater Than 100?
def over_hundred(some_list):
    """
    This function takes in a list and returns whether the sum of the elements of that list
    is greater than 100.

    >>> test_numbers = [-100, 0, 100]
    >>> over_hundred(test_numbers)
    False
    >>> over_hundred([50, 50, 50])
    True
    >>> over_hundred([20, 20, 20, 20, 20, 20, -200])
    False
    >>> nicholas_christmas_lights = [-2000, 9000]
    >>> over_hundred(nicholas_christmas_lights)
    True
    >>> sorry_about_that_problem = [100, -100, 100, -100, 200]
    >>> over_hundred(sorry_about_that_problem)
    True
    >>> i_am_the_best = [100]
    >>> over_hundred(i_am_the_best)
    False
    """
    #YOUR CODE HERE
    return

"""
Fantastic work. Several more things. The first is a dictionary. If given the choice, do not
work with dictionaries. They are fricken slow. However, they are more readable and a useful
structure, especially for databases. They look like this:

[Below is a Terminal Display]

>>> some_dict = {}
>>> some_dict
{}
>>> some_dict['key'] = 'value'
>>> some_dict
{'key': 'value'}

[End of Terminal Display]

Instead of using integers as indices (0, 1, 2, 3, ...) like lists, dictionaries use
user-defined keys as indices, as shown above. So unless you set 0 equal to something
in a dictionary, asking for the 0th index - dict[0], for instance - would make no
sense. Like a list, the elements of a dictionary can be anything.

[Below is a Terminal Display]

>>> another_dict = {}
>>> another_dict[0] = 0
>>> another_dict[1] = 'Random'
>>> another_dict[2] = []
>>> another_dict
{0: 0, 2: [], 1: 'Random'}
>>> another_dict[2].append([])
>>> another_dict
{0: 0, 2: [[]], 1: 'Random'}
>>> list(another_dict.keys())
[0, 2, 1]
>>> list(another_dict.values())
[0, [[]], 'Random']

[End of Terminal Display]

Yes, lists can be in lists. Yes, dictionaries can be in dictionaries. No, dictionaries
do not always display in the order that you construct it in. Okay, now I want you
to build a dictionary using that you've learnt.
"""

#Q05: NAME AND AGE
def name_age(a_list):
    """
    This function takes in a list containing two elements: a string and a number.
    This function returns a dictionary with the string as a key and the number as a value.

    >>> person_age = ['Captain Underpants', 30]
    >>> name_age(person_age)
    {'Captain Underpants': 30}
    >>> list(name_age(person_age).keys())
    ['Captain Underpants']
    >>> list(name_age(person_age).values())
    [30]
    """
    #YOUR CODE HERE
    return

"""
Great. Hopefully all of the work you've done up until this point has clarified a lot of
what lecture has covered. You will learn more throughout the course, and this covers
some of the fundamentals you will need - variables, lists, iterating, dictionaries, and
functions. You have been exposed to other things already - modules/packages such as
numpy and astropy - but these are the fundamentals you will absolutely need as the course
progresses!

Okay, now consider the following problem:
"""

#Q06: USE EVERYTHING YOU KNOW FROM ABOVE FOR THIS!
def filter_flux(fluxes, allowance):
    """
    This function takes in a list of flux readings (basically the amount of light we see) and
    an allowance number (a threshold for acceptance or rejection) and returns either an
    average value or a notice of rejection. If this method of allowing measurement values
    seems wrong to you, trust that feeling. This is a pretty bad method... But it's a start!
    And you should try to implement it before trying for more complicated methods!

    >>> light_data = [300, 400, 600, 800, 800, 900, 900, 1000]
    >>> light_data2 = [21, 78, 32, 56, 128, 98, 82, 46, 55]
    >>> light_data3 = [1, 3, 15, 39, 130, 311, 529, 601, 732]
    >>> filter_flux(light_data, 300)
    712.5
    >>> filter_flux(light_data2, 300)
    Reject this light curve.
    >>> filter_flux(light_data3, 300)
    Reject this light curve.
    """
    #YOUR CODE HERE
    return

"""
Lastly, modules. You need to some basics about these. The ones of primary concern are numpy,
astropy, and matplotlib. Importing a module has the following syntax:

import <module>

You may also write:

import <module> as <shorthand>

This way, you can call a module without typing the entire thing. For instance,

[Below is a Terminal Display]

>>> import pandas as pd
>>> type(pd)
<class 'module'>

[End of Terminal Display]
"""

#Q07: IMPORT THREE MODULES
"""Here, I want you to import numpy (using the name np), matplotlib.pyplot (using the name
plt), and Table from astropy.table."""
#import _ as _
#import _ as _
#from _ import _

"""
LAST FEW REVIEW REMARKS.

You can assign multiple variables at once. For instance,

[Below is a Terminal Display]

>>> a, b = 1, 2
>>> a
1
>>> b
2

[End of Terminal Display]

Numpy arrays are also more convenient to work with than lists. For instance, instead of
using for loops, numpy comes with built-in methods that does a lot of what you'd like to
do. For instance,

[Below is a Terminal Display]

>>> np.array([1, 2, 3]).sum()
6
>>> np.array([1, 1]).mean()
1.0

[End of Terminal Display]

Okay. That was a bit quick, but it should suffice for the last problem.
"""

#Q08a:
def last_problem_a(a_list):
    """
    This function takes in a list and returns a numpy array of that same list, as well
    as the sum and mean of the array. As a hint, you do not have to write loops here!

    >>> type(Table)
    <class 'type'>
    >>> type(plt)
    <class 'module'>
    >>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> array, sum, mean = last_problem_a(data)
    >>> type(array)
    <class 'numpy.ndarray'>
    >>> sum
    55
    >>> mean
    5.5
    """
    #YOUR CODE HERE
    return

#Q08b:
def last_problem_b(database):
    """
    This function takes in a database (STRUCTURED AS A DICTIONARY) and returns a numpy
    array of mean values.
    For instance, if I have a dictionary like so:
    {'a': [100, 200], 'b': [100, 200, 300]},
    then my function should return - maybe in a different order:
    array([150, 200])

    >>> data = {'star_a': [10, 20, 30, 40, 50], 'star_b': [0, 5, 10], 'star_c': [200, 400, 600]}
    >>> averages = last_problem_b(data)
    >>> np.array(averages).mean()
    145.0
    """
    #YOUR CODE HERE
    return

#NOTE: The test in the last problem is to take the mean value of your resultant list of means.
#This is because the dictionary values are not always in the order you generate them in.
#If this is confusing, don't worry for now.
"""
Review these things! Part 1 of the midterm was intended to be primarily review. It's okay
if you did not get these subjects before, and it's okay if you don't fully understand it now.
Next week, Midterm Part 2, will have you working through an astropy table to analyze some
data using the skills you've learned in this review!
"""
