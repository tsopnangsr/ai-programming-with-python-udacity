#Zip-and-enumerate

#ZIP: returns and itereator that combines multiple iterables into one sequce of tuples.
#Each tuple contains the elements in that position from all the iterables.


"""
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
#In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
"""


#Enumerate
#enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.

"""
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
This code would output:

0 a
1 b
2 c
3 d
4 e
"""

#Quizz
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for x, y, z, label in zip(x_coord, y_coord, z_coord, labels):
    points.append("{}: {}, {}, {}".format(label, x, y, z))

for point in points:
    print(point)


#Quiz: Zip Lists to a Dictionary
#Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict()
for name, height in zip(cast_names, cast_heights):
    cast[name] = height
    # replace with your code
print(cast)


#Quiz: Unzip Tuples
#Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)



#Quiz: Transpose with Zip
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
"""x, y, z = zip(*data)
a = list()
for i in range(len(x)):
    a.append([x[i], y[i], z[i]])
    
data_transpose = zip(a[0], a[1], a[2], a[3])
"""
# replace with your code
print(data_transpose)



#Quiz: Enumerate
#Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, c in enumerate(cast):
    cast[i] = "{} {}".format(cast[i], heights[i])

print(cast)
  


