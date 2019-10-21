#defining functions

#A function definitions starts with "def" followed by the name of the function
#Arguments: Values passed in as inputs to a functions
#Local varible: variable that can just be used within the body of the function
#"return" key workd is used to give an output value when the function is called.



#Quiz Solution: Population Density Function
def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2


#Quiz Solution: readable_timedelta
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))


