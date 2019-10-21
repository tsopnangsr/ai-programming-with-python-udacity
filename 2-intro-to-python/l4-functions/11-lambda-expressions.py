#11-lambda-expressions

"""
Lambda Expressions
You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments.

With a lambda expression, this function:

def multiply(x, y):
    return x * y
can be reduced to:

multiply = lambda x, y: x * y
Both of these functions are used in the same way. In either case, we can call multiply like this:

multiply(4, 7)
This returns 28.

Components of a Lambda Function
The lambda keyword is used to indicate that this is a lambda expression.
Following lambda are one or more arguments for the anonymous function separated by commas, followed by a colon :. Similar to functions, the way the arguments are named in a lambda expression is arbitrary.
Last is an expression that is evaluated and returned in this function. This is a lot like an expression you might see as a return statement in a function.
With this structure, lambda expressions aren’t ideal for complex functions, but can be very useful for short, simple functions.

"""


#Quiz: Lambda with Map
#map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. The code below uses map() to find the mean of each list in numbers to create the list averages. Give it a test run to see what happens.

#Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

#averages = list(map(mean, numbers))
averages = list(map(lambda number: sum(number)/len(number), numbers))
print(averages)



#Quiz: Lambda with Filter
#filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True. The code below uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities. Give it a test run to see what happens.

#Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

#short_cities = list(filter(is_short, cities))
short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)
  
