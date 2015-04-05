from utility import *


# Part 1
# print out the information of female students from Indiana
# input: students, which is a list of lists. Each element in students is a list [sid, sname, gender, state]
#        including information of student id, student name, gender and state where the student is from.
def femaleStudents(students):

	for student in students:
		gender = student[2]
		state = student[3]

		if gender == 'Female' and state == 'Indiana':
			printStudent(student)



def printStudent(student):
	sid = student[0]
	name = student[1]
	gender = student[2]
	state = student[3]
	print(sid.ljust(20) + name.ljust(20) + gender.ljust(20) + state.ljust(20))    



def main():
	print "Part1:\n"
	print "StudentId".ljust(20) + "StudentName".ljust(20) +  "Gender".ljust(20) +  "FromWhichState".ljust(20)
	print "==========================================================================="
	femaleStudents(readStudent())

main()