from utility import *
from plot import *
 
# Part 4
# print out the information of students who are simultaneously 
# taking a course with keyword1 in the course name and a course with keyword2 in the course name
# input: students is a list of lists; each element in students is a list [sid, sname, gender, state]
#        registrations is a list of lists; each element in registrations is a list [sid, cid, grade]
#        courses is a list of lists; each element in courses is a list [cid, cname]
#        keyword1 is a string that will be used to get course id for the course with the keyword1 in the course name
#        keyword2 is a string that will be used to get course id for the course with the keyword2 in the course name
# return: an integer which is the number of students who are taking both course simultaneously
def courseStatistic1(students, registrations, courses, keyword1, keyword2):

	keyword1Cid = getCourseId(courses, keyword1)
	keyword2Cid = getCourseId(courses, keyword2)

	sidsInKeyword1Cid = []
	sidsInKeyword2Cid = []

	for registration in registrations:
		sid = registration[0]
		cid = registration[1]
		grade = registration[2]


		if cid == keyword1Cid:
			sidsInKeyword1Cid.append(sid)
		if cid == keyword2Cid:
			sidsInKeyword2Cid.append(sid)


	# sids in both (idea gotten from http://stackoverflow.com/questions/642763/python-intersection-of-two-lists)
	sidsInBothCids = list(set(sidsInKeyword1Cid).intersection(set(sidsInKeyword2Cid)))

	print "CourseId".ljust(20) + "StudentId".ljust(20) + "StudentName".ljust(20) + "Gender".ljust(20) + "FromWhichState".ljust(20) 
	print "=============================================================================================="

	courses = keyword1Cid + " + " + keyword2Cid
	for student in students:
		sid = student[0]
		name = student[1]
		gender = student[2]
		state = student[3]
		if sid in sidsInBothCids:
			print(courses.ljust(20) + sid.ljust(20) + name.ljust(20) + gender.ljust(20) + state.ljust(20))

	print "The total number of students taking both " + keyword1Cid + " and " + keyword2Cid + " is " + str(len(sidsInBothCids))

	return len(sidsInBothCids)



 
# print out the information of students
# who are taking only the course with keyword in the course name
# input: students is a list of lists; each element in students is a list [sid, sname, gender, state]
#        registrations is a list of lists; each element in registrations is a list [sid, cid, grade]
#        courses is a list of lists; each element in courses is a list [cid, cname]
#        keyword is a string that will be used to get course id for the course with the keyword in the course name
# return: an integer which is the number of students who are taking only the course with the keyword in the course name
def courseStatistic2(students, registrations, courses, keyword):
	
	keywordCid = getCourseId(courses, keyword)


	# get all sids in keywordCid
	sidsInKeywordCid = []
	for registration in registrations:
		sid = registration[0]
		cid = registration[1]
		grade = registration[2]


		if cid == keywordCid:
			sidsInKeywordCid.append(sid)

	# now make sure no sid in 'sidsInKeywordCid' have
	# registrations in another course

	sidsInAnotherCid = []
	for sid in sidsInKeywordCid:
		for registration in registrations:

			registrationSid = registration[0]
			registrationCid = registration[1]

			# if sid is in a course with a cid that doesn't match
			# our keywordCid, remove that sid, since we only 
			# want sids in the course that matches keywordCid
			if sid == registrationSid and registrationCid != keywordCid:
				sidsInAnotherCid.append(sid)


	sidsOnlyInKeywordCid = [sid for sid in sidsInKeywordCid if sid not in sidsInAnotherCid]

	print "CourseId".ljust(20) + "StudentId".ljust(20) + "StudentName".ljust(20) + "Gender".ljust(20) + "FromWhichState".ljust(20) 
	print "=============================================================================================="

	for student in students:
		sid = student[0]
		name = student[1]
		gender = student[2]
		state = student[3]
		if sid in sidsOnlyInKeywordCid:
			print(keywordCid.ljust(20) + sid.ljust(20) + name.ljust(20) + gender.ljust(20) + state.ljust(20))

	print "The total number of students taking only " + keywordCid + " is " + str(len(sidsOnlyInKeywordCid))

	return len(sidsOnlyInKeywordCid)















def part4_main():
	print "Part4:\n"
	numSidsInBoth = courseStatistic1(readStudent(), readRegistration(), readCourse(), "Python", "Java")
	numSidsOnlyInPython = courseStatistic2(readStudent(), readRegistration(), readCourse(), "Python")
	numSidsOnlyInJava = courseStatistic2(readStudent(), readRegistration(), readCourse(), "Java")
	plotPieChart([numSidsInBoth, numSidsOnlyInPython, numSidsOnlyInJava])

#part4_main()