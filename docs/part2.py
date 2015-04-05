from utility import *
 
# Part 2    
# print out the information of students who are taking a course with the keyword in the course name  
# input: students is a list of lists; each element in students is a list [sid, sname, gender, state]
#        registrations is a list of lists; each element in registrations is a list [sid, cid, grade]
#        courses is a list of lists; each element in courses is a list [cid, cname]
#        keyword is a string that will be used to get course id for the course with the keyword in the course name
def studentsInPython(students, registrations, courses, keyword):

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

	# find which students are included in our sids list
	for student in students:
		sid = student[0]

		# if student's sid is in the sids list
		# we want to see their info
		if sid in sids:
			printStudent(student)


def main():
	print "Part2:\n"
	print "StudentId".ljust(20) + "StudentName".ljust(20) +  "Gender".ljust(20) +  "FromWhichState".ljust(20)
	print "==========================================================================="
	studentsInPython(readStudent(), readRegistration(), readCourse(), "Python")

main()