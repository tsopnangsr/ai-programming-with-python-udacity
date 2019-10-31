#9-students-missing-assignments.py

names = list() # get and process input for a list of names
assignments = list() # get and process input for a list of the number of assignments
grades = list() # get and process input for a list of grades

names = input("Enter names separeted with commas: ").split(",")
assignments = input("Enter assignments separeted with commas: ").split(",")
grades = input("Enter grades separeted with commas: ").split(",")

#print(grades)
# message string to be used for each student
# HINT: use .format() with this string in your for loop
for i in range(len(names)):
	message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
	submit before you can graduate. You're current grade is {} and can increase \
	to {} if you submit all assignments before the due date.\n\n".format(names[i], assignments[i], grades[i], int(grades[i])+2*int(assignments[i]))
	print(message)

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

