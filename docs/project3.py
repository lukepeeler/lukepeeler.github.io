from utility import *
from plot import *
from part1 import *
from part2 import *
from part3 import *
from part4 import *
 
 
def main():
    # Read data from student.txt, course.txt and registration.txt
    # into 3 lists called students, courses and registrations, respectively.
    # You will need to call appropriate functions in utility.py
	students = readStudent()
	courses = readCourse()
	registrations = readRegistration()
 	

 	while True:
	    # Your code to output the selection options on the screen for users to select
		print "***************************"
		print "*    1. To run part 1     *"
		print "*    2. To run part 2     *"
		print "*    3. To run part 3     *"
		print "*    4. To run part 4     *"
		print "*    5. To exit           *"
		print "***************************"
		print "\nPlease select [1 - 5] to run different parts:"
    	

    	# Your code to allow users to select different parts to run
    	# You are required to use a while loop
		selection = raw_input()

		if selection == "1":
			part1_main()
		elif selection == "2":
			part2_main()
		elif selection == "3":
			part3_main()
 		elif selection == "4":
			part4_main()
 		elif selection == "5":
			print "Later, gator"
 			return
		else:
			print "Unrecognized input: '" + selection + "'"
			print "Please make another selection according to the available options."

main()