# read the file into a list called students which is a list of lists
# each element in students is a list [sid, sname, gender, state]
# input: fileName is the name of the file you want to read
# return: the list called students
def readStudent():
 
    # Read the file into list lines
    f = open("student.txt",'r')
    lines = f.readlines()
    f.close()
 
    # This is a list of lists
    studentlist = []
 
    # Parse the lines
    for i in range(len(lines)):
        # Split line on comma '|'
        list = lines[i].split('|')
        sid = list[0].strip().split("=")[1].strip() # LP: since 'split' gives you back an array, you have to use brackets with
                                                    # indices to get the elements out of it (e.g., [0], [1], etc.)
                                                    # and in this case, you always want [1], since calling split('=') on something like
                                                    # 'cid=CS123' gives you an array like ['cid', 'CS123'] and you care about the data
                                                    # which is at index 1, giving you 'CS123'
                                                    # LP: and it's a good idea to use 'strip()'
                                                    # at the end, which removes whitespace at the beginning and end
                                                    # of a string (e.g., " Charlie Day " becomes "Charlie Day")
        name = list[1].strip().split("=")[1].strip()
        gender = list[2].strip().split("=")[1].strip()
        state = list[3].strip().split("=")[1].strip()
 
        entry = [sid, name, gender, state]
 
        studentlist.append(entry)


        # LP: you had the print after the return statement.
        # the function exits after the return statement, so you didn't see
        # the list printed out

    # LP: and here, you want these statements not indented under the 'for'
    # loop, since you want them to happen after it finishes    
    #print studentlist
    return studentlist
        

# read the file into a list called courses which is a list of lists
# each element in courses is a list [cid, cname]
# input: fileName is the name of the file you want to read
# return: the list called courses
def readCourse():
 
    # Read the file into list lines
    f = open("course.txt","r")
    lines = f.readlines()
    f.close()
 
    # This is a list of lists
    courselist = []
 
    # Parse the lines
    for i in range(len(lines)):
        # Split line on comma '|'
        list = lines[i].split('|')
        cid = list[0].strip().split("=")[1].strip()
        name = list[1].strip().split("=")[1].strip()
 
        entry = [cid, name]
 
        courselist.append(entry)
 
    #print courselist
    return courselist

# read the file into a list called registrations which is a list of lists
# each element in registrations is a list [sid, cid, grade]
# input: fileName is the name of the file you want to read
# return: the list called registrations
def readRegistration():
    # Read the file into list lines
    f = open("registration.txt","r")
    lines = f.readlines()
    f.close()
   
    # This is a list of lists
    registrations = []
 
    # Parse the lines
    for i in range(len(lines)):
        # Split line on comma '|'
        list = lines[i].split('|')
        sid = list[0].strip().split("=")[1].strip()
        cid = list[1].strip().split("=")[1].strip()
        grade = list[2].strip().split("=")[1].strip()
 
        entry = [sid, cid, grade]
 
        registrations.append(entry)
    
    #print registrations
    return registrations


def main():
    call1 = readStudent()
    call2 = readCourse()
    call3 = readRegistration()

main()



