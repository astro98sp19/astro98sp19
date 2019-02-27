"""ASTRONOMY 98/198 SPRING 2019"""
"""HOMEWORK 4"""
"""PLEASE DO NOT DELETE THE ACCOMAPNYING 'planets.csv' FILE WHILE WORKING ON THIS"""

# Q00a: Import Your Module(s)!
###IMPORT MODULES HERE###
#HINT: YOU NEED TO import THREE MODULES FOR THIS HOMEWORK

# Q00b: READ DATA
def read_data(csv):
    """
    This function takes in a string that designates a local directory and returns
    an AstroPy table.

    Parameters
    --------------
    csv (string): the directory for your file

    Returns
    --------------
    astropy table

    Exceptions
    -------------
    Table format must be in .csv.

    >>> k2planets = read_data('planets.csv')
    >>> type(k2planets)
    <class 'astropy.table.table.Table'>
    >>> len(k2planets)
    3917
    >>> k2planets['pl_orbper'][0]
    326.02999999999997
    >>> k2planets.colnames
    ['pl_orbper', 'pl_orbpererr1', 'pl_orbpererr2', 'pl_orbperlim', 'ra_str', 'ra', 'dec_str',
    'dec', 'pl_massj', 'pl_massjerr1', 'pl_massjerr2', 'pl_massjlim', 'pl_masse', 'pl_masseerr1',
    'pl_masseerr2', 'pl_masselim', 'pl_rade', 'pl_radeerr1', 'pl_radeerr2', 'pl_radelim', 'pl_disc']
    """
    ###YOUR CODE HERE (DELETE THE ...)###
    #HINT: You need two keyword arguments when calling astropy.table.Table:
    #(1) format, (2) header_start
    return

#IMPORTANT: WHEN YOU HAVE COMPLETED Q00, UNPOUND THE FOLLOWING LINE:
#k2planets = read_data('planets.csv')

# Q01: YEARS?
def num_planets_discovered_year(atable):
    """
    This function takes in an astropy datatable from the K2 mission and returns a
    dictionary that shows the planets discovered in each year.

    Parameters
    --------------
    atable: astropy table

    Returns
    -------------
    dictionary:
        keys: int (year of planet discovered, e.g. 1989)
        items: int (number of planets discovered)

    Exceptions
    -------------
    Table must have appropriate column names ('pl_disc' is the name of the column for year
    of discovery).

    >>> kyears = np.array(k2planets['pl_disc'])
    >>> kyears.min()
    1989
    >>> kyears.max()
    2019
    >>> nums = num_planets_discovered_year(k2planets)
    >>> nums[1996]
    6
    >>> nums[2018] + nums[2019]
    334
    """
    ###YOUR CODE HERE (DELETE THE ...)###
    return


# Q02: PLOT IT!
def plot_planets_per_year(atable):
    """
    This function takes in an astropy datatable from the K2 mission and produces a plot
    that shows the number of planets discovered in each year.

    Parameters
    --------------
    atable: astropy table

    Returns
    -------------
    x: numpy array (years)
    y: numpy array (number of planets)

    Exceptions
    -------------
    Table must have appropriate column names ('pl_disc' is the name of the column for year
    of discovery).

    >>> x, y = plot_planets_per_year(k2planets)
    >>> type(x)
    <class 'numpy.ndarray'>
    >>> type(y)
    <class 'numpy.ndarray'>
    >>> len(x)
    28
    >>> y.sum()
    3917
    """
    #IF NECESSARY, YOUR CODE HERE. HINT: USE THE FUNCTION FROM Q01
    #AND USE THE .keys() and .values() methods for dictionaries!
    x = #YOUR CODE HERE - HINT: MUST BE A NUMPY ARRAY
    y = #YOUR CODE HERE - HINT: MUST BE A NUMPY ARRAY
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("LABEL YOUR X AXIS")
    ax.set_ylabel("LABEL YOUR Y AXIS")
    ax.set_title("TITLE YOUR PLOT")
    ax.bar(x, y, 0.7)
    #plt.show() - to see your plot. COMMENT THIS OUT WHEN YOU SUBMIT!!!
    return

# Q03: EXOPLANET CLASSIC
def mass_v_per(atable):
    """
    This function takes in an astropy table, plots the mass versus period of the
    datatable, and returns two lists.

    Parameters
    --------------
    atable: astropy table

    Returns
    -------------
    x: numpy array (period)
    y: numpy array (in jupiter mass)

    Exceptions
    -------------
    Table must have appropriate column names.

    >>> x, y = mass_v_per(k2planets)
    >>> type(x)
    <class 'numpy.ndarray'>
    >>> type(y)
    <class 'numpy.ndarray'>
    >>> y.max()
    30.0
    >>> x.max()
    7300000.0
    """
    #IF NECESSARY YOUR CODE HERE
    x = #YOUR CODE HERE - HINT: MUST BE A NUMPY ARRAY
    y = #YOUR CODE HERE - HINT: MUST BE A NUMPY ARRAY
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("LABEL YOUR X AXIS")
    ax.set_ylabel("LABEL YOUR Y AXIS")
    ax.set_title("TITLE YOUR PLOT")
    ax.scatter(x, y, label = "K2 Confirmed Planet")
    ax.legend()
    #plt.show() - to see your plot. COMMENT THIS OUT WHEN YOU SUBMIT!!!
    return
