#3-lab-instructions.py

Principle Objectives
Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs.
 
Correctly classify the breed of dog, for the images that are of dogs.
 
Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve the objectives _1_ and _2_.
 
Consider the time resources required to best achieve objectives _1_ and _2_, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.
TODO: Edit program check_images.py
The check_images.py is the program file that you will be editing to achieve the four objectives above. This file contains a main() function that outlines how to complete this program through using functions that have not yet been defined. You will be creating these undefined functions in check_images.py to achieve the objectives above.

For students that:
Have less time to devote to the lab,
Are new to Python and/or programming, or
Feel less comfortable with programming in Python.
We have provided an alternative version of check_images.py named check_images_hints.py . It's the same as check_images.py, except check_images_hints.py:

Provides more of the instructor solution, so there is less for the student to code on their own.
Provides detailed directions on the sections that the student is expected to code on their own.
Both check_images.py and check_images_hints.py will reach the same solution, so the solutions videos at the end of each section apply to both. It is left for the student to decide which version of the lab (check_images.py or check_images_hints.py) that they want to complete. Please note that when we refer to check_images.py in 6. Timing Code through 15. Printing Results we are referring to check_images.py OR check_images_hints.py which ever program you decided to edit for this lab.

Note that:
Before beginning the lab please review the Frequently Asked Questions, FAQ, about the lab. This FAQ covers questions that frequently appeared in Slack for AIPND.
If a students decides to complete the more challenging version of the lab (check_images.py); they are encouraged to look at check_images_hints.py for hints if they get stuck completing part of the lab.
This lab and other lessons within the Nanodegree will be using a GitHub repository to store program files and other resources for this Nanodegree. To learn more about GitHub, please see the GitHub Lesson that's located within the Extracurricular section of this Nanodegree. This optional material is provided to give students more information on how to use GitHub for those that are less familiar with GitHub.
The Lab Workspace concept is setup with the programs and files (like pet_images folder) you will need to complete the lab. It is recommended that you only edit and change the check_images.py(or check_images_hints.py) program to complete the lab. Changes to other files and programs within this Workspace can result in your program not running appropriately even if you have coded it correctly.
The Python comments that begin with # TODO: in check_images.py(or check_images_hints.py) program indicates where you will need to change the code of the program. The comments in check_images.py(or check_images_hints.py) will help you make changes so that your program will achieve the principle objectives above.
Function docstrings contain input parameters and return values, which were left to provide guidance for achieving the instructor provided solution using check_images.py. These serve as helpful guidance, you are welcome to program these functions differently as long as you achieve the objectives above. If you decided to edit check_images_hints.py instead of check_images.py, you will have to use the variable, argument, and parameter names within the check_images_hints.py program.
6. Timing Code to 15. Printing Results will provide additional guidance for programming the undefined functions and completing the check_images.py(or check_images_hints.py) program. This information has been provided to you to help you complete the lab more quickly.
Specifically the information provides:

Which Lessons to review regarding programming the undefined functions.
Details about the assignment's files (e.g. image files in pet_images folder, dognames.txt).
Details regarding using the classifier function in classifier.py.
Links to relevant python documentation.
Relevant example code (see "Example Code" section below).
Students can use the functions within the program print_functions_for_lab_checks.py to check their code for sections 7. Command Line Arguments through 14. Calculating Results. Students will find this program within the Lab Workspace and within the GitHub repository (see link above). The docstring below each function definition within print_functions_for_lab_checks.py, describes how to use the function. Additionally, one can find each function used within the Lab Solution (see below).

The Lab Solution can be found within 18. Lab Solution Workspace and within the GitHub repository as check_images_solution.py.
Program Outline
Repeat below for all three image classification algorithms (e.g. input algorithm as command line argument):

Time your program
Use Time Module to compute program runtime
Get program Inputs from the user
Use command line arguments to get user inputs
Create Pet Images Labels
Use the pet images filenames to create labels
Store the pet image labels in a data structure (e.g. dictionary)
Create Classifier Labels and Compare Labels
Use the Classifier function classify the images and create the classifier labels
Compare Classifier Labels to Pet Image Labels
Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists)
Classifying Labels as "Dogs" or "Not Dogs"
Classify all Labels (Pet & Classifier) as "Dogs" or "Not Dogs" using dognames.txt file
Store new classifications in the complex data structure (e.g. dictionary of lists)
Calculate the Results
Use Labels and their classifications to determine how well the algorithm worked on classifying images.
Print the Results
Example Code
You will find example code within most sections within the classroom. Additionally, this example code has been provided for you as python programs in the Github repository at the end of the section, within the classroom. When you see the title Code, what follows is a link to the example code program in the Github repository.

Note
If you plan on copying all or part of the example code within the sections, please copy it from the Github repository. Copying example code from the sections within the classroom, could result with syntax errors regarding indention and/or tabs.

Solutions Videos
At the end of each concept you will find a solutions video, that walks through the solution for what you just programmed. In the solution videos, we describe ways to test your program to make sure it is producing the expected results; as a means to catch any programming errors early, before you have completed coding. We recommended watching the video and checking your code after coding each undefined function.


