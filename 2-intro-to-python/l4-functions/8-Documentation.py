#8-Documentation.py

#Documentation
#Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings. Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.

def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area

#Quiz: Write a Docstring
#Write a docstring for the readable_timedelta function you defined earlier! Remember the way you write your docstrings is pretty flexible! Look through Python's docstring conventions here and check out this Stack Overflow page for some inspiration!

def readable_timedelta(days):
    # insert your docstring here
    """This function gives a more easier and readable way to show number of days
    INPUT:
    days: number to days you want to convert into week + days format
    OUTPUT: 
    text_week_days: String that give a readable way using week(s) and day(s)
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)



