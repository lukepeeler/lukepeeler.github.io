from utility import *
from plot import *

#Write a program called part3.py to print out statistics of states from where students 
#who are taking a Java course come from, and also show the results in a bar chart.
 
# Part 3
# print out statistics of states where students 
# who are taking a course with the keyword in the course name come from
# input: students is a list of lists; each element in students is a list [sid, sname, gender, state]
#        registrations is a list of lists; each element in registrations is a list [sid, cid, grade]
#        courses is a list of lists; each element in courses is a list [cid, cname]
#        keyword is a string that will be used to get course id for the course with the keyword in the course name
# return: a list of lists. Each element is a list [[state1, numer1], [state2, number2], ...]    
def stateStatistic(students, registrations, courses, keyword): 

	keywordCid = getCourseId(courses, keyword)

	# get each sid for each student with registration in 'keywordCid'
	sids = []
	for registration in registrations:
		sid = registration[0]
		cid = registration[1]
		grade = registration[2]

		# if this registration cid matches the keywordCid
		# we want to include the student's sid in our list
		if cid == keywordCid:
			sids.append(sid)


	statesList = []
	# find which students are included in our sids list
	# so we can account for them in our statesList
	for student in students:
		sid = student[0]

		# if student's sid is in the sids list
		# we want to add them to our running list
		# of states and number of students
		if sid in sids:
			addStudentToStatesList(student, statesList)

	return statesList


def addStudentToStatesList(student, statesList):

	studentState = student[3]

	entryAddedToList = False
	for entry in statesList:
		state = entry[0]

		# if the state is already in our list
		# we just increment the number of students
		# for that state, and we're done, so we should return
		if state == studentState:
			entry[1] = entry[1] + 1
			return

	# if we get here, that means we didn't find the
	# student's state in the list, so we should add it
	# to account for this student
	statesList.append([studentState, 1])




def main():

	statesList = stateStatistic(readStudent(), readRegistration(), readCourse(), "Java")
	print "State".ljust(20) + "Number".ljust(20)        
	print "=========================="
	for entry in statesList:
		state = entry[0]
		numStudents = entry[1]
		print state.ljust(20) + str(numStudents).ljust(20)
	plotBarChart(statesList)


main()


