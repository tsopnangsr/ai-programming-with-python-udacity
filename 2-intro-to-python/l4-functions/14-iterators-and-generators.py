#14-iterators-and-generators.py

"""
Iterators And Generators
Iterables are objects that can return one of their elements at a time, such as a list. Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.

An iterator is an object that represents a stream of data. This is different from a list, which is also an iterable, but is not an iterator because it is not a stream of data.

Generators are a simple way to create iterators using functions. You can also define iterators using classes, which you can read more about here.

Here is an example of a generator function called my_range, which produces an iterator that is a stream of numbers from 0 to (x - 1).

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
Notice that instead of using the return keyword, it uses yield. This allows the function to return values one at a time, and start where it left off each time it’s called. This yield keyword is what differentiates a generator from a typical function.

Remember, since this returns an iterator, we can convert it to a list or iterate through it in a loop to view its contents. For example, this code:

for x in my_range(5):
    print(x)
outputs:

0
1
2
3
4
Why Generators?
You may be wondering why we'd use generators over lists. Here’s an excerpt from a stack overflow page that addresses this:

Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.
"""
Quiz: Implement my_enumerate
Write your own generator function that works like the built-in function enumerate.

Calling the function like this:

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
should output:

Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    for i in range(len(iterable)):
        yield (i+start, iterable[i])


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
  


"""Quiz: Chunker
If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files), being able to take and use chunks of it at a time can be very valuable.

Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.

Calling the function like this:
"""
for chunk in chunker(range(25), 4):
    print(list(chunk))
should output:

[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
[16, 17, 18, 19]
[20, 21, 22, 23]
[24]
def chunker(iterable, size):
    # Implement function here
    for i in range(0, len(iterable), size):
        yield iterable[i:i+size]


for chunk in chunker(range(25), 4):
    print(list(chunk))
  


#Generator Expressions
#Here's a cool concept that combines generators and list comprehensions! You can actually create a generator in the same way you'd normally write a list comprehension, except with parentheses instead of square brackets. For example:

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
This can help you save time and create efficient code!




